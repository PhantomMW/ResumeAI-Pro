import streamlit as st

from components.metrics import render_metrics
from components.dashboard import render_dashboard
from components.skills import render_skills
from components.reviews import render_reviews
from components.interview import render_interview
from components.charts import render_charts
from components.decision import render_decision


def render_results(result, job_title):

    # ==================================================
    # Header
    # ==================================================

    st.title("📊 Resume Analysis Dashboard")

    st.caption(f"🎯 Target Position: **{job_title}**")

    st.divider()

    # ==================================================
    # Executive Summary
    # ==================================================

    with st.container(border=True):

        st.subheader("🧠 Executive Summary")

        ats = result.get("ats_score", 0)
        resume = result.get("resume_score", 0)
        decision = result.get("hiring_decision", "Unknown")

        st.markdown(
            f"""
Your resume has been successfully analyzed for the **{job_title}** position.

### Summary

- 🎯 **ATS Score:** **{ats}%**
- 📄 **Resume Score:** **{resume}%**
- 💼 **Hiring Decision:** **{decision}**

Review the detailed sections below to discover your strengths, missing skills,
AI recommendations, interview preparation, and professional improvement tips.
"""
        )

    st.divider()

    # ==================================================
    # Key Metrics
    # ==================================================

    st.subheader("📈 Performance Overview")

    render_metrics(result)

    st.divider()

    # ==================================================
    # Hiring Decision
    # ==================================================

    st.subheader("🏆 Hiring Decision")

    render_decision(result)

    st.divider()

    # ==================================================
    # Dashboard Overview
    # ==================================================

    st.subheader("📋 Detailed Analysis")

    render_dashboard(result)

    st.divider()

    # ==================================================
    # Charts
    # ==================================================

    st.subheader("📊 Visual Insights")

    render_charts(result)

    st.divider()

    # ==================================================
    # Skills Analysis
    # ==================================================

    st.subheader("🧠 Skills Analysis")

    render_skills(result)

    st.divider()

    # ==================================================
    # AI Resume Review
    # ==================================================

    st.subheader("💡 AI Resume Review")

    render_reviews(result)

    st.divider()

    # ==================================================
    # Interview Questions
    # ==================================================

    st.subheader("🎤 AI Interview Preparation")

    render_interview(result)

    st.divider()

    st.success("✅ Resume analysis completed successfully.")