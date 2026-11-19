
import os
import subprocess
import docx
import pdfplumber

from langchain_core.tools import tool


@tool
def extract_cv_text(file_path: str) -> str:
    """
    Extract text from a CV file in PDF, DOCX, or DOC format.

    Args:
        file_path: Path to the CV document.

    Returns:
        Extracted text or an error message.
    """

    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".docx":
        try:
            document = docx.Document(file_path)
            text = [para.text for para in document.paragraphs]
            return "\n".join(text)

        except Exception as e:
            return f"Error reading the DOCX file: {e}"

    elif ext == ".pdf":
        try:
            text = []

            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text.append(page_text)

            return "\n".join(text)

        except Exception as e:
            return f"Error reading the PDF file: {e}"

    elif ext == ".doc":
        try:
            subprocess.run(
                [
                    "soffice",
                    "--headless",
                    "--convert-to",
                    "docx",
                    "--outdir",
                    os.path.dirname(file_path) or ".",
                    file_path
                ],
                check=True,
                capture_output=True,
                text=True
            )

            converted_file = os.path.splitext(file_path)[0] + ".docx"

            document = docx.Document(converted_file)
            text = [para.text for para in document.paragraphs]

            os.remove(converted_file)

            return "\n".join(text)

        except Exception as e:
            return f"Error reading the DOC file: {e}"

    else:
        return "Unsupported file format. Please use .pdf, .docx, or .doc."
