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

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


# ==========================================
# AI Client
# ==========================================

def generate_ai_response(prompt, retries=3):

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