import fitz
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_text = ""

    for page in doc:
        text = page.get_text("text")
        if text.strip():
            extracted_text += text + "\n"
        else:
            for img in page.get_images(full=True):
                xref = img[0]
                base_image = doc.extract_image(xref)
                img = Image.open(io.BytesIO(base_image["image"]))
                extracted_text += pytesseract.image_to_string(img) + "\n"

    return extracted_text if extracted_text.strip() else "No readable text found in PDF."
