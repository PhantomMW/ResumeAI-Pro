from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

from reportlab.lib.colors import darkblue


def generate_pdf(result, job_title):

    filename = "Resume_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title = styles["Heading1"]

    title.alignment = TA_CENTER

    title.textColor = darkblue

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    story.append(
        Paragraph(
            "AI Resume Analyzer Report",
            title
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Target Job:</b> {job_title}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {result.get('ats_score',0)}/100",
            normal
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "Professional Summary",
            heading
        )
    )

    story.append(
        Paragraph(
            result.get(
                "summary",
                ""
            ),
            normal
        )
    )

    story.append(Spacer(1,20))

    sections = [

        ("Strengths","strengths"),

        ("Weaknesses","weaknesses"),

        ("Missing Skills","missing_skills"),

        ("Resume Improvements","improvements"),

        ("Interview Questions","interview_questions")

    ]

    for title_text,key in sections:

        story.append(
            Paragraph(
                title_text,
                heading
            )
        )

        values = result.get(key,[])

        if isinstance(values,list):

            for item in values:

                story.append(
                    Paragraph(
                        f"• {item}",
                        normal
                    )
                )

        story.append(Spacer(1,15))

    reviews = [

        ("Experience Review","experience_review"),

        ("Education Review","education_review"),

        ("Projects Review","projects_review"),

        ("Certifications Review","certifications_review"),

        ("Overall Recommendation","overall_recommendation")

    ]

    for title_text,key in reviews:

        story.append(
            Paragraph(
                title_text,
                heading
            )
        )

        story.append(
            Paragraph(
                result.get(
                    key,
                    ""
                ),
                normal
            )
        )

        story.append(Spacer(1,15))

    doc.build(story)

    return filename


def generate_cover_letter_pdf(letter):

    filename = "Cover_Letter.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER
    title.textColor = darkblue

    normal = styles["BodyText"]

    story = []

    story.append(
        Paragraph(
            "AI Generated Cover Letter",
            title
        )
    )

    story.append(Spacer(1,20))

    paragraphs = letter.split("\n")

    for line in paragraphs:

        if line.strip() != "":

            story.append(
                Paragraph(
                    line,
                    normal
                )
            )

            story.append(Spacer(1,8))

    doc.build(story)

    return filename
def generate_rewritten_resume_pdf(text):

    filename = "Rewritten_Resume.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER
    title.textColor = darkblue

    normal = styles["BodyText"]

    story = []

    story.append(
        Paragraph(
            "AI Rewritten Resume",
            title
        )
    )

    story.append(Spacer(1,20))

    for line in text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line,
                    normal
                )
            )

            story.append(Spacer(1,8))

    doc.build(story)

    return filename