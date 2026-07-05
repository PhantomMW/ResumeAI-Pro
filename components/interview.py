import streamlit as st


def render_interview(result):

    st.header("🎤 AI Interview Questions")

    questions = result.get(
        "interview_questions",
        []
    )

    if not questions:

        st.warning(
            "No interview questions available."
        )

        return

    for index, question in enumerate(
        questions,
        start=1
    ):

        with st.expander(
            f"Question {index}",
            expanded=(index == 1)
        ):

            st.write(question)

    st.divider()