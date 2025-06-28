from pypdf import PdfReader
from io import StringIO
from pdfminer.high_level import extract_text, extract_text_to_fp


def convert_pdf_to_text(pdf_path):
    reader = PdfReader(pdf_path)
    text_per_page = []
    for i in range(len(reader.pages)):
        text = extract_text(pdf_path, page_numbers=[i])
        text_per_page.append(text.strip())
    return text_per_page
