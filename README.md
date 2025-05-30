# 🧠 Braille AI Data Pipeline | Flickdone Assessment

This repository contains the code and demo for a data engineering pipeline designed to convert unstructured text data into a structured, AI-trainable dataset for Braille translation. This was developed as part of the assessment task for the **Data Engineer (AI Data Specialist)** role at **Flickdone**.

---

## 📌 Overview

Flickdone develops AI systems to make digital and printed content accessible to the visually impaired. This project simulates a real-world data pipeline that:

- Collects unstructured text data (scanned pages, OCR-compatible images, or web content)
- Extracts and cleans text using OCR tools (Tesseract & Vision-Language Models like Gemini or Qwen VL)
- Structures the output into JSON with paragraph-aligned content and metadata
- Translates text into Braille using open-source libraries like **Liblouis**
- (Optional) Annotates visual elements like tables or diagrams

---

## 🛠️ Pipeline Stages

### 1. **Collect**
- Sources include scanned pages and online text content.
- Sample data is stored in `data/`.

### 2. **Extract and Clean**
- Uses `Tesseract OCR` for basic extraction.
- Advanced VLM support (e.g., Gemini/Qwen-VL) is pluggable.
- Text is normalized and cleaned using custom Python scripts.

### 3. **Structure**
- Converts extracted text into structured JSON format:

```json
{
  "id": "page_001",
  "language": "en",
  "paragraphs": [
    {"text": "Sample paragraph 1."},
    {"text": "Sample paragraph 2."}
  ]
}
4. Braille Translation
Uses Liblouis to generate a parallel Braille corpus.

Supports both English and Hindi.

5. Optional Annotation
Manual or AI-assisted annotation for images, tables, or diagrams.

Added as metadata to the structured JSON.

📽️ Demo Video
Watch the demo showcasing the complete pipeline:
🔗 Watch on Vimeo

📁 Project Structure
graphql
Copy
Edit
├── data/
│   ├── input/                # Raw unstructured files
│   └── output/               # Structured and translated outputs
├── src/
│   ├── collect.py            # Web scraping and document fetching
│   ├── extract_ocr.py        # OCR extraction
│   ├── clean_text.py         # Text normalization and preprocessing
│   ├── structure_json.py     # JSON structuring
│   ├── braille_translate.py  # Liblouis integration
│   └── config.py             # Path and language configuration
├── README.md
└── requirements.txt
🧪 Sample Input/Output
Input:
Scanned page image (e.g., page_001.jpeg)

Output:

Cleaned text: page_001.txt

JSON structured data: page_001.json

Braille text: page_001.brf

🚀 How to Run
1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/jyothir-369/braille-ai-pipeline.git
cd braille-ai-pipeline
2. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Run the pipeline:
bash
Copy
Edit
python src/collect.py
python src/extract_ocr.py
python src/clean_text.py
python src/structure_json.py
python src/braille_translate.py
🧾 License
This project is licensed under the MIT License. See the LICENSE file for details.

👨‍💻 Author
Jyothir Raghavalu Bhogi
📧 Email: jyothirraghavalu369@gmail.com
🔗 LinkedIn: linkedin.com/in/jyothir-raghavalu-bhogi-059500252
🌐 Portfolio: https://jyothir-369.github.io/BJR/

📬 Contact
For questions or collaboration inquiries, feel free to reach out via email or LinkedIn.

yaml
Copy
Edit

---

Let me know if you'd like this automatically pushed to your GitHub repo or need a `.gitignore` or `requirements.txt` generated as well.







