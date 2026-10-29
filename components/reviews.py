import streamlit as st
from utils import render_html


def render_reviews(result):
    render_html(
        """
        <div style="margin-bottom: 15px;">
            <h3 style="font-size: 24px; font-weight: 800; margin: 0;" class="gradient-title">📑 Comprehensive Section Audit</h3>
            <p style="font-size: 13px; color: #94A3B8 !important; margin: 0;">In-depth AI feedback tailored to each segment of your CV</p>
        </div>
        """
    )

    sections = [
        ("💼 Professional Experience", "experience_review", True, "#6366F1"),
        ("🎓 Academic & Education", "education_review", False, "#06B6D4"),
        ("📂 Portfolio & Projects", "projects_review", False, "#10B981"),
        ("📜 Certifications & Credentials", "certifications_review", False, "#F59E0B")
    ]

    for title, key, default_open, accent_color in sections:
        review_text = result.get(key, "No feedback available.")
        with st.expander(title, expanded=default_open):
            render_html(
                f"""
                <div style="padding: 10px 4px; font-size: 14.5px; line-height: 1.7; color: #E2E8F0;">
                    {review_text}
                </div>
                """
            )

    st.divider()
