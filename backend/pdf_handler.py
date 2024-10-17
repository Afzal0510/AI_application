from PyPDF2 import PdfReader

async def process_pdf(file):
    pdf_reader = PdfReader(file.file)
    content = ""
    for page in pdf_reader.pages:
        content += page.extract_text()
    return content
