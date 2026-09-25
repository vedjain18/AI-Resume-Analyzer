import pymupdf
from docx import Document


def extract_text_from_pdf(file_path):
    text = ""

    pdf = pymupdf.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def extract_text_from_docx(file_path):
    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_resume_text(file_path):
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")
if __name__ == "__main__":
    file_path = "resume_demo.docx"

    text = extract_resume_text(file_path)

    print("----- EXTRACTED RESUME TEXT -----")
    print(text)
    print("----- END -----") 