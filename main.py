from fastapi import FastAPI, UploadFile, File, HTTPException
from services import extract_text_from_pdf, analyze_text_with_ai, ResumeData

app = FastAPI(
    title="AI Document Extractor API",
    description="API for extracting structured data from PDF resumes using Anthropic Claude."
)

@app.post("/api/extract", response_model=ResumeData)
async def extract_document_data(file: UploadFile = File(...)):
    """
    Upload a PDF file and extract structured data using AI.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        file_bytes = await file.read()
        
        extracted_text = extract_text_from_pdf(file_bytes)
        
        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="PDF is empty or contains no readable text.")
        
        structured_data = analyze_text_with_ai(extracted_text)
        
        return structured_data

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")