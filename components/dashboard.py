import streamlit as st


# ==========================================
# Dashboard
# ==========================================

def render_dashboard(result):

    st.subheader("📋 Professional Overview")

    st.caption(
        "Executive summary of your resume and career profile."
    )

    st.divider()

    # ======================================
    # Career Information
    # ======================================

    career_level = result.get(
        "career_level",
        "Not Available"
    )

    industry = result.get(
        "industry_fit",
        "Not Available"
    )

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.markdown("### 💼 Career Level")

            st.metric(
                "",
                career_level
            )

    with right:

        with st.container(border=True):

            st.markdown("### 🏭 Industry Fit")

            st.metric(
                "",
                industry
            )

    st.divider()

    # ======================================
    # Professional Summary
    # ======================================

    summary = result.get(
        "summary",
        "No summary available."
    )

    with st.container(border=True):

        st.subheader("📝 Professional Summary")

        st.write(summary)

    st.divider()

    # ======================================
    # Overall Recommendation
    # ======================================

    recommendation = result.get(
        "overall_recommendation",
        "No recommendation available."
    )

    with st.container(border=True):

        st.subheader("⭐ Overall Recommendation")

        st.success(recommendation)

    st.divider()