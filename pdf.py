import os
import PyPDF2
import pdfplumber
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path):
    text = ""

    # 1️⃣ Essayer d'abord avec pdfplumber (pour PDF texte)
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except:
        pass

    # 2️⃣ Si aucun texte n'a été extrait, utiliser OCR (pour PDF scanné)
    if not text.strip():
        print("Texte non détecté, utilisation de l'OCR...")
        images = convert_from_path(pdf_path)
        for page_image in images:
            text += pytesseract.image_to_string(page_image, lang='fra') + "\n"

    return text

# Exemple d'utilisation
pdf_file = "document.pdf"
extracted_text = extract_text_from_pdf(pdf_file)

# Sauvegarder le texte dans un fichier
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

print("Extraction terminée !")
