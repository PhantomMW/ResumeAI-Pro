from gemini_client import generate_ai_response


def generate_linkedin_summary(
    resume_text,
    job_title
):

    prompt = f"""
You are a professional LinkedIn branding expert.

Write an outstanding LinkedIn About section.

Target Job:

{job_title}

Resume:

{resume_text}

Requirements:

- Professional tone
- First person
- Around 200 words
- Highlight experience
- Mention technical skills
- Mention achievements
- End with career goals
"""

    return generate_ai_response(prompt)