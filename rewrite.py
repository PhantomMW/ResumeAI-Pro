from gemini_client import generate_ai_response


def rewrite_resume(
    resume_text,
    job_title,
    job_description
):

    prompt = f"""
You are an expert ATS Resume Writer.

Rewrite the following resume professionally.

Target Job:

{job_title}

Job Description:

{job_description}

Resume:

{resume_text}

Requirements:

- ATS Optimized
- Professional Formatting
- Improve Bullet Points
- Keep all truthful information
- Improve readability
- Modern resume style
"""

    return generate_ai_response(prompt)