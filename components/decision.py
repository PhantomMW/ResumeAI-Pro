import streamlit as st
from utils import render_html


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

    # Style mapping
    if decision == "Highly Recommended":
        badge_bg = "rgba(16, 185, 129, 0.15)"
        badge_border = "#10B981"
        badge_text = "#34D399"
        icon = "🏆"
        title = "Top-Tier Candidate • Highly Recommended"
        glow_color = "rgba(16, 185, 129, 0.4)"
    elif decision == "Recommended":
        badge_bg = "rgba(59, 130, 246, 0.15)"
        badge_border = "#3B82F6"
        badge_text = "#60A5FA"
        icon = "⭐"
        title = "Strong Candidate • Recommended"
        glow_color = "rgba(59, 130, 246, 0.4)"
    elif decision == "Consider":
        badge_bg = "rgba(245, 158, 11, 0.15)"
        badge_border = "#F59E0B"
        badge_text = "#FBBF24"
        icon = "⚡"
        title = "Potential Candidate • Further Review Required"
        glow_color = "rgba(245, 158, 11, 0.4)"
    else:
        badge_bg = "rgba(239, 68, 68, 0.15)"
        badge_border = "#EF4444"
        badge_text = "#F87171"
        icon = "⚠️"
        title = "Needs Strategic Revision • Not Recommended Yet"
        glow_color = "rgba(239, 68, 68, 0.4)"

    render_html(
        f"""
        <div style="background: linear-gradient(135deg, rgba(20, 27, 45, 0.85), rgba(15, 23, 42, 0.75)); border: 1px solid rgba(255, 255, 255, 0.08); border-left: 5px solid {badge_border}; border-radius: 20px; padding: 26px; box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4), 0 0 25px {glow_color}; position: relative; overflow: hidden;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 28px;">{icon}</span>
                    <div>
                        <h4 style="margin: 0; font-size: 19px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">{title}</h4>
                        <div style="font-size: 12px; color: #94A3B8;">Autonomous AI Hiring Simulation Verdict</div>
                    </div>
                </div>
                
                <div style="background: {badge_bg}; border: 1px solid {badge_border}; color: {badge_text}; padding: 6px 18px; border-radius: 999px; font-weight: 800; font-size: 13.5px; letter-spacing: 0.05em; text-transform: uppercase;">
                    {decision}
                </div>
            </div>
            
            <div style="background: rgba(0, 0, 0, 0.25); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 14px; padding: 18px; margin-top: 10px;">
                <div style="font-size: 12px; font-weight: 700; color: #818CF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">
                    🤖 AI Evaluator Executive Reasoning
                </div>
                <div style="font-size: 14.5px; line-height: 1.65; color: #E2E8F0;">
                    {reason}
                </div>
            </div>
        </div>
        """
    )
