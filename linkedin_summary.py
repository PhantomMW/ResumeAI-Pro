import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_linkedin_summary(
    resume_text,
    job_title
):

    prompt = f"""
You are an expert LinkedIn Profile Writer.

Using the following resume, write a professional LinkedIn About section.

Target Position:
{job_title}

Resume:
{resume_text}

Requirements:

- 150–250 words
- Professional
- ATS Friendly
- Strong opening
- Highlight achievements
- Mention technical skills
- Mention soft skills
- End with career objective

Return ONLY the LinkedIn About section.
"""

    response = model.generate_content(prompt)

    return response.text