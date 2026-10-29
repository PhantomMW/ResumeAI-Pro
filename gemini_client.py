import os
import time

import google.generativeai as genai
from google.api_core.exceptions import (
    ResourceExhausted,
    ServiceUnavailable,
    DeadlineExceeded
)

from config import GEMINI_API_KEY, MODEL_NAME


# ==========================================
# Configure Gemini
# ==========================================

_configured_key = None
_model_instance = None


def get_model():
    global _configured_key, _model_instance

    current_key = GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")

    if current_key and current_key != _configured_key:
        genai.configure(api_key=current_key)
        _configured_key = current_key
        _model_instance = genai.GenerativeModel(MODEL_NAME)

    if _model_instance is None:
        if current_key:
            genai.configure(api_key=current_key)
            _configured_key = current_key
            _model_instance = genai.GenerativeModel(MODEL_NAME)
        else:
            _model_instance = genai.GenerativeModel(MODEL_NAME)

    return _model_instance


# ==========================================
# AI Client
# ==========================================

def generate_ai_response(prompt, retries=3):
    current_key = GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")

    if not current_key:
        return (
            "⚠️ Gemini API Key is missing.\n\n"
            "Please add your Gemini API Key to `.env` or `.streamlit/secrets.toml` as:\n"
            "```\nGEMINI_API_KEY=\"your_key_here\"\n```"
        )

    model = get_model()

    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text

        except ResourceExhausted:
            return (
                "⚠️ Gemini API quota has been exceeded.\n\n"
                "Please try again later or use another API Key."
            )

        except (ServiceUnavailable, DeadlineExceeded):
            if attempt < retries - 1:
                time.sleep(2)
                continue

            return (
                "⚠️ Gemini service is temporarily unavailable.\n\n"
                "Please try again in a few minutes."
            )

        except Exception as e:
            return (
                "⚠️ Unexpected AI Error\n\n"
                f"{str(e)}"
            )
