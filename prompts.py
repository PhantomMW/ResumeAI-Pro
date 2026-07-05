def resume_analysis_prompt(resume_text, job_title, job_description):

    return f"""
You are an expert ATS System, Senior HR Manager, Technical Recruiter, Career Coach, and Resume Reviewer.

Your task is to perform a complete professional resume analysis.

==================================================
TARGET JOB
==================================================

Job Title:
{job_title}

Job Description:
{job_description}

==================================================
RESUME
==================================================

{resume_text}

==================================================
TASK
==================================================

Analyze the resume exactly as an Applicant Tracking System (ATS) and an experienced HR Manager would.

Evaluate:

- ATS compatibility
- Resume quality
- Job matching
- Grammar
- Formatting
- Keywords
- Hard Skills
- Soft Skills
- Experience
- Education
- Projects
- Certifications
- Missing Skills
- Career Level
- Industry Fit
- Hiring Recommendation

==================================================
RETURN FORMAT
==================================================

Return ONLY one valid JSON object.

The JSON MUST follow this schema EXACTLY.

{{
    "ats_score": 0,

    "resume_score": 0,

    "job_match": 0,

    "grammar_score": 0,

    "formatting_score": 0,

    "keyword_score": 0,

    "career_level": "",

    "industry_fit": "",

    "summary": "",

    "hard_skills": [],

    "soft_skills": [],

    "strengths": [],

    "weaknesses": [],

    "matched_skills": [],

    "missing_skills": [],

    "improvements": [],

    "experience_review": "",

    "education_review": "",

    "projects_review": "",

    "certifications_review": "",

    "overall_recommendation": "",

"hiring_decision": "",

"hiring_reason": "",

"interview_questions": []
}}

==================================================
RULES
==================================================

ATS Score:
Return an integer between 0 and 100.

Resume Score:
Return an integer between 0 and 100.

Job Match:
Return an integer between 0 and 100 based on the provided job description.

Grammar Score:
Return an integer between 0 and 100.

Formatting Score:
Return an integer between 0 and 100.

Keyword Score:
Return an integer between 0 and 100 based on ATS keyword optimization.

Career Level:
Choose ONLY one of the following:

Intern
Junior
Mid-Level
Senior
Lead

Industry Fit:
Return the most suitable industry for the candidate.

Summary:
Write 3-5 professional sentences.

Hard Skills:
Return between 6 and 12 technical skills extracted from the resume.

Soft Skills:
Return between 5 and 10 soft skills extracted from the resume.

Strengths:
Return between 5 and 8 strengths.

Weaknesses:
Return between 3 and 5 weaknesses.

Matched Skills:
Return technical skills that match the target job.

Missing Skills:
Return ONLY technical skills missing for the target job.

Improvements:
Return exactly 5 practical recommendations.

Experience Review:
Write a professional review of the experience section.

Education Review:
Write a professional review of the education section.

Projects Review:
Evaluate the quality and relevance of the projects.

Certifications Review:
Evaluate the certifications.

Overall Recommendation:
Provide a concise hiring recommendation.

Hiring Decision:
Choose ONLY one:

Highly Recommended
Recommended
Needs Improvement

Hiring Reason:
Explain the hiring decision in 2-3 sentences.

Interview Questions:
Return EXACTLY 7 interview questions specifically related to the target job.

==================================================
IMPORTANT
==================================================

Return ONLY valid JSON.

Do NOT return Markdown.

Do NOT use ```json.

Do NOT include explanations.

Do NOT include comments.

Do NOT include additional text.

Every score MUST be an integer.

Every list MUST be a valid JSON array.

The JSON must be directly parsable using Python json.loads().
"""