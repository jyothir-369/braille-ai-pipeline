# 🧠 Braille AI Data Pipeline  
**Convert Unstructured Text into Structured Braille Corpus**  
![MIT License](https://img.shields.io/badge/license-MIT-green)  
![Python](https://img.shields.io/badge/python-3.8%2B-blue)  
![Status](https://img.shields.io/badge/status-active-brightgreen)

> Developed as part of the **Data Engineer (AI Data Specialist)** assessment for **Flickdone**.

---

## 📌 Overview

Flickdone develops AI systems that make digital and printed content accessible for the visually impaired.  
This repository simulates a **real-world data engineering pipeline** to:

- 🗃️ Collect unstructured textual content (scanned pages, images, or web)
- 🔍 Extract and clean using OCR + Vision-Language Models (Tesseract, Gemini, Qwen-VL)
- 📦 Structure into machine-readable JSON
- 🔤 Translate into Braille using [Liblouis](http://www.liblouis.org/)
- 🖼️ *(Optional)* Annotate tables, diagrams, and images

---

## 🛠️ Pipeline Stages

<details>
<summary><strong>1. Collect</strong></summary>

- Accepts **scanned images**, **OCR-compatible files**, or **web content**
- Store raw files in `data/input/`

</details>

<details>
<summary><strong>2. Extract & Clean</strong></summary>

- Basic OCR with **Tesseract**
- Pluggable advanced extraction via **Gemini** or **Qwen-VL**
- Custom normalization scripts for text preprocessing

</details>

<details>
<summary><strong>3. Structure</strong></summary>

- JSON output format:

```json
{
  "id": "page_001",
  "language": "en",
  "paragraphs": [
    {"text": "Sample paragraph 1."},
    {"text": "Sample paragraph 2."}
  ]
}
</details> <details> <summary><strong>4. Braille Translation</strong></summary>
Uses Liblouis to generate parallel .brf Braille files

Supports English and Hindi translations

</details> <details> <summary><strong>5. Optional Annotation</strong></summary>
Manual or AI-assisted tagging of images, tables, etc.

Included as metadata in JSON

</details>
📽️ Demo Video
🎥 Watch the full pipeline demo on Vimeo (link placeholder)

📁 Project Structure
graphql
Copy
Edit
braille-ai-pipeline/
├── data/
│   ├── input/                # Raw unstructured files
│   └── output/               # Structured and translated outputs
├── src/
│   ├── collect.py            # Document/web scraping
│   ├── extract_ocr.py        # OCR and image text extraction
│   ├── clean_text.py         # Normalization & preprocessing
│   ├── structure_json.py     # JSON formatting
│   ├── braille_translate.py  # Liblouis integration
│   └── config.py             # Configs (paths, language)
├── README.md
├── requirements.txt
└── LICENSE
🧪 Sample I/O
Type	File
📄 Input	page_001.jpeg
✨ Cleaned	page_001.txt
📦 Structured	page_001.json
⠿ Braille	page_001.brf

🚀 Getting Started
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/jyothir-369/braille-ai-pipeline.git
cd braille-ai-pipeline
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Pipeline
bash
Copy
Edit
python src/collect.py
python src/extract_ocr.py
python src/clean_text.py
python src/structure_json.py
python src/braille_translate.py
📜 License
This project is licensed under the MIT License.
See the LICENSE file for details.

👨‍💻 Author
Jyothir Raghavalu Bhogi
📧 jyothirraghavalu369@gmail.com
🔗 LinkedIn
🌐 Portfolio

📬 Contact
For questions, ideas, or collaboration:
👉 Drop an email or connect on LinkedIn.
