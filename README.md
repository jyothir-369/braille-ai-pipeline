# 🧠 Braille AI Data Pipeline | Flickdone Assessment

This repository contains the code and demo for a data engineering pipeline designed to convert unstructured text data into a structured, AI-trainable dataset for Braille translation. Developed for the **Data Engineer (AI Data Specialist)** role at **Flickdone**.

---

## 📌 Overview

Flickdone develops AI systems to make digital and printed content accessible to the visually impaired. This pipeline:
- Collects unstructured text data (scanned pages, OCR-compatible images, or web content)
- Extracts and cleans text using OCR tools (Tesseract & Vision-Language Models like Gemini or Qwen VL)
- Structures output into JSON with paragraph-aligned content and metadata
- Translates text into Braille using **Liblouis**
- (Optional) Annotates visual elements like tables or diagrams

---

## 🛠️ Pipeline Stages

### 1. **Collect**
- Sources: Scanned pages and online text content
- Sample data stored in `data/`

### 2. **Extract and Clean**
- Uses `Tesseract OCR` for basic extraction
- Supports advanced VLMs (e.g., Gemini/Qwen-VL)
- Normalizes and cleans text using custom Python scripts

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

### 4. **Braille Translation**
- Uses Liblouis to generate a parallel Braille corpus
- Supports English and Hindi

### 5. **Optional Annotation**
- Manual or AI-assisted annotation for images, tables, or diagrams
- Added as metadata

---

## 📽️ Demo Video
Watch the demo showcasing the complete pipeline:  
🔗 [Watch on Vimeo](https://vimeo.com/your-video-link)

---

## 📁 Project Structure

```bash
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
bash

Copy
git clone https://github.com/yourusername/braille-ai-pipeline.git
cd braille-ai-pipeline
Install dependencies:
bash

Copy
pip install -r requirements.txt
Run the pipeline:
bash

Copy
python src/collect.py
python src/extract_ocr.py
python src/clean_text.py
python src/structure_json.py
python src/braille_translate.py
🧾 License
Licensed under the MIT License. See the LICENSE file for details.

👨‍💻 Author
Jyothir Raghavalu Bhogi

📧 Email: jyothirraghavalu369@gmail.com

🔗 LinkedIn: linkedin.com/in/jyothir-raghavalu-bhogi-059500252

🌐 Portfolio: https://jyothir-369.github.io/BJR/

📬 Contact
For questions or collaboration, reach out via email or LinkedIn.

text

Copy

### Specific Fixes Applied
1. **Proper Code Block Formatting**:
   - Added ```bash to open each `bash` code block and ``` to close them, ensuring commands like `git clone` and `pip install` are correctly rendered as code.
   - Removed stray "Copy" text and ensured no non-code text is inside code blocks.
2. **Consistent List Structure**:
   - Formatted "4. Braille Translation" and "5. Optional Annotation" as proper Markdown headers (###) with bullet points for clarity.
   - Ensured consistent indentation and spacing for bullet points and sub-items.
3. **Removed Redundant Commentary**:
   - Excluded the "Fixes and Improvements Made" section and "Additional Notes" from the README, as they appear to be meta-commentary not intended for the final GitHub README. These can be documented separately if needed.
4. **Corrected Links**:
   - Ensured the Vimeo link is formatted as `[Watch on Vimeo](https://vimeo.com/your-video-link)` for proper rendering. Replace `your-video-link` with the actual Vimeo URL.
5. **Section Separators**:
   - Added `---` separators to improve readability and separate sections visually.
6. **Proper Author and Contact Formatting**:
   - Formatted the author and contact sections with bold text for the name and proper Markdown link syntax for email, LinkedIn, and portfolio.

### Why This Fixes the Red Color
- The red highlighting occurs when GitHub’s Markdown parser encounters unclosed code blocks or mixed content (e.g., plain text inside a code block). By ensuring each `bash` block is properly opened (```bash) and closed (```), and by keeping non-code text (like "Install dependencies") outside code blocks, the parser correctly interprets the content.
- The consistent use of Markdown headers and lists prevents structural errors that could confuse the renderer.

### Additional Recommendations
- **Verify on GitHub**: After updating your README with this content, check the rendered view on GitHub to confirm no red highlighting remains. If any issues persist, it may be due to additional unclosed blocks earlier in the file.
- **Add Missing Files**: If you need a `requirements.txt` or `.gitignore`, here’s a quick example for `requirements.txt`:
  ```text
  pytesseract==0.3.10
  liblouis==3.24.0
  requests==2.31.0
And for .gitignore:

text

Copy
data/input/*
data/output/*
__pycache__/
*.pyc
Update Vimeo Link: Replace https://vimeo.com/your-video-link with the actual video URL.
Chart Visualization: If you want a visual representation of the pipeline stages (e.g., a flowchart), I can generate a Chart.js chart. For example, a bar chart showing the stages’ sequence. Let me know if you’d like this.
Push to GitHub: If you need help pushing this to GitHub, run:
bash

Copy
git add README.md
git commit -m "Update README with proper formatting"
git push origin mainusing Chart.js.

Let me know if you need further refinements or additional files!
