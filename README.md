🧠 Braille AI Data Pipeline
Convert Unstructured Text into Structured Braille Corpus




Developed for the Data Engineer (AI Data Specialist) role at Flickdone

📌 Overview
Flickdone creates AI-powered accessibility tools for the visually impaired, helping convert scanned content into structured Braille formats. This project simulates a real-world data pipeline with the following capabilities:

🔹 Collect ➜ 🔍 Extract ➜ 🧹 Clean ➜ 📦 Structure ➜ 🔤 Translate ➜ 🖼️ Annotate (optional)

🧩 Features
📥 Input: Scanned images, PDFs, or web-based content

🔠 OCR Extraction: Using Tesseract, Gemini, or Qwen-VL

🧽 Cleaning: Text normalization and preprocessing

🧾 Structuring: Paragraphs and metadata into machine-readable JSON

⠿ Braille Conversion: English & Hindi support using Liblouis

🖼️ Optional: Annotate tables, diagrams, images

🛠️ Pipeline Stages
<details> <summary><strong>1️⃣ Collect</strong></summary>
Accepts scanned images, OCR-compatible documents, or web content

Store raw files in: data/input/

</details> <details> <summary><strong>2️⃣ Extract & Clean</strong></summary>
Basic OCR via Tesseract

Optional VLMs: Gemini, Qwen-VL

Custom cleaning scripts remove noise and normalize text

</details> <details> <summary><strong>3️⃣ Structure</strong></summary>
Output as structured JSON:

json
Copy
Edit
{
  "id": "page_001",
  "language": "en",
  "paragraphs": [
    { "text": "Sample paragraph 1." },
    { "text": "Sample paragraph 2." }
  ]
}
</details> <details> <summary><strong>4️⃣ Braille Translation</strong></summary>
Converts JSON to Braille using Liblouis

Generates .brf files

Supports English and Hindi Braille

</details> <details> <summary><strong>5️⃣ Optional Annotation</strong></summary>
Manual or AI-based tagging of:

Tables

Figures

Diagrams

Stored as metadata alongside paragraphs

</details>
🎥 Demo Video
Coming soon — Watch the full pipeline in action
(Link placeholder for Vimeo/YouTube)

📁 Project Structure
pgsql
Copy
Edit
braille-ai-pipeline/
├── data/
│   ├── input/                # Raw files
│   └── output/               # Processed and translated content
├── src/
│   ├── collect.py            # Data scraping & file ingestion
│   ├── extract_ocr.py        # OCR & image extraction
│   ├── clean_text.py         # Cleaning & preprocessing
│   ├── structure_json.py     # JSON formatting
│   ├── braille_translate.py  # Braille conversion (Liblouis)
│   └── config.py             # Language & path configs
├── README.md
├── requirements.txt
└── LICENSE
🧪 Sample Input/Output
Type	File
📄 Input	page_001.jpeg
✨ Cleaned	page_001.txt
📦 JSON	page_001.json
⠿ Braille	page_001.brf

🚀 Getting Started
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/jyothir-369/braille-ai-pipeline.git
cd braille-ai-pipeline
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Pipeline
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
See the LICENSE file for full details.

👤 Author
Jyothir Raghavalu Bhogi
📧 jyothirraghavalu369@gmail.com
🔗 LinkedIn
🌐 Portfolio Website

💬 Contact
For feedback, suggestions, or collaboration:
📩 Drop an email or connect on LinkedIn

