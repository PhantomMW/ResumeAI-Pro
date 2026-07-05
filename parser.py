import pdfplumber
from docx import Document


def extract_text_from_pdf(pdf_file):
    """
    Extract text from PDF files.
    """

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()


def extract_text_from_docx(docx_file):
    """
    Extract text from DOCX files.
    """

    document = Document(docx_file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text.strip()


def extract_resume_text(uploaded_file):
    """
    Detect file type and extract text.
    """

    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        return ""