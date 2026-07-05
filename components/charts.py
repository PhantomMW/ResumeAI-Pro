import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


def render_charts(result):

    st.header("📊 Resume Analytics Dashboard")

    st.caption(
        "Interactive visualization of your resume performance."
    )

    # =====================================================
    # Scores
    # =====================================================

    resume = result.get("resume_score", 0)
    ats = result.get("ats_score", 0)
    job = result.get("job_match", 0)
    grammar = result.get("grammar_score", 0)
    formatting = result.get("formatting_score", 0)
    keywords = result.get("keyword_score", 0)

    categories = [
        "Resume",
        "ATS",
        "Job Match",
        "Grammar",
        "Formatting",
        "Keywords"
    ]

    values = [
        resume,
        ats,
        job,
        grammar,
        formatting,
        keywords
    ]

    # =====================================================
    # First Row
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(

            x=categories,

            y=values,

            text=values,

            title="Performance Scores"

        )

        fig.update_layout(

            yaxis=dict(range=[0,100]),

            template="plotly_white",

            height=430

        )

        fig.update_traces(

            textposition="outside",

            hovertemplate="<b>%{x}</b><br>Score: %{y}%<extra></extra>"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        radar = go.Figure()

        radar.add_trace(

            go.Scatterpolar(

                r=values,

                theta=categories,

                fill="toself",

                name="Resume"

            )

        )

        radar.update_layout(

            template="plotly_white",

            polar=dict(

                radialaxis=dict(

                    visible=True,

                    range=[0,100]

                )

            ),

            title="Overall Performance",

            height=430

        )

        st.plotly_chart(

            radar,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # Second Row
    # =====================================================

    hard = len(result.get("hard_skills", []))
    soft = len(result.get("soft_skills", []))
    missing = len(result.get("missing_skills", []))

    col3, col4 = st.columns(2)

    with col3:

        pie = px.pie(

            names=[
                "Hard Skills",
                "Soft Skills",
                "Missing Skills"
            ],

            values=[
                hard,
                soft,
                missing
            ],

            hole=0.45,

            title="Skills Distribution"

        )

        pie.update_layout(

            template="plotly_white",

            height=430

        )

        st.plotly_chart(

            pie,

            use_container_width=True

        )

    with col4:

        gauge = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=ats,

                title={"text":"ATS Score"},

                gauge={

                    "axis":{"range":[0,100]},

                    "bar":{"thickness":0.35},

                    "steps":[

                        {"range":[0,50],"color":"#ffcccc"},

                        {"range":[50,70],"color":"#ffe599"},

                        {"range":[70,85],"color":"#b6d7a8"},

                        {"range":[85,100],"color":"#93c47d"}

                    ]

                }

            )

        )

        gauge.update_layout(

            template="plotly_white",

            height=430

        )

        st.plotly_chart(

            gauge,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # ATS Breakdown
    # =====================================================

    breakdown = go.Figure()

    breakdown.add_trace(

        go.Bar(

            x=[

                "Grammar",

                "Formatting",

                "Keywords"

            ],

            y=[

                grammar,

                formatting,

                keywords

            ],

            text=[

                grammar,

                formatting,

                keywords

            ],

            textposition="outside"

        )

    )

    breakdown.update_layout(

        title="ATS Breakdown",

        template="plotly_white",

        yaxis=dict(range=[0,100]),

        height=430

    )

    st.plotly_chart(

        breakdown,

        use_container_width=True

    )

    st.divider()