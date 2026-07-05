import streamlit as st


def render_reviews(result):

    st.header("📑 Resume Sections Review")

    # =====================================
    # Experience
    # =====================================

    with st.expander(
        "💼 Experience Review",
        expanded=True
    ):

        st.write(
            result.get(
                "experience_review",
                "Not Available"
            )
        )

    # =====================================
    # Education
    # =====================================

    with st.expander(
        "🎓 Education Review"
    ):

        st.write(
            result.get(
                "education_review",
                "Not Available"
            )
        )

    # =====================================
    # Projects
    # =====================================

    with st.expander(
        "📂 Projects Review"
    ):

        st.write(
            result.get(
                "projects_review",
                "Not Available"
            )
        )

    # =====================================
    # Certifications
    # =====================================

    with st.expander(
        "📜 Certifications Review"
    ):

        st.write(
            result.get(
                "certifications_review",
                "Not Available"
            )
        )

    st.divider()