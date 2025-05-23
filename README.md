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
Here are the issues causing this:

The JSON block is opened with triple backticks (```json) but not properly closed before continuing to normal text.

After the JSON block, the next lines (starting with 4. Braille Translation) are considered part of the JSON or code block because of missing closure.

Also, the markdown parser expects consistent formatting, so mixing JSON with plain text without closing the code block breaks rendering.

How to fix it:
Make sure to close the JSON code block with triple backticks before continuing with the numbered list.

For numbered lists and paragraphs, do not indent or place inside code blocks.

Use triple backticks only around code snippets or blocks.

Fixed snippet example:
markdown
Copy
Edit
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
Braille Translation
Uses Liblouis to generate a parallel Braille corpus.

Supports both English and Hindi.

Optional Annotation
Manual or AI-assisted annotation for images, tables, or diagrams can be added as metadata.

yaml
Copy
Edit

Notice how:

- The JSON block is wrapped between triple backticks ```json ... ```
- After closing the JSON block, normal text continues outside any code block.

---

### Summary:

Wherever you use code blocks (JSON, bash, yaml, etc.), always:

- Open with ``` and optionally a language tag like ```json
- Close with ```
- Then write normal text **outside** those blocks

---

If you want, I can help you fix your entire markdown snippet to render perfectly! Would you like me to do that?






You said:
complete one


ChatGPT said:
Sure! Here’s your entire markdown content fixed so it renders properly without the red color or code formatting issues — with all code blocks correctly opened and closed, and normal text outside code blocks:

markdown
Copy
Edit
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
Manual or AI-assisted annotation for images, tables, or diagrams can be added as metadata.

📽️ Demo Video
Watch the demo showcasing the complete pipeline:

🔗 Watch on Vimeo

📁 Project Structure
bash
Copy
Edit
├── data/
│   ├── input/                # Raw unstructured files
│   └── output/               # Final structured and translated outputs
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

bash
Copy
Edit
git clone https://github.com/yourusername/braille-ai-pipeline.git
cd braille-ai-pipeline
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the pipeline step-by-step:

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

Let me know if you want me to generate a requirements.txt or .gitignore file, or help you push all this to your GitHub repo.

yaml
Copy
Edit

---

This version:

- Properly closes all code blocks (` ``` `) for JSON, bash, etc.
- Ensures numbered and bullet lists are outside code blocks
- Adds some section separators (`---`) for readability
- Formats links properly with markdown syntax

If you want, I can also help you generate example `requirements.txt` or `.gitignore` next!
