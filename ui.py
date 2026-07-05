import streamlit as st

from config import APP_TITLE, APP_VERSION


# ==========================================
# Professional CSS
# ==========================================

CUSTOM_CSS = """
<style>

/* ==========================================
Google Font
========================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
    color:#1F2937;
}

/* ==========================================
App Background
========================================== */

.stApp{
    background-color:#F5F7FB;
}

/* ==========================================
Main Container
========================================== */

.block-container{
    max-width:1400px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* ==========================================
Sidebar
========================================== */

section[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E5E7EB;
}

/* ==========================================
Headers
========================================== */

h1{
    color:#111827 !important;
    font-weight:700 !important;
}

h2,h3,h4{
    color:#1F2937 !important;
    font-weight:600 !important;
}

p,span,label,li{
    color:#374151 !important;
}

/* ==========================================
Metric Cards
========================================== */

div[data-testid="stMetric"]{

    background:#FFFFFF;

    border:1px solid #E5E7EB;

    border-radius:18px;

    padding:18px;

    box-shadow:0 4px 15px rgba(0,0,0,.05);

    transition:0.25s ease;

}

div[data-testid="stMetric"]:hover{

    transform:translateY(-4px);

    box-shadow:0 8px 25px rgba(0,0,0,.10);

}

/* ==========================================
Buttons
========================================== */

.stButton>button{

    width:100%;

    height:48px;

    border-radius:12px;

    font-weight:600;

    font-size:16px;

    border:none;

    transition:0.25s;

}

.stButton>button:hover{

    transform:translateY(-2px);

}

/* ==========================================
Inputs
========================================== */

div[data-baseweb="input"]{

    border-radius:12px;

}

div[data-baseweb="textarea"]{

    border-radius:12px;

}

textarea{

    border-radius:12px !important;

}

/* ==========================================
Progress Bar
========================================== */

.stProgress > div > div{

    border-radius:999px;

}

/* ==========================================
Expanders
========================================== */

details{

    border-radius:12px;

    border:1px solid #E5E7EB;

}

/* ==========================================
Containers
========================================== */

div[data-testid="stVerticalBlock"]{
    gap:1rem;
}

/* ==========================================
Divider
========================================== */

hr{
    margin-top:1.2rem;
    margin-bottom:1.2rem;
}

/* ==========================================
Scrollbar
========================================== */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#CBD5E1;
    border-radius:20px;
}

::-webkit-scrollbar-thumb:hover{
    background:#94A3B8;
}

</style>
"""

# ==========================================
# Page Configuration
# ==========================================

def configure_page():

    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(
        CUSTOM_CSS,
        unsafe_allow_html=True
    )


# ==========================================
# Sidebar
# ==========================================

def render_sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/fluency/96/resume.png",
            width=80
        )

        st.title("ResumeAI Pro")

        st.caption(f"Version {APP_VERSION}")

        st.divider()

        st.markdown("## 📌 Features")

        st.info("📄 Resume Analyzer")
        st.info("🎯 ATS Checker")
        st.info("📊 Resume Score")
        st.info("🧠 Skill Gap Analysis")
        st.info("💌 Cover Letter")
        st.info("✨ Resume Rewriter")
        st.info("💼 Career Advisor")
        st.info("🤖 Resume Chat")
        st.info("📑 PDF Report")
        st.info("📂 History")

        st.divider()

        st.markdown("### 🤖 AI Model")

        st.success("Google Gemini")

        st.divider()

        st.markdown("### 👨‍💻 Developer")

        st.write("**Mohammed Wael**")

        st.caption("Mechatronics Engineering")

        st.divider()

        st.caption("© ResumeAI Pro")
        # ==========================================
# Header
# ==========================================

def render_header():

    st.title("🚀 ResumeAI Pro")

    st.caption(
        "AI-Powered Resume Analysis • ATS Optimization • Career Assistant"
    )

    st.divider()

    with st.container(border=True):

        st.markdown("""
### 🤖 Your Personal AI Career Assistant

Upload your resume and receive a complete AI-powered analysis including:

- 📊 ATS Compatibility Score
- 📄 Resume Quality Evaluation
- 🎯 Job Matching Analysis
- 🧠 Missing Skills Detection
- 💡 Professional Improvement Suggestions
- 💌 AI Cover Letter Generator
- ✨ Resume Rewriter
- 💼 Career Roadmap
- 🤖 Resume AI Chat
- 📑 Professional PDF Report

""")

    st.divider()


# ==========================================
# Upload Section
# ==========================================

def upload_section():

    left, right = st.columns([2.4, 1])

    with left:

        st.markdown("## 📄 Upload Your Resume")

        uploaded_file = st.file_uploader(
            "Choose your Resume",
            type=["pdf", "docx"]
        )

        st.caption(
            "Supported formats: PDF (.pdf) and Word (.docx)"
        )

        st.text_input(
            "💼 Target Job Title",
            placeholder="Example: Embedded Systems Engineer",
            key="job_title_input"
        )

        job_title = st.session_state.job_title_input

        job_description = st.text_area(
            "📋 Job Description",
            height=250,
            placeholder="Paste the complete job description here..."
        )

        st.divider()

        analyze = st.button(
            "🚀 Analyze Resume",
            type="primary",
            use_container_width=True
        )

    with right:

        st.markdown("## 📈 Analysis Output")

        st.success("✅ ATS Compatibility")

        st.success("✅ Resume Score")

        st.success("✅ Job Match")

        st.success("✅ Missing Skills")

        st.success("✅ AI Suggestions")

        st.success("✅ Cover Letter")

        st.success("✅ Resume Rewrite")

        st.success("✅ Career Advice")

        st.success("✅ Resume Chat")

        st.success("✅ PDF Report")

        st.divider()

        st.metric(
            label="AI Engine",
            value="Gemini"
        )

    return (
        uploaded_file,
        job_title,
        job_description,
        analyze
    )

# ==========================================
# Footer
# ==========================================

def render_footer():

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.caption("🚀 ResumeAI Pro")

    with col2:
        st.caption(f"Version {APP_VERSION}")

    with col3:
        st.caption("Powered by Google Gemini")

    st.markdown(
    """
    <div style="text-align:center;
                padding-top:15px;
                color:gray;
                font-size:14px;">
        Developed with ❤️ by <b>Mohammed Wael</b><br>
        <b>AI Developer | Mechatronics Engineer</b>
    </div>
    """,
    unsafe_allow_html=True
)