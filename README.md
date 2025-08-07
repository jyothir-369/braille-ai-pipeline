🧠 Braille AI Data Pipeline
Convert Unstructured Text into Structured Braille Corpus

A full-fledged data pipeline that transforms scanned or unstructured content into structured English and Hindi Braille using OCR, preprocessing, and Liblouis conversion.

🌐 Website
Coming soon...
Feel free to preview the project via the GitHub repository.

📌 Overview
Braille AI Data Pipeline is designed to empower accessibility by transforming diverse content sources—such as scanned documents, PDFs, and web articles—into structured Braille format. The pipeline mimics a real-world data flow in stages:

mathematica
Copy
Edit
📥 Collect ➜ 🔍 Extract ➜ 🧽 Clean ➜ 📦 Structure ➜ 🔡 Translate ➜ 🖼️ Annotate (optional)
🔧 Features
🖼️ Input: Scanned images, PDFs, and digital text

🔠 OCR Extraction: Powered by Tesseract / Gemini / Qwen-VL

🧽 Cleaning: Text normalization & noise removal

🧾 Structuring: Converts content into machine-readable JSON

⠿ Braille Conversion: English & Hindi support via Liblouis

🖍️ Optional Annotation: Table/image tagging (future scope)

🛠️ Pipeline Stages
Stage	Description
1️⃣ Collect	Ingest scanned files or scrape digital content
2️⃣ Extract & Clean	OCR-based text recognition & cleanup
3️⃣ Structure	Convert into logical sections (JSON format)
4️⃣ Braille Translate	Convert to .brf Braille files
5️⃣ Annotate (Opt.)	Add semantic tags for images/tables (TBD)

🗂 Project Structure
graphql
Copy
Edit
braille-ai-pipeline/
├── data/
│   ├── input/               # Raw files (images, text, etc.)
│   └── output/              # Processed results and Braille files
├── src/
│   ├── collect.py           # Data scraping & ingestion
│   ├── extract_ocr.py       # OCR text extraction
│   ├── clean_text.py        # Text preprocessing & normalization
│   ├── structure_json.py    # Structuring as JSON
│   ├── braille_translate.py # Braille file generation
│   └── config.py            # Language & file path settings
├── requirements.txt
├── README.md
└── LICENSE
🧪 Sample I/O
File Type	Name	Description
🖼️ Input	page_001.jpeg	Scanned document
✨ Cleaned	page_001.txt	Preprocessed text
📦 JSON	page_001.json	Structured content
⠿ Braille	page_001.brf	Final translated Braille file

🚀 Getting Started
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/jyothir-369/braille-ai-pipeline.git
cd braille-ai-pipeline
2️⃣ Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run Pipeline Components
bash
Copy
Edit
python src/collect.py
python src/extract_ocr.py
python src/clean_text.py
python src/structure_json.py
python src/braille_translate.py
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

👤 Author
Jyothir Raghavalu Bhogi
📧 jyothirraghavalu369@gmail.com
🔗 LinkedIn
🌐 Portfolio

💬 Contact
For questions, collaborations, or feature requests, feel free to email me or connect on LinkedIn.

