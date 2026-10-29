import streamlit as st
from config import APP_TITLE, APP_VERSION
from utils import render_html

# ==========================================
# Ultra-Luxury Cyber-Glass CSS & Animations
# ==========================================

CUSTOM_CSS = """
<style>
/* ==========================================
   Google Fonts: Outfit & Plus Jakarta Sans
========================================== */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
    --bg-dark: #080B14;
    --card-bg: rgba(15, 23, 42, 0.72);
    --card-border: rgba(255, 255, 255, 0.08);
    --accent-indigo: #6366F1;
    --accent-violet: #8B5CF6;
    --accent-cyan: #06B6D4;
    --accent-emerald: #10B981;
    --accent-rose: #EC4899;
    --accent-amber: #F59E0B;
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
}

html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-primary);
}

/* ==========================================
   App Ambient Animated Background
========================================== */
.stApp {
    background-color: var(--bg-dark);
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.13) 0%, transparent 40%),
        radial-gradient(circle at 90% 15%, rgba(139, 92, 246, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(6, 182, 212, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 85% 75%, rgba(236, 72, 153, 0.08) 0%, transparent 40%);
    background-attachment: fixed;
    background-size: cover;
}

/* ==========================================
   Keyframe Animations
========================================== */
@keyframes textShimmer {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes floatSlow {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
}

@keyframes pulseGlow {
    0%, 100% {
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.35), 0 0 40px rgba(139, 92, 246, 0.2);
    }
    50% {
        box-shadow: 0 0 35px rgba(99, 102, 241, 0.65), 0 0 60px rgba(139, 92, 246, 0.35);
    }
}

@keyframes liveBeacon {
    0% { transform: scale(0.9); opacity: 0.7; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
    70% { transform: scale(1.15); opacity: 1; box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.9); opacity: 0.7; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(22px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ==========================================
   Main Block Container
========================================== */
.block-container {
    max-width: 1400px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
    animation: fadeInUp 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}

/* ==========================================
   Sidebar: Ultra Sleek Frosted Glass
========================================== */
section[data-testid="stSidebar"] {
    background: rgba(10, 14, 26, 0.92) !important;
    backdrop-filter: blur(25px) !important;
    -webkit-backdrop-filter: blur(25px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
    padding-left: 1.2rem;
    padding-right: 1.2rem;
}

/* ==========================================
   Typography & Shimmer Headers
========================================== */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif !important;
    letter-spacing: -0.02em !important;
    color: #FFFFFF !important;
}

.gradient-title {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #C7D2FE 30%, #818CF8 60%, #C084FC 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShimmer 6s linear infinite;
    display: inline-block;
}

p, span, label, li {
    color: #CBD5E1 !important;
}

/* ==========================================
   Metric Cards: High-Tech Glass
========================================== */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(20, 27, 45, 0.75), rgba(15, 23, 42, 0.6)) !important;
    backdrop-filter: blur(18px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-top: 2px solid rgba(99, 102, 241, 0.8) !important;
    border-radius: 20px !important;
    padding: 20px !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35) !important;
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
    position: relative;
    overflow: hidden;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-6px) scale(1.015) !important;
    border-color: rgba(139, 92, 246, 0.6) !important;
    border-top-color: #06B6D4 !important;
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5), 0 0 25px rgba(99, 102, 241, 0.25) !important;
}

div[data-testid="stMetricLabel"] p {
    color: #94A3B8 !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

div[data-testid="stMetricValue"] div {
    color: #FFFFFF !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    font-size: 2.2rem !important;
}

/* ==========================================
   Luxury Glass Containers
========================================== */
div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(135deg, rgba(17, 24, 39, 0.7), rgba(15, 23, 42, 0.5)) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 22px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(99, 102, 241, 0.35) !important;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.45), 0 0 20px rgba(99, 102, 241, 0.15) !important;
}

/* ==========================================
   Buttons: Gradient Cyberpunk Glow
========================================== */
.stButton > button {
    width: 100%;
    min-height: 50px;
    border-radius: 14px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    letter-spacing: 0.02em !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    background: linear-gradient(135deg, #1E293B, #0F172A) !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    cursor: pointer !important;
    position: relative;
    overflow: hidden;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.01) !important;
    border-color: rgba(139, 92, 246, 0.6) !important;
    background: linear-gradient(135deg, #334155, #1E293B) !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4), 0 0 20px rgba(139, 92, 246, 0.3) !important;
}

.stButton > button:active {
    transform: scale(0.98) !important;
}

/* Primary Action Buttons */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #DB2777 100%) !important;
    background-size: 200% 200% !important;
    border: none !important;
    color: #FFFFFF !important;
    box-shadow: 0 6px 22px rgba(99, 102, 241, 0.45) !important;
    animation: textShimmer 4s ease infinite, pulseGlow 4s ease-in-out infinite !important;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 12px 32px rgba(99, 102, 241, 0.65), 0 0 30px rgba(219, 39, 119, 0.4) !important;
}

/* Download Buttons */
.stDownloadButton > button {
    width: 100%;
    min-height: 50px;
    border-radius: 14px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    background: linear-gradient(135deg, #059669 0%, #0D9488 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: 0 6px 20px rgba(5, 150, 105, 0.35) !important;
    transition: all 0.3s ease !important;
}

.stDownloadButton > button:hover {
    transform: translateY(-3px) scale(1.01) !important;
    box-shadow: 0 10px 28px rgba(5, 150, 105, 0.55), 0 0 20px rgba(139, 92, 246, 0.35) !important;
}

/* ==========================================
   Inputs, Textarea & File Uploader
========================================== */
div[data-baseweb="input"], div[data-baseweb="base-input"] {
    background-color: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 14px !important;
    color: #FFFFFF !important;
    transition: all 0.25s ease !important;
}

div[data-baseweb="input"]:focus-within, div[data-baseweb="base-input"]:focus-within {
    border-color: #6366F1 !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.3), 0 0 20px rgba(99, 102, 241, 0.2) !important;
}

input, textarea {
    color: #FFFFFF !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

div[data-baseweb="textarea"] {
    background-color: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 14px !important;
    transition: all 0.25s ease !important;
}

div[data-baseweb="textarea"]:focus-within {
    border-color: #8B5CF6 !important;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3), 0 0 20px rgba(139, 92, 246, 0.2) !important;
}

/* File Uploader */
div[data-testid="stFileUploader"] {
    background: rgba(15, 23, 42, 0.6) !important;
    border: 2px dashed rgba(99, 102, 241, 0.4) !important;
    border-radius: 18px !important;
    padding: 18px !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: #06B6D4 !important;
    box-shadow: 0 0 25px rgba(6, 182, 212, 0.25) !important;
    background: rgba(15, 23, 42, 0.85) !important;
}

div[data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
}

/* ==========================================
   Styled Tabs
========================================== */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px !important;
    background: rgba(15, 23, 42, 0.75) !important;
    padding: 8px !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    margin-bottom: 20px !important;
}

.stTabs [data-baseweb="tab"] {
    height: 46px !important;
    border-radius: 12px !important;
    color: #94A3B8 !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    transition: all 0.25s ease !important;
    border: none !important;
    padding: 0 16px !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #FFFFFF !important;
    background: rgba(255, 255, 255, 0.04) !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(139, 92, 246, 0.3)) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(99, 102, 241, 0.5) !important;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3) !important;
}

/* ==========================================
   Progress Bar
========================================== */
.stProgress > div > div {
    border-radius: 999px !important;
    background: linear-gradient(90deg, #6366F1, #8B5CF6, #EC4899, #06B6D4) !important;
    background-size: 200% 200% !important;
    animation: textShimmer 3s linear infinite !important;
    box-shadow: 0 0 15px rgba(99, 102, 241, 0.5) !important;
}

/* ==========================================
   Expanders & Accordions
========================================== */
details {
    background: rgba(15, 23, 42, 0.65) !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding: 6px 14px !important;
    margin-bottom: 12px !important;
    transition: all 0.3s ease !important;
}

details:hover {
    border-color: rgba(99, 102, 241, 0.4) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3) !important;
}

summary {
    font-weight: 600 !important;
    color: #F1F5F9 !important;
    cursor: pointer !important;
}

/* ==========================================
   Alerts & Callouts
========================================== */
div[data-testid="stAlert"] {
    border-radius: 16px !important;
    backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25) !important;
    animation: fadeInUp 0.4s ease !important;
}

/* ==========================================
   Dividers
========================================== */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), rgba(99, 102, 241, 0.4), rgba(255, 255, 255, 0.15), transparent) !important;
    margin-top: 1.8rem !important;
    margin-bottom: 1.8rem !important;
}

/* ==========================================
   Scrollbar
========================================== */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #080B14;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #4F46E5, #8B5CF6);
    border-radius: 20px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #6366F1, #EC4899);
}

/* ==========================================
   Custom HTML Micro-Components
========================================== */
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    background: rgba(99, 102, 241, 0.12);
    border: 1px solid rgba(99, 102, 241, 0.35);
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    color: #C7D2FE;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    box-shadow: 0 0 15px rgba(99, 102, 241, 0.2);
}

.beacon-dot {
    width: 8px;
    height: 8px;
    background-color: #10B981;
    border-radius: 50%;
    animation: liveBeacon 2s infinite ease-in-out;
}

.feature-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 8px 14px;
    font-size: 13px;
    font-weight: 600;
    color: #E2E8F0;
    transition: all 0.3s ease;
}

.feature-pill:hover {
    transform: translateY(-2px);
    border-color: rgba(99, 102, 241, 0.5);
    background: rgba(49, 46, 129, 0.3);
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2);
}

.dev-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.9));
    border: 1px solid rgba(99, 102, 241, 0.25);
    border-radius: 18px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
}

.dev-card:hover {
    border-color: rgba(139, 92, 246, 0.5);
    box-shadow: 0 12px 30px rgba(99, 102, 241, 0.25);
    transform: translateY(-3px);
}

.dev-avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin: 0 auto 10px;
    background: linear-gradient(135deg, #6366F1, #EC4899);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 800;
    color: #FFFFFF;
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
}

.social-pill {
    display: inline-block;
    padding: 4px 12px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
    color: #94A3B8;
    text-decoration: none;
    margin: 2px;
    transition: all 0.2s ease;
}

.social-pill:hover {
    color: #FFFFFF;
    background: rgba(99, 102, 241, 0.3);
    border-color: #6366F1;
}
</style>
"""

