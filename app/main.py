import uvicorn
from fastapi import FastAPI, UploadFile, File, Query
from summarization import summarize_large_text
from ocr import extract_text_from_pdf
from utils import extract_pdf_metadata, detect_language

app = FastAPI()

@app.post("/summarize")
async def summarize_pdf(
    file: UploadFile = File(...), 
    model: str = Query("bart", description="Summarization model: bart, t5, or pegasus")
):
    """Handles PDF upload, text extraction, summarization, and metadata extraction."""
    file_path = f"temp_{file.filename}"

    try:
        # Save uploaded PDF
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Extract text
        text = extract_text_from_pdf(file_path)
        if len(text.strip()) < 50:
            return {"error": "PDF contains too little text for summarization."}

        # Detect language
        language = detect_language(text)

        # Summarize text (Ensuring <= 100 words)
        summary = summarize_large_text(text, model=model)

        # Extract metadata
        metadata = extract_pdf_metadata(file_path)

        return {"metadata": metadata, "language": language, "summary": summary}

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
