import json
import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def clean_response(text):

    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    if text.startswith("```"):
        text = text.replace("```", "")

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def generate_career_advice(
    resume_text,
    job_title,
    job_description
):

    prompt = f"""
You are an expert Career Coach, HR Manager, and Technical Mentor.

Analyze the following resume and generate professional career advice.

Target Job:
{job_title}

Job Description:
{job_description}

Resume:
{resume_text}

Return ONLY a valid JSON.

Schema:

{{
"career_level":"",
"next_role":"",
"skills_to_learn":[],
"recommended_certifications":[],
"learning_roadmap":[],
"career_advice":""
}}

Rules:

- career_level:
Junior / Mid-Level / Senior

- next_role:
Best next career step.

- skills_to_learn:
Return exactly 5 skills.

- recommended_certifications:
Return exactly 5 certificates.

- learning_roadmap:
Return exactly 6 roadmap steps.

- career_advice:
4-6 lines.

Return ONLY JSON.
"""

    try:

        response = model.generate_content(prompt)

        cleaned = clean_response(response.text)

        return json.loads(cleaned)

    except Exception:

        return {

            "career_level": "Unknown",

            "next_role": "Not Available",

            "skills_to_learn": [],

            "recommended_certifications": [],

            "learning_roadmap": [],

            "career_advice":
            "Unable to generate career advice."

        }