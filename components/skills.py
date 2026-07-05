import streamlit as st


# ==========================================
# Helper
# ==========================================

def render_skill_list(skills, empty_message, icon):

    if skills:

        for skill in skills:
            st.markdown(f"- {icon} **{skill}**")

    else:

        st.caption(empty_message)


# ==========================================
# Skills Analysis
# ==========================================

def render_skills(result):

    st.header("🧠 Skills Analysis")

    st.caption(
        "Comparison between the detected skills in your resume and the target job requirements."
    )

    hard_skills = result.get("hard_skills", [])
    soft_skills = result.get("soft_skills", [])
    matched_skills = result.get("matched_skills", [])
    missing_skills = result.get("missing_skills", [])

    # =====================================================
    # Hard & Soft Skills
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader(f"💻 Hard Skills ({len(hard_skills)})")

            render_skill_list(
                hard_skills,
                "No hard skills detected.",
                "✅"
            )

    with col2:

        with st.container(border=True):

            st.subheader(f"🤝 Soft Skills ({len(soft_skills)})")

            render_skill_list(
                soft_skills,
                "No soft skills detected.",
                "🔹"
            )

    st.divider()

    # =====================================================
    # Matched & Missing Skills
    # =====================================================

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader(f"🎯 Matched Skills ({len(matched_skills)})")

            render_skill_list(
                matched_skills,
                "No matched skills found.",
                "🟢"
            )

    with right:

        with st.container(border=True):

            st.subheader(f"⚠ Missing Skills ({len(missing_skills)})")

            if missing_skills:

                for skill in missing_skills:
                    st.markdown(f"- 🔴 **{skill}**")

            else:

                st.success(
                    "Excellent! No missing skills detected."
                )

    st.divider()

    # =====================================================
    # Skills Summary
    # =====================================================

    total_detected = len(hard_skills) + len(soft_skills)

    col3, col4, col5 = st.columns(3)

    col3.metric("Detected Skills", total_detected)
    col4.metric("Matched Skills", len(matched_skills))
    col5.metric("Missing Skills", len(missing_skills))