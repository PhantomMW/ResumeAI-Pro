import re


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