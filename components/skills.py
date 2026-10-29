import streamlit as st
from utils import render_html


# ==========================================
# Skill Chip Badges Helper
# ==========================================

def render_skill_chips(skills, empty_message, chip_type):
    """
    Renders skills as interactive, glowing modern badges.
    """
    if not skills:
        render_html(
            f"""
            <div style="padding: 14px; background: rgba(255, 255, 255, 0.02); border-radius: 12px; color: #64748B; font-size: 13px; text-align: center;">
                {empty_message}
            </div>
            """
        )
        return

    # Style definitions
    styles = {
        "hard": {
            "bg": "rgba(6, 182, 212, 0.12)",
            "border": "rgba(6, 182, 212, 0.35)",
            "text": "#67E8F9",
            "icon": "⚡"
        },
        "soft": {
            "bg": "rgba(139, 92, 246, 0.12)",
            "border": "rgba(139, 92, 246, 0.35)",
            "text": "#C084FC",
            "icon": "🤝"
        },
        "matched": {
            "bg": "rgba(16, 185, 129, 0.12)",
            "border": "rgba(16, 185, 129, 0.4)",
            "text": "#34D399",
            "icon": "✅"
        },
        "missing": {
            "bg": "rgba(244, 63, 94, 0.12)",
            "border": "rgba(244, 63, 94, 0.4)",
            "text": "#FB7185",
            "icon": "⚠️"
        }
    }

    cfg = styles.get(chip_type, styles["hard"])
    
    chips_html = "".join([
        f"""
        <span style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; margin: 4px; background: {cfg['bg']}; border: 1px solid {cfg['border']}; border-radius: 999px; font-size: 12.5px; font-weight: 600; color: {cfg['text']}; transition: all 0.25s ease; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
            <span style="font-size: 11px;">{cfg['icon']}</span>
            <span>{skill}</span>
        </span>
        """
        for skill in skills
    ])

    render_html(
        f"""
        <div style="display: flex; flex-wrap: wrap; padding: 6px 0;">
            {chips_html}
        </div>
        """
    )


# ==========================================
# Skills Analysis
# ==========================================

def render_skills(result):
    render_html(
        """
        <div style="margin-bottom: 12px;">
            <h3 style="font-size: 24px; font-weight: 800; margin: 0;" class="gradient-title">🧠 Deep Skills Gap Matrix</h3>
            <p style="font-size: 13px; color: #94A3B8 !important; margin: 0;">Cross-examination of your technical competency against target job requirements</p>
        </div>
        """
    )

    hard_skills = result.get("hard_skills", [])
    soft_skills = result.get("soft_skills", [])
    matched_skills = result.get("matched_skills", [])
    missing_skills = result.get("missing_skills", [])

    # =====================================================
    # Hard & Soft Skills Row
    # =====================================================
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            render_html(
                f"""
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <div style="font-size: 16px; font-weight: 800; color: #67E8F9; font-family: 'Outfit', sans-serif;">💻 Hard & Technical Skills</div>
                    <span style="padding: 2px 10px; background: rgba(6, 182, 212, 0.2); border-radius: 999px; font-size: 11px; font-weight: 700; color: #67E8F9;">{len(hard_skills)} Detected</span>
                </div>
                """
            )
            render_skill_chips(
                hard_skills,
                "No technical skills detected in the document.",
                "hard"
            )

    with col2:
        with st.container(border=True):
            render_html(
                f"""
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <div style="font-size: 16px; font-weight: 800; color: #C084FC; font-family: 'Outfit', sans-serif;">🤝 Soft & Leadership Skills</div>
                    <span style="padding: 2px 10px; background: rgba(139, 92, 246, 0.2); border-radius: 999px; font-size: 11px; font-weight: 700; color: #C084FC;">{len(soft_skills)} Detected</span>
                </div>
                """
            )
            render_skill_chips(
                soft_skills,
                "No soft skills detected in the document.",
                "soft"
            )

    render_html("<div style='height: 12px;'></div>")

    # =====================================================
    # Matched & Missing Skills Row
    # =====================================================
    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            render_html(
                f"""
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <div style="font-size: 16px; font-weight: 800; color: #34D399; font-family: 'Outfit', sans-serif;">🎯 Matched Job Qualifications</div>
                    <span style="padding: 2px 10px; background: rgba(16, 185, 129, 0.2); border-radius: 999px; font-size: 11px; font-weight: 700; color: #34D399;">{len(matched_skills)} Verified</span>
                </div>
                """
            )
            render_skill_chips(
                matched_skills,
                "No matched skills found between your resume and the job description.",
                "matched"
            )

    with right:
        with st.container(border=True):
            render_html(
                f"""
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <div style="font-size: 16px; font-weight: 800; color: #FB7185; font-family: 'Outfit', sans-serif;">⚠️ High-Priority Missing Keywords</div>
                    <span style="padding: 2px 10px; background: rgba(244, 63, 94, 0.2); border-radius: 999px; font-size: 11px; font-weight: 700; color: #FB7185;">{len(missing_skills)} Required</span>
                </div>
                """
            )
            if missing_skills:
                render_skill_chips(
                    missing_skills,
                    "",
                    "missing"
                )
            else:
                render_html(
                    """
                    <div style="padding: 14px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; color: #34D399; font-size: 13px; text-align: center; font-weight: 600;">
                        🎉 Outstanding! You cover 100% of all required job skills.
                    </div>
                    """
                )

    st.divider()
