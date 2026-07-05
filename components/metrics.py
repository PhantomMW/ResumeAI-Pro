import streamlit as st


# ==========================================
# Helpers
# ==========================================

def get_status(score):

    if score >= 85:
        return "🟢 Excellent"

    elif score >= 70:
        return "🟡 Good"

    elif score >= 50:
        return "🟠 Fair"

    return "🔴 Needs Improvement"


def render_card(title, score):

    st.metric(
        title,
        f"{score}%"
    )

    st.progress(score / 100)

    st.caption(get_status(score))


# ==========================================
# Dashboard Metrics
# ==========================================

def render_metrics(result):

    ats = result.get("ats_score", 0)
    resume = result.get("resume_score", 0)
    match = result.get("job_match", 0)
    grammar = result.get("grammar_score", 0)
    formatting = result.get("formatting_score", 0)
    keywords = result.get("keyword_score", 0)

    st.subheader("📊 Performance Dashboard")

    st.caption(
        "Your resume performance across the most important hiring metrics."
    )

    st.divider()

    # ======================================
    # Main Metrics
    # ======================================

    col1, col2, col3 = st.columns(3)

    with col1:
        render_card(
            "📄 Resume Score",
            resume
        )

    with col2:
        render_card(
            "🎯 ATS Score",
            ats
        )

    with col3:
        render_card(
            "🤝 Job Match",
            match
        )

    st.write("")

    # ======================================
    # Detailed Metrics
    # ======================================

    col4, col5, col6 = st.columns(3)

    with col4:
        render_card(
            "✍ Grammar",
            grammar
        )

    with col5:
        render_card(
            "📝 Formatting",
            formatting
        )

    with col6:
        render_card(
            "🔑 Keywords",
            keywords
        )

    st.divider()

    # ======================================
    # Overall Performance
    # ======================================

    overall = round(
        (
            ats
            + resume
            + match
            + grammar
            + formatting
            + keywords
        ) / 6
    )

    st.subheader("🏆 Overall Resume Performance")

    st.progress(overall / 100)

    left, right = st.columns([1, 3])

    with left:

        st.metric(
            "Overall",
            f"{overall}%"
        )

    with right:

        if overall >= 85:

            st.success(
                "Excellent resume. It is highly competitive for most applications."
            )

        elif overall >= 70:

            st.info(
                "Good resume. A few improvements can significantly increase your chances."
            )

        elif overall >= 50:

            st.warning(
                "Your resume has potential, but several sections should be improved."
            )

        else:

            st.error(
                "Your resume needs major improvements before applying for jobs."
            )