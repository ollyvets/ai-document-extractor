import fitz  # PyMuPDF
import json
import os
from typing import List, Optional
from pydantic import BaseModel
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("Critical Error: ANTHROPIC_API_KEY is missing in the .env file.")
client = Anthropic(api_key=api_key)

class ResumeData(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    skills: List[str] = []
    experience_years: Optional[int] = 0
    education: Optional[str] = None

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Извлекает текст из PDF."""
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        raise ValueError(f"Failed to read PDF: {str(e)}")

def analyze_text_with_ai(text: str) -> ResumeData:
    """Отправляет текст в Claude и возвращает валидированные данные Pydantic."""
    prompt = f"""
    You are an expert HR data extraction system.
    Extract the following information from the provided resume text.
    Return ONLY a valid JSON object. Do not include any explanations.
    
    Required JSON structure:
    {{
        "full_name": "extracted full name or null",
        "email": "extracted email or null",
        "skills": ["skill 1", "skill 2"],
        "experience_years": total years of experience as an integer or 0,
        "education": "highest degree and institution or null"
    }}

    Resume text:
    {text}
    """

    response = client.messages.create(
        model="claude-3-haiku-20240307", 
        max_tokens=1000,
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )
    
    result_text = response.content[0].text.strip()
    
    result_text = result_text.replace("```json", "").replace("```", "").strip()
    
    try:
        parsed_data = json.loads(result_text)

        validated_data = ResumeData(**parsed_data)
        return validated_data
    except json.JSONDecodeError:
        raise ValueError("AI did not return a valid JSON format.")
    except Exception as e:
        raise ValueError(f"Data validation failed: {str(e)}")