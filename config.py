import os
from dotenv import load_dotenv
import streamlit as st

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

# ==========================================
# Gemini API Key (Safe Loading)
# ==========================================

GEMINI_API_KEY = None

# Safely check Streamlit secrets without raising StreamlitSecretNotFoundError
try:
    if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

# Fallback to operating system environment variables or .env file
if not GEMINI_API_KEY:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# ==========================================
# Gemini Model
# ==========================================

MODEL_NAME = "gemini-2.5-flash"

# ==========================================
# Application Settings
# ==========================================

APP_TITLE = "ResumeAI Pro"

APP_VERSION = "2.0"
