import streamlit as st
import requests
import pandas as pd
from io import BytesIO


st.set_page_config(page_title="AI CV Extractor", page_icon="📄", layout="centered")

def convert_json_to_excel(data: dict) -> bytes:
    """
    Converts a Python dictionary into an Excel file format.
    Formats lists into comma-separated strings for better readability in Excel.
    """

    export_data = data.copy()
    

    if "skills" in export_data and isinstance(export_data["skills"], list):
        export_data["skills"] = ", ".join(export_data["skills"])
        

    df = pd.DataFrame([export_data])
    
    output = BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Extracted Data')
    
    return output.getvalue()

def main():
    """
    Main function to render the Streamlit user interface.
    Handles user interactions: file upload, API calls, and displaying results.
    """
    st.title("📄 Universal AI CV Extractor")
    st.markdown("Upload a PDF resume, and the AI will extract structured data into an Excel file.")


    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

    if uploaded_file is not None:
        if st.button("Extract Data ✨"):
            with st.spinner('AI is analyzing the document...'):
             
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                
                try:

                    response = requests.post("http://localhost:8000/api/extract", files=files)
                    
                    if response.status_code == 200:
                        result_data = response.json()
                        
                        st.success("Data successfully extracted!")
                        
                        st.subheader("Extracted JSON Data")
                        st.json(result_data)

                        excel_data = convert_json_to_excel(result_data)
                        
                        st.download_button(
                            label="📥 Download as Excel",
                            data=excel_data,
                            file_name="extracted_cv_data.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    else:
                        st.error(f"Error from backend: {response.json().get('detail', 'Unknown error')}")
                        
                except requests.exceptions.ConnectionError:
                    st.error("Failed to connect to the backend. Ensure the FastAPI server is running on port 8000.")

if __name__ == "__main__":
    main()