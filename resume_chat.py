import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_resume_ai(
    resume_text,
    job_title,
    job_description,
    question
):

    prompt = f"""
You are an expert Career Coach, ATS Specialist, and Senior HR Manager.

The user has already uploaded this resume.

Resume:
{resume_text}

Target Job:
{job_title}

Job Description:
{job_description}

The user asks:

{question}

Answer professionally.

Give practical advice.

If the question is about improving the resume,
answer based ONLY on the uploaded resume.

Keep the answer concise.
"""

    response = model.generate_content(prompt)

    return response.text