import streamlit as st
from utils import render_html


# ==========================================
# Dashboard: Executive Profile Overview
# ==========================================

def render_dashboard(result):
    render_html(
        """
        <div style="margin-bottom: 15px;">
            <h3 style="font-size: 24px; font-weight: 800; margin: 0;" class="gradient-title">📋 Executive Profile Overview</h3>
            <p style="font-size: 13px; color: #94A3B8 !important; margin: 0;">High-level career classification and strategic industry positioning</p>
        </div>
        """
    )

    career_level = result.get("career_level", "Not Available")
    industry = result.get("industry_fit", "Not Available")

    left, right = st.columns(2)

    with left:
        render_html(
            f"""
            <div style="background: linear-gradient(135deg, rgba(20, 27, 45, 0.8), rgba(15, 23, 42, 0.7)); border: 1px solid rgba(255, 255, 255, 0.08); border-top: 3px solid #6366F1; border-radius: 18px; padding: 22px; box-shadow: 0 10px 25px rgba(0,0,0,0.35);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <span style="font-size: 12px; font-weight: 700; color: #818CF8; text-transform: uppercase; letter-spacing: 0.05em;">Career Seniority</span>
                    <span style="font-size: 20px;">💼</span>
                </div>
                <div style="font-size: 24px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">
                    {career_level}
                </div>
                <div style="font-size: 12px; color: #94A3B8; margin-top: 4px;">Assessed based on depth of impact, tenure, and leadership metrics</div>
            </div>
            """
        )

    with right:
        render_html(
            f"""
            <div style="background: linear-gradient(135deg, rgba(20, 27, 45, 0.8), rgba(15, 23, 42, 0.7)); border: 1px solid rgba(255, 255, 255, 0.08); border-top: 3px solid #06B6D4; border-radius: 18px; padding: 22px; box-shadow: 0 10px 25px rgba(0,0,0,0.35);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <span style="font-size: 12px; font-weight: 700; color: #22D3EE; text-transform: uppercase; letter-spacing: 0.05em;">Industry Alignment</span>
                    <span style="font-size: 20px;">🏭</span>
                </div>
                <div style="font-size: 24px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">
                    {industry}
                </div>
                <div style="font-size: 12px; color: #94A3B8; margin-top: 4px;">Primary sector relevance and market domain compatibility</div>
            </div>
            """
        )

    render_html("<div style='height: 14px;'></div>")

    # Professional Summary Card
    summary = result.get("summary", "No summary available.")

    render_html(
        f"""
        <div style="background: linear-gradient(135deg, rgba(20, 27, 45, 0.8), rgba(15, 23, 42, 0.7)); border: 1px solid rgba(255, 255, 255, 0.08); border-left: 4px solid #8B5CF6; border-radius: 18px; padding: 22px; box-shadow: 0 10px 25px rgba(0,0,0,0.35);">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
                <span style="font-size: 18px;">📝</span>
                <span style="font-size: 16px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">Executive Synopsis</span>
            </div>
            <div style="font-size: 14.5px; line-height: 1.7; color: #CBD5E1;">
                {summary}
            </div>
        </div>
        """
    )

    render_html("<div style='height: 14px;'></div>")

    # Overall Recommendation Card
    recommendation = result.get("overall_recommendation", "No recommendation available.")

    render_html(
        f"""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(6, 182, 212, 0.08)); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 18px; padding: 22px; box-shadow: 0 10px 25px rgba(0,0,0,0.35);">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <span style="font-size: 18px;">⭐</span>
                <span style="font-size: 16px; font-weight: 800; color: #34D399; font-family: 'Outfit', sans-serif;">Strategic Action Recommendation</span>
            </div>
            <div style="font-size: 14.5px; line-height: 1.7; color: #E2E8F0;">
                {recommendation}
            </div>
        </div>
        """
    )

    st.divider()
