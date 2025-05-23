🧠 Braille AI Data Pipeline | Flickdone Assessment
This repository contains the code and demo for a data engineering pipeline designed to convert unstructured text data into a structured, AI-trainable dataset for Braille translation. Developed for the Data Engineer (AI Data Specialist) role at Flickdone.

📌 Overview
Flickdone develops AI systems to make digital and printed content accessible to the visually impaired. This pipeline:

Collects unstructured text data (scanned pages, OCR-compatible images, or web content)
Extracts and cleans text using OCR tools (Tesseract & Vision-Language Models like Gemini or Qwen VL)
Structures output into JSON with paragraph-aligned content and metadata
Translates text into Braille using Liblouis
(Optional) Annotates visual elements like tables or diagrams


🛠️ Pipeline Stages
1. Collect

Sources: Scanned pages and online text content
Sample data stored in data/

2. Extract and Clean

Uses Tesseract OCR for basic extraction
Supports advanced VLMs (e.g., Gemini/Qwen-VL)
Normalizes and cleans text using custom Python scripts

3. Structure

Converts extracted text into structured JSON format:

{
  "id": "page_001",
  "language": "en",
  "paragraphs": [
    {"text": "Sample paragraph 1."},
    {"text": "Sample paragraph 2."}
  ]
}

4. Braille Translation

Uses Liblouis to generate a parallel Braille corpus
Supports English and Hindi

5. Optional Annotation

Manual or AI-assisted annotation for images, tables, or diagrams
Added as metadata


📽️ Demo Video
Watch the demo showcasing the complete pipeline:🔗 Watch on Vimeo

📁 Project Structure
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

Input: Scanned page image (e.g., page_001.jpeg)
Output:
Cleaned text: page_001.txt
JSON: page_001.json
Braille text: page_001.brf




🚀 How to Run

Clone the repository:

git clone https://github.com/jyothir-369/braille-ai-pipeline.git
cd braille-ai-pipeline


Install dependencies:

pip install -r requirements.txt


Run the pipeline:

python src/collect.py
python src/extract_ocr.py
python src/clean_text.py
python src/structure_json.py
python src/braille_translate.py


🧾 License
Licensed under the MIT License. See the LICENSE file for details.

👨‍💻 Author
Jyothir Raghavalu Bhogi📧 Email: jyothirraghavalu369@gmail.com🔗 LinkedIn: linkedin.com/in/jyothir-raghavalu-bhogi-059500252🌐 Portfolio: https://jyothir-369.github.io/BJR/

📬 Contact
For questions or collaboration, reach out via email or LinkedIn.
