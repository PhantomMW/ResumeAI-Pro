import json
import google.generativeai as genai

from config import GEMINI_API_KEY
from prompts import resume_analysis_prompt

# ==========================================
# Configure Gemini
# ==========================================

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# ==========================================
# Default Response
# ==========================================

DEFAULT_RESPONSE = {
    "ats_score": 0,
    "resume_score": 0,
    "job_match": 0,
    "grammar_score": 0,
    "formatting_score": 0,
    "keyword_score": 0,

    "career_level": "",
    "industry_fit": "",

    "summary": "",

    "hard_skills": [],
    "soft_skills": [],

    "strengths": [],
    "weaknesses": [],
    "matched_skills": [],
    "missing_skills": [],
    "improvements": [],

    "experience_review": "",
    "education_review": "",
    "projects_review": "",
    "certifications_review": "",

    "overall_recommendation": "",

"hiring_decision": "",

"hiring_reason": "",

    "interview_questions": []
}


# ==========================================
# Clean Gemini Response
# ==========================================

def clean_response(text):

    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    if text.startswith("```"):
        text = text.replace("```", "")

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


# ==========================================
# Analyze Resume
# ==========================================

def analyze_resume(resume_text, job_title, job_description):

    prompt = resume_analysis_prompt(
        resume_text,
        job_title,
        job_description
    )

    try:

        response = model.generate_content(prompt)

        cleaned = clean_response(response.text)

        result = json.loads(cleaned)

        # Fill missing keys automatically
        for key, value in DEFAULT_RESPONSE.items():
            if key not in result:
                result[key] = value

        return result

    except json.JSONDecodeError:

        error = DEFAULT_RESPONSE.copy()

        error["summary"] = "Failed to parse Gemini response."

        error["overall_recommendation"] = (
            "Gemini returned an invalid JSON response."
        )

        return error

    except Exception as e:

        error = DEFAULT_RESPONSE.copy()

        error["summary"] = str(e)

        error["overall_recommendation"] = (
            "Unexpected error occurred while analyzing the resume."
        )

        return error