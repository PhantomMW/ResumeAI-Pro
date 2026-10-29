import streamlit as st
from utils import render_html


# ==========================================
# Helpers & Color Gradients
# ==========================================

METRIC_THEMES = {
    "resume": {
        "color": "#818CF8",
        "bg_gradient": "linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.08))",
        "border_glow": "rgba(99, 102, 241, 0.8)",
        "icon": "📄"
    },
    "ats": {
        "color": "#06B6D4",
        "bg_gradient": "linear-gradient(135deg, rgba(6, 182, 212, 0.2), rgba(14, 165, 233, 0.08))",
        "border_glow": "rgba(6, 182, 212, 0.8)",
        "icon": "🎯"
    },
    "match": {
        "color": "#10B981",
        "bg_gradient": "linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.08))",
        "border_glow": "rgba(16, 185, 129, 0.8)",
        "icon": "🤝"
    },
    "grammar": {
        "color": "#F59E0B",
        "bg_gradient": "linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(217, 119, 6, 0.08))",
        "border_glow": "rgba(245, 158, 11, 0.8)",
        "icon": "✍️"
    },
    "formatting": {
        "color": "#EC4899",
        "bg_gradient": "linear-gradient(135deg, rgba(236, 72, 153, 0.2), rgba(219, 39, 119, 0.08))",
        "border_glow": "rgba(236, 72, 153, 0.8)",
        "icon": "📐"
    },
    "keywords": {
        "color": "#A855F7",
        "bg_gradient": "linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(147, 51, 234, 0.08))",
        "border_glow": "rgba(168, 85, 247, 0.8)",
        "icon": "🔑"
    }
}


def get_status_badge(score):
    if score >= 85:
        return '<span style="color: #34D399; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700;">🟢 EXCELLENT</span>'
    elif score >= 70:
        return '<span style="color: #60A5FA; background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700;">🔵 GOOD</span>'
    elif score >= 50:
        return '<span style="color: #FBBF24; background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.3); padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700;">🟠 FAIR</span>'
    return '<span style="color: #F87171; background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.3); padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700;">🔴 NEEDS WORK</span>'


def render_luxury_card(theme_key, title, score):
    theme = METRIC_THEMES.get(theme_key, METRIC_THEMES["resume"])
    status_html = get_status_badge(score)
    
    render_html(
        f"""
        <div style="background: linear-gradient(145deg, rgba(20, 27, 45, 0.85), rgba(15, 23, 42, 0.7)); border: 1px solid rgba(255, 255, 255, 0.08); border-top: 3px solid {theme['border_glow']}; border-radius: 20px; padding: 22px 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35); transition: all 0.3s ease; position: relative; overflow: hidden; height: 100%;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span style="font-size: 13px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em;">{theme['icon']} {title}</span>
                {status_html}
            </div>
            
            <div style="font-family: 'Outfit', sans-serif; font-size: 2.6rem; font-weight: 900; color: #FFFFFF; line-height: 1; margin: 10px 0 14px 0;">
                {score}<span style="font-size: 1.4rem; color: {theme['color']}; margin-left: 2px;">%</span>
            </div>
            
            <div style="width: 100%; height: 7px; background: rgba(255, 255, 255, 0.08); border-radius: 999px; overflow: hidden;">
                <div style="width: {score}%; height: 100%; background: linear-gradient(90deg, {theme['color']}, #FFFFFF); border-radius: 999px; box-shadow: 0 0 12px {theme['color']}; transition: width 1s ease;"></div>
            </div>
        </div>
        """
    )


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

    render_html(
        """
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px;">
            <div>
                <h3 style="font-size: 24px; font-weight: 800; margin: 0;" class="gradient-title">📊 Performance Analytics Dashboard</h3>
                <p style="font-size: 13px; color: #94A3B8 !important; margin: 0;">Comprehensive 6-vector analysis audited by Gemini AI</p>
            </div>
        </div>
        """
    )

    # Main Metrics (Top Row)
    col1, col2, col3 = st.columns(3)

    with col1:
        render_luxury_card("resume", "Resume Score", resume)

    with col2:
        render_luxury_card("ats", "ATS Compatibility", ats)

    with col3:
        render_luxury_card("match", "Job Match", match)

    render_html("<div style='height: 16px;'></div>")

    # Detailed Metrics (Bottom Row)
    col4, col5, col6 = st.columns(3)

    with col4:
        render_luxury_card("grammar", "Grammar & Tone", grammar)

    with col5:
        render_luxury_card("formatting", "Structure & Format", formatting)

    with col6:
        render_luxury_card("keywords", "Keyword Density", keywords)

    st.divider()

    # Overall Aggregate Score Banner
    overall = round((ats + resume + match + grammar + formatting + keywords) / 6)

    render_html(
        f"""
        <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9)); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 20px; padding: 22px 26px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="width: 75px; height: 75px; border-radius: 50%; background: linear-gradient(135deg, #6366F1, #EC4899); display: flex; align-items: center; justify-content: center; font-family: 'Outfit', sans-serif; font-size: 26px; font-weight: 900; color: #FFFFFF; box-shadow: 0 0 25px rgba(99, 102, 241, 0.5);">
                    {overall}%
                </div>
                <div>
                    <div style="font-size: 18px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">🏆 Overall Aggregate Benchmark</div>
                    <div style="font-size: 13px; color: #94A3B8; margin-top: 3px;">Weighted average across all six AI evaluation dimensions</div>
                </div>
            </div>
            
            <div style="flex: 1; min-width: 250px; max-width: 450px;">
                <div style="display: flex; justify-content: space-between; font-size: 12px; color: #94A3B8; margin-bottom: 6px; font-weight: 600;">
                    <span>Overall Strength</span>
                    <span>{overall} / 100</span>
                </div>
                <div style="width: 100%; height: 9px; background: rgba(255, 255, 255, 0.08); border-radius: 999px; overflow: hidden;">
                    <div style="width: {overall}%; height: 100%; background: linear-gradient(90deg, #6366F1, #8B5CF6, #06B6D4); border-radius: 999px; box-shadow: 0 0 15px rgba(99, 102, 241, 0.6);"></div>
                </div>
            </div>
        </div>
        """
    )
