from gemini_client import generate_ai_response
import json


def generate_career_advice(
    resume_text,
    job_title,
    job_description
):

    prompt = f"""
You are an expert Career Coach.

Analyze the resume and provide career advice.

Resume:

{resume_text}

Target Job:

{job_title}

Job Description:

{job_description}

Return ONLY a valid JSON object with the following structure:

{{
    "career_level": "",
    "next_role": "",
    "skills_to_learn": [],
    "recommended_certifications": [],
    "learning_roadmap": [],
    "career_advice": ""
}}
"""

    response = generate_ai_response(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "career_level": "Unknown",
            "next_role": "Unknown",
            "skills_to_learn": [],
            "recommended_certifications": [],
            "learning_roadmap": [],
            "career_advice": response
        }