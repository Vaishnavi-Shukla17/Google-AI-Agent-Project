import fitz

def extract_pdf_text(pdf_file, max_pages: int = None) -> str:
    pdf_file.seek(0)
    pdf_bytes = pdf_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    full_text = []
    total_pages = len(doc)
    pages_to_read = total_pages if max_pages is None else min(max_pages, total_pages)

    for page_num in range(pages_to_read):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        if text and text.strip():
            full_text.append(text)

    return "\n".join(full_text).strip()

def chunk_text(text: str, chunk_size: int = 2500, overlap: int = 200):
    if not text.strip():
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks
