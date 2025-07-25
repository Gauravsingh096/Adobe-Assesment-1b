def extract_sections(pdf_path):
    # Basic: extract each page as a section with dummy title
    sections = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                sections.append({
                    "page_number": i+1,
                    "section_title": f"Page {i+1}",
                    "text": text.strip()
                })
    except Exception as e:
        print(f"Error parsing {pdf_path}: {e}")
    return sections
# PDF parsing utilities
import PyPDF2

def extract_sections(pdf_path):
    # Basic: extract each page as a section with dummy title
    sections = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                sections.append({
                    "page_number": i+1,
                    "section_title": f"Page {i+1}",
                    "text": text.strip()
                })
    except Exception as e:
        print(f"Error parsing {pdf_path}: {e}")
    return sections
