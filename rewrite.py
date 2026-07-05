import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def rewrite_resume(
    resume_text,
    job_title,
    job_description
):

    prompt = f"""
You are an expert Resume Writer and Senior HR Manager.

Rewrite the following resume professionally for this position.

Target Job:
{job_title}

Job Description:
{job_description}

Resume:
{resume_text}

Requirements:

- Keep the information truthful.
- Improve wording and professionalism.
- Optimize for ATS.
- Improve grammar.
- Improve formatting.
- Use strong action verbs.
- Highlight achievements.
- Organize sections clearly.
- Keep the resume concise.
- Return ONLY the rewritten resume.
"""

    response = model.generate_content(prompt)

    return response.text