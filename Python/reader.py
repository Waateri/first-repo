import os
import regex as re
from PyPDF2 import PdfReader
import easyocr

reader = easyocr.Reader(['en'])  # Initialize the easyocr reader with just English

def extract_largest_number(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        first_page = pdf_reader.pages[0]
        text = first_page.extract_text()

        # Extract amounts excluding dates and percentages
        pattern = r"(?![(\[]\d+[\.,]\d{2}[)\]])(?<!\d\.)\b(?<!VAT\s*)\d+[\.,]\d{2}\b(?!\.\d{4}|%)"
        matches = re.findall(pattern, text)

        if matches:
            largest_number = max(float(match.replace(',', '.')) for match in matches)
            return largest_number
        else:
            print(f"Couldn't find any numbers in {pdf_path}")
            return 0

def extract_largest_number_from_image(img_path):
    """Extract the largest amount from the given image using easyocr."""
    results = reader.readtext(img_path)
    
    # Extract all detected text
    text = ' '.join([result[1] for result in results])
    
    # Extract amounts excluding dates and percentages
    pattern = r"(?![(\[]\d+[\.,]\d{2}[)\]])(?<!\d\.)\b(?<!VAT\s*)\d+[\.,]\d{2}\b(?!\.\d{4}|%)"
    matches = re.findall(pattern, text)
    
    if matches:
        largest_number = max(float(match.replace(',', '.')) for match in matches)
        return largest_number
    else:
        print(f"Couldn't find any numbers in {img_path}")
        return 0

# Example usage remains the same for the rest of the script

folder_path = "2-2025"  # Change this to the path of your folder containing the PDFs and images
total_sum = 0

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        largest_number = extract_largest_number(pdf_path)
        print(f"Amount in {filename}: €{largest_number:.2f}")
        total_sum += largest_number
    elif filename.lower().endswith((".jpeg", ".png")):
        img_path = os.path.join(folder_path, filename)
        largest_number = extract_largest_number_from_image(img_path)
        print(f"Amount in {filename}: €{largest_number:.2f}")
        total_sum += largest_number

print(f"Total sum of the largest numbers in all invoices: €{total_sum:.2f}")
