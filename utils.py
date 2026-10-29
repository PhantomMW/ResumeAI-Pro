import re
import textwrap
import streamlit as st


def clean_text(text):
    """
    Clean extracted resume text.
    """
    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove extra blank lines
    text = text.strip()

    return text


def is_supported_file(filename):
    """
    Check supported resume formats.
    """
    filename = filename.lower()
    return filename.endswith(".pdf") or filename.endswith(".docx")


def render_html(html_str):
    """
    Safely render raw HTML in Streamlit without CommonMark treating indented lines as code blocks.
    """
    cleaned = textwrap.dedent(html_str).strip()
    if hasattr(st, "html"):
        st.html(cleaned)
    else:
        st.markdown(cleaned, unsafe_allow_html=True)
