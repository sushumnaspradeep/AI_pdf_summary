import fitz
import langdetect

def detect_language(text):
    try:
        return langdetect.detect(text)
    except:
        return "unknown"

def extract_pdf_metadata(pdf_path):
    doc = fitz.open(pdf_path)
    metadata = doc.metadata
    return {
        "Title": metadata.get("title", "Unknown"),
        "Author": metadata.get("author", "Unknown"),
        "CreationDate": metadata.get("creationDate", "Unknown"),
        "Pages": len(doc)
    }
