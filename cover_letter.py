from gemini_client import generate_ai_response


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

    return generate_ai_response(prompt)