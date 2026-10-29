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
from utils import clean_text, render_html
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
# Session State Initialization
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
# Reset Analysis Helper
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
# Page Bootstrap
# ==========================================

configure_page()
render_sidebar()
render_header()

# ==========================================
# Upload & Trigger Section
# ==========================================

uploaded_file, job_title, job_description, analyze = upload_section()

if analyze:
    if uploaded_file is None:
        st.error("⚠️ Please upload your resume (PDF or DOCX) to begin analysis.")
        st.stop()

    if not job_title.strip():
        st.error("⚠️ Please specify the target job title.")
        st.stop()

    resume_text = extract_resume_text(uploaded_file)
    resume_text = clean_text(resume_text)

    if not resume_text:
        st.error("⚠️ Unable to extract readable text from the uploaded document. Please check the file formatting.")
        st.stop()

    # Futuristic Animated Loading Experience
    progress_bar = st.progress(0)
    status_box = st.empty()

    steps = [
        ("📄 Parsing resume structure & typography...", 15),
        ("🧹 Sanitizing and tokenizing document contents...", 35),
        ("🧠 Initializing Gemini AI reasoning engine...", 55),
        ("🎯 Evaluating ATS criteria & keyword cross-referencing...", 75),
        ("📊 Synthesizing multi-dimensional report...", 90),
    ]

    for msg, p in steps:
        with status_box:
            render_html(
                f"""
                <div style="padding: 12px 18px; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.35); border-radius: 14px; color: #C7D2FE; font-weight: 600; font-size: 14px; margin-bottom: 12px; display: flex; align-items: center; gap: 10px;">
                    <span class="beacon-dot"></span>
                    <span>{msg}</span>
                </div>
                """
            )
        progress_bar.progress(p)
        time.sleep(0.3)

    result = analyze_resume(
        resume_text=resume_text,
        job_title=job_title,
        job_description=job_description
    )

    progress_bar.progress(100)
    with status_box:
        render_html(
            """
            <div style="padding: 12px 18px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 14px; color: #34D399; font-weight: 700; font-size: 14px; margin-bottom: 12px;">
                ✅ Deep Analysis Successfully Generated!
            </div>
            """
        )
    time.sleep(0.6)

    progress_bar.empty()
    status_box.empty()

    # Save to session
    st.session_state.result = result
    st.session_state.resume_text = resume_text
    st.session_state.job_title = job_title
    st.session_state.job_description = job_description

    # Save to history vault
    save_analysis(job_title, result)


# ==========================================
# Results & AI Career Acceleration Suite
# ==========================================

