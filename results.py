import streamlit as st
from utils import render_html

from components.metrics import render_metrics
from components.dashboard import render_dashboard
from components.skills import render_skills
from components.reviews import render_reviews
from components.interview import render_interview
from components.charts import render_charts
from components.decision import render_decision


def render_results(result, job_title):
    ats = result.get("ats_score", 0)
    resume = result.get("resume_score", 0)
    decision = result.get("hiring_decision", "Unknown")

    # ==================================================
    # Dashboard Header & Executive Snapshot
    # ==================================================
    render_html(
        f"""
        <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.75), rgba(15, 23, 42, 0.85)); border: 1px solid rgba(255, 255, 255, 0.08); border-top: 3px solid #6366F1; border-radius: 22px; padding: 26px 30px; box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4); margin-bottom: 25px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; margin-bottom: 18px;">
                <div>
                    <div style="display: inline-flex; align-items: center; gap: 6px; padding: 3px 12px; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 999px; font-size: 11px; font-weight: 700; color: #A5B4FC; text-transform: uppercase;">
                        ⚡ Comprehensive Audit Complete
                    </div>
                    <h2 style="font-size: 28px; font-weight: 900; margin: 8px 0 2px 0;" class="gradient-title">Resume Intelligence Dashboard</h2>
                    <div style="font-size: 13.5px; color: #94A3B8;">Benchmarked Target Role: <b style="color: #FFFFFF;">{job_title}</b></div>
                </div>
                
                <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                    <div style="background: rgba(6, 182, 212, 0.12); border: 1px solid rgba(6, 182, 212, 0.3); padding: 8px 16px; border-radius: 14px; text-align: center;">
                        <div style="font-size: 10px; font-weight: 700; color: #67E8F9; text-transform: uppercase;">ATS Score</div>
                        <div style="font-size: 20px; font-weight: 900; color: #FFFFFF; font-family: 'Outfit';">{ats}%</div>
                    </div>
                    <div style="background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.3); padding: 8px 16px; border-radius: 14px; text-align: center;">
                        <div style="font-size: 10px; font-weight: 700; color: #A5B4FC; text-transform: uppercase;">Resume Score</div>
                        <div style="font-size: 20px; font-weight: 900; color: #FFFFFF; font-family: 'Outfit';">{resume}%</div>
                    </div>
                    <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); padding: 8px 16px; border-radius: 14px; text-align: center;">
                        <div style="font-size: 10px; font-weight: 700; color: #34D399; text-transform: uppercase;">Status</div>
                        <div style="font-size: 14px; font-weight: 800; color: #FFFFFF; margin-top: 4px;">{decision}</div>
                    </div>
                </div>
            </div>
            
            <p style="font-size: 14px; line-height: 1.6; color: #CBD5E1; margin: 0;">
                Your resume has undergone a complete multi-vector evaluation against industry ATS filtering algorithms and job requirements. 
                Explore each analytical module below to pinpoint exact optimization opportunities.
            </p>
        </div>
        """
    )

    # Key Metrics
    render_metrics(result)

    # Hiring Decision
    render_decision(result)

    render_html("<div style='height: 16px;'></div>")

    # Dashboard Overview
    render_dashboard(result)

    # Charts & Visual Insights
    render_charts(result)

    # Skills Analysis
    render_skills(result)

    # AI Resume Review
    render_reviews(result)

    # Interview Questions
    render_interview(result)
