from gemini_client import generate_ai_response


def ask_resume_ai(
    resume_text,
    job_title,
    job_description,
    question
):

    prompt = f"""
You are an AI Resume Expert.

Answer the user's question based ONLY on the resume and job description.

Resume:

{resume_text}

Target Job:

{job_title}

Job Description:

{job_description}

User Question:

{question}

Provide a professional and helpful answer.
"""

    return generate_ai_response(prompt)