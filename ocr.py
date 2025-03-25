import pytesseract
from PIL import Image
import pdfplumber
from pdf2image import convert_from_path
import os

# Set Tesseract path (Make sure Tesseract is installed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def clear_output_file():
    """Clears output.txt before saving new extracted text."""
    with open("output.txt", "w", encoding="utf-8") as file:
        file.truncate(0)  # Clears previous content

def save_text_to_file(text):
    """Saves extracted text to output.txt after clearing old text."""
    clear_output_file()  # Ensure the file is cleared before writing
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text.strip())

def extract_text_from_image(image_path):
    """Extracts text from an image file using OCR and saves it."""
    try:
        image = Image.open(image_path).convert("L")  # Convert to grayscale for better OCR
        text = pytesseract.image_to_string(image, lang="eng+urd")  # English + Urdu OCR

        if text.strip():
            save_text_to_file(text)  # Save fresh text to file

        return text.strip() if text.strip() else "No text found in the image."

    except Exception as e:
        return f"Error processing image: {str(e)}"

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file. Uses OCR if text is not selectable and saves output."""
    text = ""

    if not os.path.exists(pdf_path):
        return "Error: PDF file not found."

    try:
        clear_output_file()  # Ensure the output file is empty before extraction

        # Try extracting selectable text using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"

        # If no selectable text is found, use OCR (convert all pages to images dynamically)
        if not text.strip():
            images = convert_from_path(pdf_path)  # Process all pages dynamically
            for img in images:
                text += pytesseract.image_to_string(img, lang="eng+urd") + "\n"

        if text.strip():
            save_text_to_file(text)  # Save fresh text to file

        return text.strip() if text.strip() else "No text found in the PDF."

    except Exception as e:
        return f"Error processing PDF: {str(e)}"












































# import pytesseract
# from PIL import Image
# import pdfplumber
# from pdf2image import convert_from_path
# import os
# from docx import Document
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from pypdf import PdfReader, PdfWriter

# # Set Tesseract path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def clear_output_file():
#     """Clears output.txt before saving new extracted text."""
#     with open("output.txt", "w", encoding="utf-8") as file:
#         file.truncate(0)

# def save_text_to_pdf(text, filename="extracted_text.pdf"):
#     """Saves extracted text to a proper PDF file."""
#     c = canvas.Canvas(filename, pagesize=letter)
#     c.setFont("Helvetica", 10)
#     y_position = 750

#     for line in text.split("\n"):
#         c.drawString(50, y_position, line)
#         y_position -= 15  # Move down for next line

#         if y_position < 50:  # If the page is full, add a new page
#             c.showPage()
#             c.setFont("Helvetica", 10)
#             y_position = 750

#     c.save()

# def save_text_to_word(text, filename="extracted_text.docx"):
#     """Saves extracted text to a properly formatted Word file."""
#     doc = Document()
#     doc.add_heading("Extracted Text", level=1)

#     for paragraph in text.split("\n\n"):
#         doc.add_paragraph(paragraph)

#     doc.save(filename)

# def extract_text_from_image(image_path):
#     """Extracts text from an image file using OCR and saves it."""
#     try:
#         image = Image.open(image_path).convert("L")
#         text = pytesseract.image_to_string(image, lang="eng+urd")

#         if text.strip():
#             save_text_to_word(text, "image_extracted_text.docx")
#             save_text_to_pdf(text, "image_extracted_text.pdf")
#             with open("output.txt", "w", encoding="utf-8") as file:
#                 file.write(text.strip())

#         return text.strip() if text.strip() else "No text found in the image."

#     except Exception as e:
#         return f"Error processing image: {str(e)}"

# def extract_text_from_pdf(pdf_path):
#     """Extracts text from a PDF file. Uses OCR if text is not selectable."""
#     text = ""

#     if not os.path.exists(pdf_path):
#         return "Error: PDF file not found."

#     try:
#         clear_output_file()

#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 extracted_text = page.extract_text()
#                 if extracted_text:
#                     text += extracted_text + "\n"

#         if not text.strip():
#             images = convert_from_path(pdf_path)
#             for img in images:
#                 text += pytesseract.image_to_string(img, lang="eng+urd") + "\n"

#         if text.strip():
#             save_text_to_word(text, "pdf_extracted_text.docx")
#             save_text_to_pdf(text, "pdf_extracted_text.pdf")
#             with open("output.txt", "w", encoding="utf-8") as file:
#                 file.write(text.strip())

#         return text.strip() if text.strip() else "No text found in the PDF."

#     except Exception as e:
#         return f"Error processing PDF: {str(e)}"

# def convert_pdf_to_searchable(pdf_path, output_pdf="searchable_output.pdf"):
#     """Converts an unselectable scanned PDF into a selectable, searchable PDF."""
#     if not os.path.exists(pdf_path):
#         return "❌ Error: PDF file not found."

#     try:
#         images = convert_from_path(pdf_path)
#         pdf_writer = PdfWriter()

#         for i, img in enumerate(images):
#             text = pytesseract.image_to_string(img, lang="eng+urd")

#             temp_pdf = f"temp_page_{i}.pdf"
#             c = canvas.Canvas(temp_pdf, pagesize=letter)
#             c.setFont("Helvetica", 10)
#             c.drawString(50, 750, text)
#             c.save()

#             temp_reader = PdfReader(temp_pdf)
#             original_reader = PdfReader(pdf_path)

#             page = original_reader.pages[i]
#             page.merge_page(temp_reader.pages[0])
#             pdf_writer.add_page(page)

#             os.remove(temp_pdf)

#         with open(output_pdf, "wb") as f:
#             pdf_writer.write(f)

#         return f"✅ Searchable PDF saved as {output_pdf}"

#     except Exception as e:
#         return f"❌ Error processing PDF: {str(e)}"

