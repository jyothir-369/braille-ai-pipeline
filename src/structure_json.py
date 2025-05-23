import os
import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
TEXT_EXTENSION = ".txt"
ID_PREFIX = "doc_"

try:
    from config import PROCESSED_DIR, JSON_OUT, LANGUAGE
except ImportError as e:
    raise ImportError("Config module is missing or incorrectly defined") from e

# Validate configuration
if not os.path.isdir(PROCESSED_DIR):
    raise ValueError(f"PROCESSED_DIR {PROCESSED_DIR} is not a valid directory")
if not LANGUAGE:
    raise ValueError("LANGUAGE is not defined in config")

# Ensure output directory exists
os.makedirs(JSON_OUT, exist_ok=True)

# Convert each cleaned text file into a structured JSON file
for i, entry in enumerate(sorted(os.scandir(PROCESSED_DIR), key=lambda x: x.name)):
    if not entry.is_file() or not entry.name.endswith(TEXT_EXTENSION):
        continue

    file_path = Path(PROCESSED_DIR) / entry.name
    if not file_path.parent.samefile(PROCESSED_DIR):
        logging.warning(f"Skipping invalid path: {entry.name}")
        continue

    try:
        if os.path.getsize(file_path) == 0:
            logging.warning(f"Skipping empty file: {entry.name}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        record = {
            "id": f"{ID_PREFIX}{i+1}",
            "language": LANGUAGE,
            "text": text,
            "braille": None,  # To be filled by braille_translate.py
            "metadata": {
                "source_file": entry.name
            }
        }

        out_path = os.path.join(JSON_OUT, f"{record['id']}.json")
        if os.path.exists(out_path):
            logging.warning(f"Overwriting existing file: {out_path}")

        with open(out_path, "w", encoding="utf-8") as out:
            json.dump(record, out, indent=2, ensure_ascii=False)
        logging.info(f"Processed file: {entry.name} -> {out_path}")

    except (IOError, UnicodeDecodeError) as e:
        logging.error(f"Error processing {entry.name}: {e}")
        continue