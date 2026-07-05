import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_cover_letter(
    resume_text,
    job_title,
    job_description
):

    prompt = f"""
You are an expert HR Manager.

Write a professional Cover Letter.

Job Title:

{job_title}

Job Description:

{job_description}

Resume:

{resume_text}

Requirements:

- Professional tone
- One page maximum
- Strong introduction
- Mention relevant skills
- Mention projects if available
- Strong closing paragraph
"""

    response = model.generate_content(prompt)

    return response.text