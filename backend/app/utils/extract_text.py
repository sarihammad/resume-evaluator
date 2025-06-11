from io import BytesIO
import fitz

def extract_text_from_file(content: bytes, filename: str) -> str:
    if filename.endswith(".pdf"):
        doc = fitz.open(stream=content, filetype="pdf")
        return " ".join(page.get_text() for page in doc)
    else:
        return content.decode("utf-8")
