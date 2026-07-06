import json

from prompts import resume_analysis_prompt
from gemini_client import generate_ai_response

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

def analyze_resume(
    resume_text,
    job_title,
    job_description
):

    prompt = resume_analysis_prompt(
        resume_text,
        job_title,
        job_description
    )

    try:

        response = generate_ai_response(prompt)

        if response.startswith("⚠️"):

            error = DEFAULT_RESPONSE.copy()

            error["summary"] = response

            error["overall_recommendation"] = (
                "The AI service is currently unavailable."
            )

            return error

        cleaned = clean_response(response)

        result = json.loads(cleaned)

        for key, value in DEFAULT_RESPONSE.items():

            if key not in result:

                result[key] = value

        return result

    except json.JSONDecodeError:

        error = DEFAULT_RESPONSE.copy()

        error["summary"] = (
            "Failed to parse the AI response."
        )

        error["overall_recommendation"] = (
            "The AI returned an invalid JSON response."
        )

        return error

    except Exception as e:

        error = DEFAULT_RESPONSE.copy()

        error["summary"] = str(e)

        error["overall_recommendation"] = (
            "Unexpected error occurred while analyzing the resume."
        )

        return error