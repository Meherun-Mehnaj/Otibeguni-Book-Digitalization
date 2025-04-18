import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2
import numpy as np

custom_config = r'--oem 3 --psm 6'  


def preprocess_image(pil_image):
 
    open_cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return Image.fromarray(thresh)

#Convert PDF to images with higher resolution
print("Converting PDF to images with 300 DPI")
pages = convert_from_path("F:\Otibeguni\Banglar Kingbodonti 2.pdf", dpi=300)

output_filename = "BanglarKingbodonti2_2ndTrial.txt"
with open(output_filename, "w", encoding="utf-8") as output_file:
    for i, page in enumerate(pages):
        print(f"🧼 Preprocessing and OCR on page {i+1}")
        processed = preprocess_image(page)
        text = pytesseract.image_to_string(processed, lang='ben', config=custom_config)

        #page marker and text
        output_file.write(f"\n\n---  Page {i+1} ---\n\n")
        output_file.write(text)

        print(f"Page {i+1} added to {output_filename}")

print("All pages saved with improved accuracy.")
