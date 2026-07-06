import os
from dotenv import load_dotenv
import streamlit as st

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

# ==========================================
# Gemini API Key
# ==========================================

if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==========================================
# Gemini Model
# ==========================================

MODEL_NAME = "gemini-2.5-flash"

# ==========================================
# Application Settings
# ==========================================

APP_TITLE = "ResumeAI Pro"

APP_VERSION = "2.0"