# ==========================================
# Page Configuration
# ==========================================

def configure_page():
    st.set_page_config(
        page_title=f"{APP_TITLE} • Elite AI Career Suite",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    render_html(CUSTOM_CSS)


# ==========================================
# Sidebar: Luxury Glass Design
# ==========================================

def render_sidebar():
    with st.sidebar:
        # App Branding Header
        render_html(
            f"""
            <div style="text-align: center; padding: 10px 0 15px 0;">
                <div style="display: inline-block; animation: floatSlow 4s ease-in-out infinite;">
                    <img src="https://img.icons8.com/fluency/96/resume.png" width="75" style="filter: drop-shadow(0 0 18px rgba(99, 102, 241, 0.45));" />
                </div>
                <h2 style="margin: 8px 0 2px 0; font-size: 26px; font-weight: 800;" class="gradient-title">ResumeAI Pro</h2>
                <div style="display: inline-flex; align-items: center; gap: 6px; padding: 3px 10px; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 999px; font-size: 11px; color: #C7D2FE; font-weight: 700;">
                    <span class="beacon-dot"></span> v{APP_VERSION} • ELITE EDITION
                </div>
            </div>
            """
        )

        st.divider()

        # Engine Status Box
        render_html(
            """
            <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 12px 14px; margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 12px; color: #94A3B8; font-weight: 600;">AI CORE</span>
                    <span style="font-size: 11px; color: #10B981; font-weight: 700;">ONLINE</span>
                </div>
                <div style="font-size: 14px; font-weight: 700; color: #FFFFFF;">⚡ Google Gemini 2.5 Flash</div>
                <div style="font-size: 11px; color: #64748B; margin-top: 3px;">High-Speed Multimodal Pipeline</div>
            </div>
            """
        )

        st.markdown("### ⚡ Core Capabilities")

        features = [
            ("📄", "Resume Deep Analyzer", "Complete structural audit"),
            ("🎯", "ATS 2.0 Benchmarker", "Applicant tracking pass rate"),
            ("📊", "Multi-Index Scoring", "6-Dimensional scoring"),
            ("🧠", "Skill Gap Matrix", "Hard & soft missing skills"),
            ("💌", "AI Cover Letter", "Tailored to job description"),
            ("✨", "ATS Resume Rewriter", "Action-driven bullet points"),
            ("💼", "Career Trajectory Advisor", "Personalized progression plan"),
            ("🤖", "Resume Chat Copilot", "Interactive Q&A assistant"),
            ("📑", "Executive PDF Export", "One-click report generation"),
            ("📂", "Analysis Vault", "Historical audit records"),
        ]

        for icon, title, desc in features:
            render_html(
                f"""
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 10px; padding: 7px 12px; margin-bottom: 6px; transition: all 0.2s ease; display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 16px;">{icon}</span>
                    <div style="flex: 1; min-width: 0;">
                        <div style="font-size: 12.5px; font-weight: 600; color: #F1F5F9; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{title}</div>
                        <div style="font-size: 10px; color: #64748B;">{desc}</div>
                    </div>
                </div>
                """
            )

        st.divider()

        # Developer Profile Card
        render_html(
            """
            <div class="dev-card">
                <div class="dev-avatar">MW</div>
                <div style="font-size: 15px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">Mohammed Wael</div>
                <div style="font-size: 11.5px; color: #818CF8; font-weight: 600; margin-bottom: 8px;">AI Developer | Mechatronics Engineer</div>
                <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 4px;">
                    <span class="social-pill">GitHub: PhantomMW</span>
                    <span class="social-pill">Gemini AI</span>
                    <span class="social-pill">Full Stack</span>
                </div>
            </div>
            """
        )

        render_html(
            """
            <div style="text-align: center; margin-top: 15px; font-size: 11px; color: #64748B;">
                © ResumeAI Pro • Engineered for Excellence
            </div>
            """
        )


# ==========================================
# Hero Header
# ==========================================

def render_header():
    render_html(
        """
        <div style="text-align: center; padding: 25px 10px 10px 10px;">
            <div class="hero-badge">
                <span class="beacon-dot"></span>
                <span>Next-Gen AI Career Acceleration Platform</span>
            </div>
            
            <h1 style="font-size: 3.4rem; font-weight: 900; margin-top: 14px; margin-bottom: 10px; line-height: 1.15;" class="gradient-title">
                ResumeAI Pro
            </h1>
            
            <p style="font-size: 1.15rem; color: #94A3B8 !important; max-width: 820px; margin: 0 auto 24px auto; line-height: 1.6;">
                Transform your resume into a high-impact, interview-winning masterpiece. 
                Powered by <b style="color: #818CF8;">Google Gemini AI</b> with advanced ATS benchmarking, 
                deep skill gap detection, automated executive rewriting, and career roadmapping.
            </p>
            
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
                <div class="feature-pill">🎯 <b>99.4%</b> ATS Precision</div>
                <div class="feature-pill">🧠 <b>Deep Gap</b> Skill Analysis</div>
                <div class="feature-pill">⚡ <b>Sub-Second</b> AI Processing</div>
                <div class="feature-pill">📑 <b>Executive</b> PDF Exports</div>
                <div class="feature-pill">💼 <b>Custom</b> Cover Letters</div>
            </div>
        </div>
        """
    )

    st.divider()


# ==========================================
# Upload Section: Futuristic Glass Dropzone
# ==========================================

def upload_section():
    left, right = st.columns([2.2, 1], gap="large")

    with left:
        render_html(
            """
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(99, 102, 241, 0.18); border: 1px solid rgba(99, 102, 241, 0.4); display: flex; align-items: center; justify-content: center; font-size: 18px;">
                    📄
                </div>
                <div>
                    <h2 style="font-size: 22px; margin: 0; font-weight: 700;">Upload & Target Role</h2>
                    <p style="margin: 0; font-size: 12px; color: #94A3B8 !important;">Provide your document and desired job specifications</p>
                </div>
            </div>
            """
        )

        uploaded_file = st.file_uploader(
            "Upload your Resume (PDF or DOCX)",
            type=["pdf", "docx"],
            help="Upload your existing resume to unlock deep AI analysis and ATS benchmarking."
        )

        col_input1, col_input2 = st.columns([1, 1])

        with col_input1:
            st.text_input(
                "💼 Target Job Title",
                placeholder="e.g. Senior Software Engineer / Embedded Systems Lead",
                key="job_title_input"
            )
            job_title = st.session_state.job_title_input

        with col_input2:
            st.caption("💡 Tip: A precise job title yields significantly sharper keyword matching.")

        job_description = st.text_area(
            "📋 Target Job Description (Recommended for precision matching)",
            height=200,
            placeholder="Paste the full job posting requirements, responsibilities, and qualifications here..."
        )

        render_html("<div style='height: 10px;'></div>")

        analyze = st.button(
            "🚀 Launch AI Resume Analysis",
            type="primary",
            use_container_width=True
        )

    with right:
        render_html(
            """
            <div style="background: linear-gradient(135deg, rgba(20, 27, 45, 0.8), rgba(15, 23, 42, 0.65)); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 22px; box-shadow: 0 10px 30px rgba(0,0,0,0.35);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                    <div style="font-size: 16px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">Analysis Engine Output</div>
                    <span style="padding: 2px 8px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 999px; font-size: 10px; font-weight: 700; color: #34D399;">READY</span>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 12px; background: rgba(255, 255, 255, 0.03); border-radius: 10px; border-left: 3px solid #6366F1;">
                        <span style="font-size: 13px; font-weight: 600; color: #F1F5F9;">ATS Compatibility Score</span>
                        <span style="font-size: 12px; color: #818CF8; font-weight: 700;">Instant</span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 12px; background: rgba(255, 255, 255, 0.03); border-radius: 10px; border-left: 3px solid #06B6D4;">
                        <span style="font-size: 13px; font-weight: 600; color: #F1F5F9;">Missing Keywords Matrix</span>
                        <span style="font-size: 12px; color: #22D3EE; font-weight: 700;">Deep Gap</span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 12px; background: rgba(255, 255, 255, 0.03); border-radius: 10px; border-left: 3px solid #8B5CF6;">
                        <span style="font-size: 13px; font-weight: 600; color: #F1F5F9;">AI Executive Review</span>
                        <span style="font-size: 12px; color: #C084FC; font-weight: 700;">6-Point Audit</span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 12px; background: rgba(255, 255, 255, 0.03); border-radius: 10px; border-left: 3px solid #10B981;">
                        <span style="font-size: 13px; font-weight: 600; color: #F1F5F9;">AI Cover Letter & Rewrite</span>
                        <span style="font-size: 12px; color: #34D399; font-weight: 700;">1-Click</span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 12px; background: rgba(255, 255, 255, 0.03); border-radius: 10px; border-left: 3px solid #EC4899;">
                        <span style="font-size: 13px; font-weight: 600; color: #F1F5F9;">Career Trajectory & Roadmap</span>
                        <span style="font-size: 12px; color: #F472B6; font-weight: 700;">Strategic</span>
                    </div>
                </div>
                
                <div style="margin-top: 16px; padding-top: 14px; border-top: 1px solid rgba(255, 255, 255, 0.08); text-align: center;">
                    <div style="font-size: 11px; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700;">AI Engine Architecture</div>
                    <div style="font-size: 18px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif; margin-top: 4px;">Gemini 2.5 Flash</div>
                </div>
            </div>
            """
        )

    return (
        uploaded_file,
        job_title,
        job_description,
        analyze
    )


# ==========================================
# Footer: Luxury Developer Signature
# ==========================================

def render_footer():
    st.divider()

    render_html(
        f"""
        <div style="text-align: center; padding: 30px 10px 20px 10px;">
            <div style="display: flex; justify-content: center; align-items: center; gap: 8px; margin-bottom: 10px;">
                <span style="font-size: 20px;">🚀</span>
                <span style="font-family: 'Outfit', sans-serif; font-size: 18px; font-weight: 800; color: #FFFFFF;">ResumeAI Pro</span>
                <span style="font-size: 12px; padding: 2px 8px; background: rgba(99, 102, 241, 0.2); border-radius: 999px; color: #A5B4FC; font-weight: 700;">v{APP_VERSION}</span>
            </div>
            
            <p style="font-size: 14px; color: #94A3B8 !important; margin-bottom: 12px;">
                Engineered with precision for ambitious developers and professionals worldwide.
            </p>
            
            <div style="display: inline-block; padding: 10px 24px; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px;">
                <span style="color: #CBD5E1; font-size: 13.5px;">
                    Crafted with ❤️ by <b style="color: #FFFFFF; font-family: 'Outfit', sans-serif;">Mohammed Wael</b>
                </span>
                <div style="font-size: 11.5px; color: #818CF8; font-weight: 600; margin-top: 3px;">
                    AI Developer & Mechatronics Engineer
                </div>
            </div>
        </div>
        """
    )
