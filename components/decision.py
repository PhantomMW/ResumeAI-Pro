import streamlit as st


# ==========================================
# Hiring Decision
# ==========================================

def render_decision(result):

    decision = result.get(
        "hiring_decision",
        "Not Available"
    )

    reason = result.get(
        "hiring_reason",
        "No explanation available."
    )

    # ======================================
    # Decision Style
    # ======================================

    if decision == "Highly Recommended":

        icon = "🟢"
        color = "success"
        title = "Excellent Candidate"

    elif decision == "Recommended":

        icon = "🟡"
        color = "warning"
        title = "Good Candidate"

    elif decision == "Consider":

        icon = "🟠"
        color = "warning"
        title = "Needs Improvement"

    else:

        icon = "🔴"
        color = "error"
        title = "Not Recommended"

    # ======================================
    # UI
    # ======================================

    st.header("🎯 AI Hiring Decision")

    with st.container(border=True):

        st.subheader(title)

        if color == "success":

            st.success(
                f"{icon} **{decision}**"
            )

        elif color == "warning":

            st.warning(
                f"{icon} **{decision}**"
            )

        else:

            st.error(
                f"{icon} **{decision}**"
            )

        st.markdown("### 🤖 AI Explanation")

        st.write(reason)

    st.divider()