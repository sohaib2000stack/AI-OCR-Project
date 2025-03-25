from ocr import extract_text_from_image, extract_text_from_pdf
from gen_ai import generate_text
import os

def clear_output_file():
    """Clears output.txt before processing new text."""
    with open("output.txt", "w", encoding="utf-8") as file:
        file.truncate(0)  # Clears previous content

def main():
    choice = input("Extract from (1) Image or (2) PDF? ")

    if choice == "1":
        image_path = input("Enter image file path: ").strip()
        clear_output_file()  # Ensure old text is removed
        text = extract_text_from_image(image_path)
    elif choice == "2":
        pdf_path = input("Enter PDF file path: ").strip()
        clear_output_file()  # Ensure old text is removed
        text = extract_text_from_pdf(pdf_path)
    else:
        print("Invalid choice!")
        return

    # Print extracted text
    print("\nExtracted Text:\n", text)

    # Read extracted text from output.txt
    if os.path.exists("output.txt"):
        with open("output.txt", "r", encoding="utf-8") as file:
            text = file.read().strip()

    # If no text was extracted, don't process further
    if not text:
        print("\n⚠️ No text found. AI generation skipped.")
        return

    # Generate AI response
    response = generate_text(text)
    print("\nGenerated AI Response:\n", response)

if __name__ == "__main__":
    main()































# from ocr import extract_text_from_image, extract_text_from_pdf, convert_pdf_to_searchable
# from gen_ai import generate_text
# import os

# def main():
#     choice = input("Select an option:\n(1) Extract text from Image\n(2) Extract text from PDF\n(3) Convert Scanned PDF to Selectable PDF\nChoice: ")

#     if choice == "1":
#         image_path = input("Enter image file path: ").strip()
#         text = extract_text_from_image(image_path)
#     elif choice == "2":
#         pdf_path = input("Enter PDF file path: ").strip()
#         text = extract_text_from_pdf(pdf_path)
#     elif choice == "3":
#         pdf_path = input("Enter scanned PDF file path: ").strip()
#         result = convert_pdf_to_searchable(pdf_path)
#         print(result)
#         return
#     else:
#         print("Invalid choice!")
#         return

#     print("\nExtracted Text:\n", text)

#     # Read extracted text from output.txt
#     if os.path.exists("output.txt"):
#         with open("output.txt", "r", encoding="utf-8") as file:
#             text = file.read().strip()

#     if not text:
#         print("\n⚠️ No text found. AI generation skipped.")
#         return

#     response = generate_text(text)
#     print("\nGenerated AI Response:\n", response)

#     save_choice = input("Do you want to save the extracted text as a Word or PDF file? (yes/no): ").strip().lower()
#     if save_choice == "yes":
#         print("✅ Extracted text has been saved as 'extracted_text.docx' and 'extracted_text.pdf'.")

# if __name__ == "__main__":
#     main()








