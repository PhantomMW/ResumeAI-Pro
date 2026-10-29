import streamlit as st
from utils import render_html


def render_interview(result):
    render_html(
        """
        <div style="margin-bottom: 15px;">
            <h3 style="font-size: 24px; font-weight: 800; margin: 0;" class="gradient-title">🎤 Targeted AI Interview Simulator</h3>
            <p style="font-size: 13px; color: #94A3B8 !important; margin: 0;">Predicted high-probability interview questions based on your resume and target role</p>
        </div>
        """
    )

    questions = result.get("interview_questions", [])

    if not questions:
        st.info("No interview questions were generated for this profile.")
        return

    for index, question in enumerate(questions, start=1):
        with st.expander(f"🎯 Scenario / Question #{index}", expanded=(index == 1)):
            render_html(
                f"""
                <div style="padding: 12px 6px; font-size: 15px; font-weight: 500; line-height: 1.7; color: #F1F5F9;">
                    {question}
                </div>
                """
            )

    st.divider()
