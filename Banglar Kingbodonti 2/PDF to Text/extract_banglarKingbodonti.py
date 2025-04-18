import pytesseract
from PIL import Image
from pdf2image import convert_from_path

print("Converting PDF to images")
pages = convert_from_path("F:\Otibeguni\Banglar Kingbodonti 2.pdf")

output_filename = "banglar_kingbodonti2.txt"
with open(output_filename, "w", encoding="utf-8") as output_file:
    for i, page in enumerate(pages):
        print(f"OCR on page {i+1}")
        text = pytesseract.image_to_string(page, lang='ben')

 
        output_file.write(f"\n\n---  Page {i+1} ---\n\n")
        output_file.write(text)

        print(f"Added page {i+1} to {output_filename}")

print("Combined text saved in one file.")