if st.session_state.result is not None:
    # Render Main Analytics Dashboard
    render_results(
        result=st.session_state.result,
        job_title=st.session_state.job_title
    )

    render_html("<div style='height: 20px;'></div>")

    # Suite Header Banner
    render_html(
        """
        <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9)); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 20px; padding: 20px 26px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4); margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
            <div>
                <div style="display: inline-flex; align-items: center; gap: 6px; padding: 2px 10px; background: rgba(139, 92, 246, 0.18); border-radius: 999px; font-size: 11px; font-weight: 700; color: #C084FC;">
                    ⚡ AI GENERATION HUB
                </div>
                <h3 style="margin: 6px 0 2px 0; font-size: 22px; font-weight: 800; color: #FFFFFF;" class="gradient-title">
                    AI Career Acceleration Tools
                </h3>
                <div style="font-size: 12.5px; color: #94A3B8;">Generate custom tailored assets, roadmap your next move, or chat live with your resume AI</div>
            </div>
        </div>
        """
    )

    tab_report, tab_cover, tab_rewrite, tab_linkedin, tab_career, tab_chat, tab_history = st.tabs([
        "📑 PDF Report",
        "💌 Cover Letter",
        "✨ AI Rewriter",
        "💼 LinkedIn Optimizer",
        "🛣️ Career Roadmap",
        "🤖 AI Copilot Chat",
        "📂 History Vault"
    ])

    # ------------------------------------------
    # Tab 1: Executive PDF Report
    # ------------------------------------------
    with tab_report:
        render_html(
            """
            <div style="padding: 10px 0 15px 0;">
                <h4 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700; color: #FFFFFF;">📑 Download Formal Executive Audit Report</h4>
                <p style="margin: 0; font-size: 13.5px; color: #94A3B8 !important;">Get a beautifully structured, presentation-ready PDF containing all scorecards, charts, and recommendations.</p>
            </div>
            """
        )

        pdf_file = generate_pdf(
            st.session_state.result,
            st.session_state.job_title
        )

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📥 Download Executive PDF Audit Report",
                data=file,
                file_name=pdf_file,
                mime="application/pdf",
                use_container_width=True
            )

    # ------------------------------------------
    # Tab 2: AI Cover Letter
    # ------------------------------------------
    with tab_cover:
        render_html(
            """
            <div style="padding: 10px 0 15px 0;">
                <h4 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700; color: #FFFFFF;">💌 Tailored High-Impact Cover Letter</h4>
                <p style="margin: 0; font-size: 13.5px; color: #94A3B8 !important;">Synthesize an articulate cover letter highlighting your exact matched strengths for this role.</p>
            </div>
            """
        )

        if st.button("✨ Generate Custom Cover Letter Now", type="primary", use_container_width=True):
            with st.spinner("Writing personalized cover letter with Gemini AI..."):
                cover_letter = generate_cover_letter(
                    st.session_state.resume_text,
                    st.session_state.job_title,
                    st.session_state.job_description
                )
            st.session_state.cover_letter = cover_letter

        if st.session_state.cover_letter:
            render_html("<div style='height: 10px;'></div>")
            st.text_area(
                "Generated Cover Letter",
                value=st.session_state.cover_letter,
                height=450
            )

            cover_pdf = generate_cover_letter_pdf(st.session_state.cover_letter)
            with open(cover_pdf, "rb") as pdf:
                st.download_button(
                    label="📥 Download Cover Letter as PDF",
                    data=pdf,
                    file_name=cover_pdf,
                    mime="application/pdf",
                    use_container_width=True
                )

    # ------------------------------------------
    # Tab 3: Resume Rewriter
    # ------------------------------------------
    with tab_rewrite:
        render_html(
            """
            <div style="padding: 10px 0 15px 0;">
                <h4 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700; color: #FFFFFF;">✨ Full ATS Optimization Rewrite</h4>
                <p style="margin: 0; font-size: 13.5px; color: #94A3B8 !important;">Re-engineer your resume with strong action verbs, quantifiable metrics, and optimal keyword density.</p>
            </div>
            """
        )

        if st.button("🚀 Rewrite & Optimize Entire Resume", type="primary", use_container_width=True):
            with st.spinner("Restructuring resume for maximum ATS pass-rate..."):
                rewritten_resume = rewrite_resume(
                    st.session_state.resume_text,
                    st.session_state.job_title,
                    st.session_state.job_description
                )
            st.session_state.rewritten_resume = rewritten_resume

        if st.session_state.rewritten_resume:
            render_html("<div style='height: 10px;'></div>")
            st.text_area(
                "ATS Optimized Resume",
                value=st.session_state.rewritten_resume,
                height=550
            )

            resume_pdf = generate_rewritten_resume_pdf(st.session_state.rewritten_resume)
            with open(resume_pdf, "rb") as pdf:
                st.download_button(
                    label="📥 Download Rewritten Resume as PDF",
                    data=pdf,
                    file_name=resume_pdf,
                    mime="application/pdf",
                    use_container_width=True
                )

    # ------------------------------------------
    # Tab 4: LinkedIn Optimizer
    # ------------------------------------------
    with tab_linkedin:
        render_html(
            """
            <div style="padding: 10px 0 15px 0;">
                <h4 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700; color: #FFFFFF;">💼 High-Engagement LinkedIn About Section</h4>
                <p style="margin: 0; font-size: 13.5px; color: #94A3B8 !important;">Generate a persuasive, story-driven personal branding summary crafted for recruiters.</p>
            </div>
            """
        )

        if st.button("💫 Generate LinkedIn Summary", type="primary", use_container_width=True):
            with st.spinner("Crafting personal branding narrative..."):
                linkedin_summary = generate_linkedin_summary(
                    st.session_state.resume_text,
                    st.session_state.job_title
                )
            st.session_state.linkedin_summary = linkedin_summary

        if st.session_state.linkedin_summary:
            render_html("<div style='height: 10px;'></div>")
            st.text_area(
                "LinkedIn About Summary",
                value=st.session_state.linkedin_summary,
                height=320
            )

    # ------------------------------------------
    # Tab 5: AI Career Roadmap
    # ------------------------------------------
    with tab_career:
        render_html(
            """
            <div style="padding: 10px 0 15px 0;">
                <h4 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700; color: #FFFFFF;">🛣️ Personalized Career Trajectory Roadmap</h4>
                <p style="margin: 0; font-size: 13.5px; color: #94A3B8 !important;">Strategic guidance on your seniority progression, next job targets, and certifications.</p>
            </div>
            """
        )

        if st.button("🧭 Generate Strategic Career Roadmap", type="primary", use_container_width=True):
            with st.spinner("Mapping career trajectory..."):
                st.session_state.career = generate_career_advice(
                    st.session_state.resume_text,
                    st.session_state.job_title,
                    st.session_state.job_description
                )

        if "career" in st.session_state:
            career = st.session_state.career
            render_html("<div style='height: 15px;'></div>")

            col1, col2 = st.columns(2)
            with col1:
                render_html(
                    f"""
                    <div style="background: rgba(20, 27, 45, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-top: 3px solid #6366F1; border-radius: 16px; padding: 18px;">
                        <div style="font-size: 11px; font-weight: 700; color: #818CF8; text-transform: uppercase;">Current Standing</div>
                        <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit'; margin-top: 4px;">{career.get('career_level', 'Professional')}</div>
                    </div>
                    """
                )
            with col2:
                render_html(
                    f"""
                    <div style="background: rgba(20, 27, 45, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-top: 3px solid #06B6D4; border-radius: 16px; padding: 18px;">
                        <div style="font-size: 11px; font-weight: 700; color: #22D3EE; text-transform: uppercase;">Next Recommended Milestone</div>
                        <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit'; margin-top: 4px;">{career.get('next_role', 'Lead Role')}</div>
                    </div>
                    """
                )

            render_html("<div style='height: 15px;'></div>")

            col_s1, col_s2 = st.columns(2)
            with col_s1:
                st.markdown("#### 📚 Recommended Skills to Master")
                for skill in career.get("skills_to_learn", []):
                    render_html(
                        f"""
                        <div style="padding: 8px 14px; background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.25); border-radius: 10px; margin-bottom: 6px; font-size: 13.5px; font-weight: 600; color: #C7D2FE;">
                            ⚡ {skill}
                        </div>
                        """
                    )

            with col_s2:
                st.markdown("#### 🏆 High-Impact Certifications")
                for cert in career.get("recommended_certifications", []):
                    render_html(
                        f"""
                        <div style="padding: 8px 14px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 10px; margin-bottom: 6px; font-size: 13.5px; font-weight: 600; color: #6EE7B7;">
                            📜 {cert}
                        </div>
                        """
                    )

            st.markdown("#### 🗺️ Strategic Step-by-Step Roadmap")
            for idx, step in enumerate(career.get("learning_roadmap", []), start=1):
                render_html(
                    f"""
                    <div style="padding: 10px 16px; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; margin-bottom: 6px; font-size: 14px; color: #E2E8F0; display: flex; align-items: center; gap: 10px;">
                        <span style="width: 24px; height: 24px; border-radius: 50%; background: #6366F1; color: #FFF; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 800;">{idx}</span>
                        <span>{step}</span>
                    </div>
                    """
                )

            st.markdown("#### 💡 Career Advisor Insight")
            st.info(career.get("career_advice", "Keep pushing forward!"))

    # ------------------------------------------
    # Tab 6: Resume AI Chat Copilot
    # ------------------------------------------
    with tab_chat:
        render_html(
            """
            <div style="padding: 10px 0 15px 0;">
                <h4 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700; color: #FFFFFF;">🤖 Interactive Resume AI Copilot</h4>
                <p style="margin: 0; font-size: 13.5px; color: #94A3B8 !important;">Ask any specific question about your resume, potential interview traps, or how to frame accomplishments.</p>
            </div>
            """
        )

        question = st.text_input(
            "Ask a tailored question about your profile...",
            placeholder="e.g. How can I better highlight my leadership experience in the summary?"
        )

        if st.button("💬 Ask Resume AI Copilot", type="primary", use_container_width=True):
            if not question.strip():
                st.warning("Please type a question before submitting.")
            else:
                with st.spinner("Consulting AI Copilot..."):
                    answer = ask_resume_ai(
                        st.session_state.resume_text,
                        st.session_state.job_title,
                        st.session_state.job_description,
                        question
                    )
                st.session_state.ai_answer = answer

        if st.session_state.ai_answer:
            render_html("<div style='height: 12px;'></div>")
            render_html(
                f"""
                <div style="background: linear-gradient(135deg, rgba(20, 27, 45, 0.85), rgba(15, 23, 42, 0.9)); border: 1px solid rgba(99, 102, 241, 0.35); border-radius: 18px; padding: 22px; box-shadow: 0 8px 30px rgba(0,0,0,0.35);">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
                        <span style="font-size: 20px;">🤖</span>
                        <span style="font-size: 16px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit';">AI Copilot Answer</span>
                    </div>
                    <div style="font-size: 14.5px; line-height: 1.7; color: #E2E8F0;">
                        {st.session_state.ai_answer}
                    </div>
                </div>
                """
            )

    # ------------------------------------------
    # Tab 7: Historical Analysis Vault
    # ------------------------------------------
    with tab_history:
        render_html(
            """
            <div style="padding: 10px 0 15px 0;">
                <h4 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700; color: #FFFFFF;">📂 Historical Analysis Vault</h4>
                <p style="margin: 0; font-size: 13.5px; color: #94A3B8 !important;">Review past resume evaluations and tracking performance over time.</p>
            </div>
            """
        )

        history = load_history()
        if history:
            for item in reversed(history):
                with st.expander(f"💼 {item.get('job', 'Position')} • ATS: {item.get('ats', 0)}% • Resume: {item.get('resume', 0)}%"):
                    st.markdown(
                        f"""
                        - 🎯 **ATS Score:** {item.get('ats', 0)}%
                        - 📄 **Resume Quality:** {item.get('resume', 0)}%
                        - 🏆 **Hiring Decision:** {item.get('decision', 'N/A')}
                        """
                    )
        else:
            st.info("No saved audit records found in your vault yet.")

    # ==========================================
    # Reset & New Analysis Button
    # ==========================================
    render_html("<div style='height: 25px;'></div>")
    if st.button("🔄 Start New Resume Audit", use_container_width=True):
        reset_analysis()
        st.rerun()

# ==========================================
# Footer
# ==========================================

render_footer()
