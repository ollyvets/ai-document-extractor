# 📄 Universal AI Document Extractor
### *Turning the chaos of PDF documents into structured business data.*

## 🌟 Why I Built This
Manual data entry is a silent productivity killer. Whether it’s an HR manager processing 100 resumes or an accountant dealing with mismatched invoices, the pain is the same: **hours of wasted time and inevitable human errors.**

I developed this tool to bridge the gap between "unstructured text" and "actionable data." By combining the semantic power of **Anthropic’s Claude 3.5** with a robust **FastAPI** backend, this service doesn't just "scrape" text—it *understands* it.

## ✨ Key Features
- **Semantic Understanding:** Unlike old-school parsers, this tool doesn't rely on rigid templates. It understands context, meaning it can extract data from a resume regardless of its layout.
- **Production-Ready Architecture:** - **FastAPI:** High-performance asynchronous API.
    - **Pydantic Validation:** Ensures the AI output always matches the required format (no broken JSON).
    - **Clean Code:** Modular structure following the Separation of Concerns principle.
- **Instant Excel Export:** A user-friendly Streamlit interface allows you to upload a file and get a clean `.xlsx` report in seconds.

## 🛠 Tech Stack
- **Language:** Python 3.10+
- **LLM:** Anthropic Claude 3.5 (Haiku/Sonnet)
- **Frameworks:** FastAPI, Streamlit
- **Libraries:** PyMuPDF (PDF processing), Pandas (Data handling), Pydantic (Validation)

## 🚀 Getting Started

1. **Clone & Install:**
   ```bash
   git clone [https://github.com/yourusername/ai-document-extractor.git]
   cd ai-document-extractor
   python -m venv venv
   source venv/bin/activate # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

2. **Configuration:**
   Create a .env file in the root directory:

   ANTHROPIC_API_KEY=your_actual_api_key_here

3. **Launch**

   Start the Backend: uvicorn main:app --reload

   Start the UI: streamlit run ui.py

## 🤝 Let's Collaborate!
This project is a baseline for what AI-driven automation can do. I can customize this tool for:

 - Automatic Invoice Processing (Integration with accounting software).
 - Medical Record Digitization.
 - Large-scale Legal Document Analysis.

Need a custom AI solution for your business? [Drop me a message on Upwork] or [Open an Issue] — I'm always happy to chat about interesting challenges! https://www.upwork.com/freelancers/~010745b4d221a00300
