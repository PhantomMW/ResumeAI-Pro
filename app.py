import streamlit as st
import time

from ui import (
    configure_page,
    render_sidebar,
    render_header,
    upload_section,
    render_footer
)

from parser import extract_resume_text
from analyzer import analyze_resume
from utils import clean_text
from results import render_results

from cover_letter import generate_cover_letter
from rewrite import rewrite_resume
from linkedin_summary import generate_linkedin_summary
from resume_chat import ask_resume_ai
from career_advisor import generate_career_advice
from history import (
    save_analysis,
    load_history
)

from report import (
    generate_pdf,
    generate_cover_letter_pdf,
    generate_rewritten_resume_pdf
)

# ==========================================
# Session State
# ==========================================

DEFAULT_STATES = {
    "result": None,
    "resume_text": "",
    "job_title": "",
    "job_description": "",
    "cover_letter": "",
    "rewritten_resume": "",
    "linkedin_summary": "",
    "ai_answer": ""
}

for key, value in DEFAULT_STATES.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ==========================================
# Reset Analysis
# ==========================================

def reset_analysis():

    keys = [
        "result",
        "resume_text",
        "job_title",
        "job_description",
        "cover_letter",
        "rewritten_resume",
        "linkedin_summary",
        "ai_answer",
        "career"
    ]

    for key in keys:

        if key in st.session_state:

            del st.session_state[key]


# ==========================================
# Configure Page
# ==========================================

configure_page()

render_sidebar()

render_header()


# ==========================================
# Upload Section
# ==========================================

uploaded_file, job_title, job_description, analyze = upload_section()


# ==========================================
# Analyze Resume
# ==========================================

if analyze:

    if uploaded_file is None:

        st.error("Please upload your resume.")
        st.stop()

    if not job_title.strip():

        st.error("Please enter the target job title.")
        st.stop()

    resume_text = extract_resume_text(
        uploaded_file
    )

    resume_text = clean_text(
        resume_text
    )

    if not resume_text:

        st.error(
            "Unable to read the uploaded resume."
        )

        st.stop()

    # ==========================================
    # Loading Progress
    # ==========================================

    progress = st.progress(0)

    status = st.empty()

    status.info("📄 Reading Resume...")
    progress.progress(15)

    status.info("🧹 Cleaning Resume...")
    progress.progress(30)

    status.info("🧠 Initializing AI...")
    progress.progress(45)

    result = analyze_resume(

        resume_text=resume_text,

        job_title=job_title,

        job_description=job_description

    )

    status.info("📊 Processing Results...")
    progress.progress(85)

    status.info("📑 Finalizing Report...")
    progress.progress(100)

    status.success("✅ Analysis Completed!")

    time.sleep(0.5)

    progress.empty()

    status.empty()

    # ==========================================
    # Save Session
    # ==========================================

    st.session_state.result = result

    st.session_state.resume_text = resume_text

    st.session_state.job_title = job_title

    st.session_state.job_description = job_description

    # ==========================================
    # Save History
    # ==========================================

    save_analysis(

        job_title,

        result

    )
    # ==========================================
# Show Results
# ==========================================

