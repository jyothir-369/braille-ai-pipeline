import pytesseract
from PIL import Image
import os
from config import RAW_DIR, PROCESSED_DIR

# Ensure output directory exists
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Process image files for OCR extraction
for filename in os.listdir(RAW_DIR):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(RAW_DIR, filename)
        image = Image.open(image_path)

        # Extract text with Tesseract OCR (English)
        text = pytesseract.image_to_string(image, lang="eng")

        # Prepare output text filename
        out_file = os.path.join(PROCESSED_DIR, filename.rsplit(".", 1)[0] + ".txt")

        # Save extracted text
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(text)
