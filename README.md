# BraillePrep: ETL Pipeline for Braille AI

This project builds a simplified data pipeline to prepare AI-trainable text-Braille pairs from unstructured content. Targeted for Flickdone's accessibility tech.

## Components
- Collect web content (Wikipedia, etc.)
- OCR extraction (Tesseract)
- Text cleaning
- Structure into JSON format
- Translate to Braille using Liblouis

## Setup
```bash
pip install -r requirements.txt
sudo apt install liblouis-bin tesseract-ocr
