import os
import re
from config import RAW_DIR, PROCESSED_DIR

# Ensure the processed directory exists
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Basic text cleaning function
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    text = text.strip()
    return text

# Iterate through all .txt files in raw directory
for filename in os.listdir(RAW_DIR):
    if filename.endswith(".txt"):
        input_path = os.path.join(RAW_DIR, filename)
        output_path = os.path.join(PROCESSED_DIR, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            raw = f.read()

        cleaned = clean_text(raw)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