if st.session_state.result is not None:

    render_results(

        result=st.session_state.result,

        job_title=st.session_state.job_title

    )

    # ==========================================
    # Professional PDF Report
    # ==========================================

    st.divider()

    st.subheader("📄 Professional Report")

    pdf_file = generate_pdf(

        st.session_state.result,

        st.session_state.job_title

    )

    with open(pdf_file, "rb") as file:

        st.download_button(

            label="📄 Download Professional PDF Report",

            data=file,

            file_name=pdf_file,

            mime="application/pdf",

            use_container_width=True

        )

    # ==========================================
    # Cover Letter Generator
    # ==========================================

    st.divider()

    st.subheader("💌 AI Cover Letter Generator")

    st.write(
        "Generate a professional cover letter based on your resume and the selected job."
    )

    if st.button(

        "💌 Generate Cover Letter",

        use_container_width=True

    ):

        with st.spinner(
            "Gemini is writing your Cover Letter..."
        ):

            cover_letter = generate_cover_letter(

                st.session_state.resume_text,

                st.session_state.job_title,

                st.session_state.job_description

            )

        st.session_state.cover_letter = cover_letter

    if st.session_state.cover_letter:

        st.success(
            "Cover Letter Generated Successfully"
        )

        st.text_area(

            "Cover Letter",

            value=st.session_state.cover_letter,

            height=500

        )

        cover_pdf = generate_cover_letter_pdf(

            st.session_state.cover_letter

        )

        with open(cover_pdf, "rb") as pdf:

            st.download_button(

                label="📄 Download Cover Letter (PDF)",

                data=pdf,

                file_name=cover_pdf,

                mime="application/pdf",

                use_container_width=True

            )

    # ==========================================
    # Resume Rewriter
    # ==========================================

    st.divider()

    st.subheader("✨ AI Resume Rewriter")

    st.write(
        "Generate an ATS-optimized version of your resume."
    )

    if st.button(

        "✨ Rewrite Resume",

        use_container_width=True

    ):

        with st.spinner(
            "AI is rewriting your resume..."
        ):

            rewritten_resume = rewrite_resume(

                st.session_state.resume_text,

                st.session_state.job_title,

                st.session_state.job_description

            )

        st.session_state.rewritten_resume = rewritten_resume

    if st.session_state.rewritten_resume:

        st.success(
            "Resume rewritten successfully!"
        )

        st.text_area(

            "Professional Resume",

            value=st.session_state.rewritten_resume,

            height=600

        )

        resume_pdf = generate_rewritten_resume_pdf(

            st.session_state.rewritten_resume

        )

        with open(resume_pdf, "rb") as pdf:

            st.download_button(

                label="📄 Download Rewritten Resume (PDF)",

                data=pdf,

                file_name=resume_pdf,

                mime="application/pdf",

                use_container_width=True

            )
                # ==========================================
    # LinkedIn Summary Generator
    # ==========================================

    st.divider()

    st.subheader("💼 LinkedIn Summary Generator")

    st.write(
        "Generate a professional LinkedIn About section."
    )

    if st.button(
        "💼 Generate LinkedIn Summary",
        use_container_width=True
    ):

        with st.spinner("Writing LinkedIn Summary..."):

            linkedin_summary = generate_linkedin_summary(

                st.session_state.resume_text,

                st.session_state.job_title

            )

        st.session_state.linkedin_summary = linkedin_summary

    if st.session_state.linkedin_summary:

        st.success("LinkedIn Summary Generated!")

        st.text_area(

            "LinkedIn About",

            value=st.session_state.linkedin_summary,

            height=300

        )

    # ==========================================
    # AI Career Advisor
    # ==========================================

    st.divider()

    st.subheader("💼 AI Career Advisor")

    if st.button(
        "💼 Generate Career Advice",
        use_container_width=True
    ):

        with st.spinner("Analyzing your career..."):

            st.session_state.career = generate_career_advice(

                st.session_state.resume_text,

                st.session_state.job_title,

                st.session_state.job_description

            )

    if "career" in st.session_state:

        career = st.session_state.career

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Career Level",

                career["career_level"]

            )

        with col2:

            st.metric(

                "Next Role",

                career["next_role"]

            )

        st.divider()

        left, right = st.columns(2)

        with left:

            st.subheader("📚 Skills To Learn")

            for skill in career["skills_to_learn"]:

                st.success(skill)

        with right:

            st.subheader("🏆 Certifications")

            for cert in career["recommended_certifications"]:

                st.info(cert)

        st.divider()

        st.subheader("🛣 Learning Roadmap")

        for step in career["learning_roadmap"]:

            st.write(f"✅ {step}")

        st.divider()

        st.subheader("💡 Career Advice")

        st.success(

            career["career_advice"]

        )

    # ==========================================
    # AI Resume Chat
    # ==========================================

    st.divider()

    st.subheader("🤖 Ask AI About Your Resume")

    question = st.text_input(
        "Ask anything about your resume..."
    )

    if st.button(
        "🤖 Ask AI",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "Please enter your question."
            )

        else:

            with st.spinner("Thinking..."):

                answer = ask_resume_ai(

                    st.session_state.resume_text,

                    st.session_state.job_title,

                    st.session_state.job_description,

                    question

                )

            st.session_state.ai_answer = answer

    if st.session_state.ai_answer:

        st.success("AI Answer")

        st.write(

            st.session_state.ai_answer

        )

    # ==========================================
    # Analysis History
    # ==========================================

    st.divider()

    st.subheader("📂 Analysis History")

    history = load_history()

    if history:

        for item in reversed(history):

            with st.expander(

                f"💼 {item['job']} | ATS {item['ats']}",

                expanded=False

            ):

                st.write(

                    f"**Resume Score:** {item['resume']}"

                )

                st.write(

                    f"**Hiring Decision:** {item['decision']}"

                )

    else:

        st.info(

            "No previous analyses found."

        )

    # ==========================================
    # Start New Analysis
    # ==========================================

    st.divider()

    if st.button(

        "🗑 Start New Analysis",

        use_container_width=True

    ):

        reset_analysis()

        st.rerun()


# ==========================================
# Footer
# ==========================================

render_footer()