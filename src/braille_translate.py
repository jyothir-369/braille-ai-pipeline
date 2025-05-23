import subprocess
import json
import os
import logging
import tempfile
import shutil
from pathlib import Path
from config import JSON_OUT, BRAILLE_DIR, LANGUAGE

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Ensure output directory exists
os.makedirs(BRAILLE_DIR, exist_ok=True)

# Define Liblouis table paths
TABLES_DIR = r"C:\Program Files\LibLouis\tables"  # Verified path
TABLE_MAP = {
    "en": "en-us-g2.ctb",  # Use en-ueb-g2.ctb if preferred (both available)
    "hi": "hi-in-g1.utb"
}

# Validate configuration
if not os.path.isdir(JSON_OUT):
    raise ValueError(f"JSON_OUT directory does not exist: {JSON_OUT}")
if LANGUAGE not in TABLE_MAP:
    raise ValueError(f"Unsupported language: {LANGUAGE}")
if not shutil.which("lou_translate"):
    raise EnvironmentError("lou_translate not found in PATH. Is Liblouis installed?")

# Resolve full path to table file
table = os.path.join(TABLES_DIR, TABLE_MAP[LANGUAGE])
if not os.path.isfile(table):
    # Log available .ctb files for debugging
    if os.path.isdir(TABLES_DIR):
        available_tables = [f for f in os.listdir(TABLES_DIR) if f.endswith(".ctb")]
        logging.warning(f"Available tables in {TABLES_DIR}: {available_tables}")
    raise FileNotFoundError(f"Liblouis table not found: {table}")

logging.info(f"Using Liblouis table: {table}")

# Process structured JSON files
for filename in sorted(os.listdir(JSON_OUT)):
    if not filename.endswith(".json"):
        continue

    input_path = Path(JSON_OUT) / filename
    if not input_path.is_file():
        logging.warning(f"Skipping non-file: {filename}")
        continue

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "text" not in data or not isinstance(data["text"], str):
            logging.error(f"'text' field missing or invalid in {filename}")
            continue

        # Create temporary file for Liblouis input
        with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", delete=False) as tmp_in:
            tmp_in.write(data["text"])
            tmp_in.flush()
            tmp_in_path = tmp_in.name

            # Use Liblouis to translate text to Braille
            try:
                # Use shell to redirect input file to lou_translate
                cmd = f'lou_translate -f "{table}" < "{tmp_in_path}"'
                result = subprocess.run(
                    cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=True
                )
                braille = result.stdout
                if not braille.strip():
                    logging.warning(f"No Braille output generated for {filename}")
                    continue

                data["braille"] = braille

            except subprocess.CalledProcessError as e:
                # Log available tables if lou_translate fails
                if os.path.isdir(TABLES_DIR):
                    available_tables = [f for f in os.listdir(TABLES_DIR) if f.endswith(".ctb")]
                    logging.warning(f"Available tables in {TABLES_DIR}: {available_tables}")
                logging.error(f"Liblouis error on {filename}: {e.stderr or e}")
                continue

        # Write updated JSON to output directory
        out_path = os.path.join(BRAILLE_DIR, filename)
        if os.path.exists(out_path):
            logging.warning(f"Overwriting existing file: {out_path}")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logging.info(f"Processed: {filename}")

    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"Error processing {filename}: {e}")
        continue
    finally:
        # Clean up temp file
        try:
            if 'tmp_in_path' in locals() and os.path.exists(tmp_in_path):
                os.unlink(tmp_in_path)
        except Exception as cleanup_error:
            logging.warning(f"Temp file cleanup failed: {cleanup_error}")