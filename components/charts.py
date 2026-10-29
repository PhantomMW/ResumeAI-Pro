import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


# ==========================================
# Luxury Dark Theme Styling Defaults
# ==========================================

CHART_FONT = dict(family="Plus Jakarta Sans, sans-serif", size=13, color="#CBD5E1")
GRID_COLOR = "rgba(255, 255, 255, 0.08)"


def apply_luxury_layout(fig, title="", height=420):
    fig.update_layout(
        title=dict(
            text=f"<b>{title}</b>",
            font=dict(family="Outfit, sans-serif", size=18, color="#FFFFFF")
        ),
        paper_bgcolor="rgba(15, 23, 42, 0.6)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=CHART_FONT,
        height=height,
        margin=dict(l=30, r=30, t=55, b=30),
        xaxis=dict(
            showgrid=True,
            gridcolor=GRID_COLOR,
            zeroline=False,
            color="#94A3B8"
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=GRID_COLOR,
            zeroline=False,
            color="#94A3B8"
        )
    )
    return fig


def render_charts(result):
    st.markdown(
        """
        <div style="margin-bottom: 15px;">
            <h3 style="font-size: 24px; font-weight: 800; margin: 0;" class="gradient-title">📊 Multi-Dimensional Visual Analytics</h3>
            <p style="font-size: 13px; color: #94A3B8 !important; margin: 0;">High-fidelity interactive graphs of your career vectors</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Scores
    resume = result.get("resume_score", 0)
    ats = result.get("ats_score", 0)
    job = result.get("job_match", 0)
    grammar = result.get("grammar_score", 0)
    formatting = result.get("formatting_score", 0)
    keywords = result.get("keyword_score", 0)

    categories = [
        "Resume Quality",
        "ATS Score",
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

    palette = ["#6366F1", "#06B6D4", "#10B981", "#F59E0B", "#EC4899", "#8B5CF6"]

    # =====================================================
    # Row 1: Bar & Radar
    # =====================================================
    col1, col2 = st.columns(2)

    with col1:
        fig_bar = go.Figure(
            data=[
                go.Bar(
                    x=categories,
                    y=values,
                    text=[f"{v}%" for v in values],
                    textposition="outside",
                    marker=dict(
                        color=palette,
                        line=dict(color="rgba(255, 255, 255, 0.2)", width=1.5),
                        cornerradius=8
                    ),
                    hovertemplate="<b>%{x}</b><br>Score: <b>%{y}%</b><extra></extra>"
                )
            ]
        )
        fig_bar.update_layout(yaxis=dict(range=[0, 115]))
        apply_luxury_layout(fig_bar, "Performance Vector Overview", 430)
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        radar = go.Figure()
        radar.add_trace(
            go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill="toself",
                fillcolor="rgba(99, 102, 241, 0.28)",
                line=dict(color="#818CF8", width=2.5),
                marker=dict(size=7, color="#C7D2FE"),
                name="Performance"
            )
        )
        radar.update_layout(
            paper_bgcolor="rgba(15, 23, 42, 0.6)",
            plot_bgcolor="rgba(0, 0, 0, 0)",
            font=CHART_FONT,
            height=430,
            title=dict(
                text="<b>Holistic Career Radar</b>",
                font=dict(family="Outfit, sans-serif", size=18, color="#FFFFFF")
            ),
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    gridcolor=GRID_COLOR,
                    color="#64748B"
                ),
                angularaxis=dict(
                    gridcolor=GRID_COLOR,
                    color="#CBD5E1"
                )
            )
        )
        st.plotly_chart(radar, use_container_width=True)

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # =====================================================
    # Row 2: Skills Donut & ATS Gauge
    # =====================================================
    hard = len(result.get("hard_skills", []))
    soft = len(result.get("soft_skills", []))
    missing = len(result.get("missing_skills", []))

    col3, col4 = st.columns(2)

    with col3:
        pie = px.pie(
            names=["Hard Skills", "Soft Skills", "Missing Skills"],
            values=[hard, soft, missing],
            hole=0.6,
            color_discrete_sequence=["#06B6D4", "#8B5CF6", "#F43F5E"]
        )
        pie.update_traces(
            textposition="inside",
            textinfo="percent+label",
            marker=dict(line=dict(color="rgba(15, 23, 42, 0.8)", width=3))
        )
        apply_luxury_layout(pie, "Skills Distribution Balance", 430)
        st.plotly_chart(pie, use_container_width=True)

    with col4:
        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=ats,
                number={"suffix": "%", "font": {"family": "Outfit", "size": 48, "color": "#FFFFFF"}},
                title={"text": "<b>ATS Optimization Index</b>", "font": {"family": "Outfit", "size": 18, "color": "#FFFFFF"}},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "#64748B", "tickwidth": 1},
                    "bar": {"color": "#6366F1", "thickness": 0.3},
                    "bgcolor": "rgba(255, 255, 255, 0.05)",
                    "borderwidth": 0,
                    "steps": [
                        {"range": [0, 50], "color": "rgba(239, 68, 68, 0.25)"},
                        {"range": [50, 70], "color": "rgba(245, 158, 11, 0.25)"},
                        {"range": [70, 85], "color": "rgba(59, 130, 246, 0.25)"},
                        {"range": [85, 100], "color": "rgba(16, 185, 129, 0.3)"}
                    ]
                }
            )
        )
        gauge.update_layout(
            paper_bgcolor="rgba(15, 23, 42, 0.6)",
            font=CHART_FONT,
            height=430,
            margin=dict(l=40, r=40, t=60, b=40)
        )
        st.plotly_chart(gauge, use_container_width=True)

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # =====================================================
    # Row 3: ATS Factors Breakdown
    # =====================================================
    breakdown = go.Figure(
        data=[
            go.Bar(
                x=["Grammar & Tone", "Formatting & Layout", "Target Keywords"],
                y=[grammar, formatting, keywords],
                text=[f"{grammar}%", f"{formatting}%", f"{keywords}%"],
                textposition="outside",
                marker=dict(
                    color=["#F59E0B", "#EC4899", "#8B5CF6"],
                    line=dict(color="rgba(255, 255, 255, 0.2)", width=1.5),
                    cornerradius=8
                ),
                hovertemplate="<b>%{x}</b>: %{y}%<extra></extra>"
            )
        ]
    )
    breakdown.update_layout(yaxis=dict(range=[0, 115]))
    apply_luxury_layout(breakdown, "Critical ATS Sub-Factor Breakdown", 380)
    st.plotly_chart(breakdown, use_container_width=True)

    st.divider()
