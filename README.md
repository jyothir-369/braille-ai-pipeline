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


4. Braille Translation
Uses Liblouis to generate a parallel Braille corpus
Supports English and Hindi
5. Optional Annotation
Manual or AI-assisted annotation for images, tables, or diagrams
Added as metadata



📽️ Demo Video
Watch the demo showcasing the complete pipeline:

🔗 Watch on Vimeo



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
Jyothir Raghavalu Bhogi

📧 Email: jyothirraghavalu369@gmail.com

🔗 LinkedIn: linkedin.com/in/jyothir-raghavalu-bhogi-059500252

🌐 Portfolio: https://jyothir-369.github.io/BJR/




📬 Contact
For questions or collaboration, reach out via email or LinkedIn.


### Specific Fixes Applied
1. **Proper Code Block Closure**:
   - Ensured all `bash` code blocks are opened with ```bash and closed with ```. For example, the `git clone` and `pip install` commands are now properly enclosed, preventing text like "Copy" or "Install dependencies" from being interpreted as code.
   - Removed stray "Copy" labels and ensured non-code text is outside code blocks.
2. **Consistent List Formatting**:
   - Formatted "4. Braille Translation" and "5. Optional Annotation" as Markdown headers (###) with bullet points for clarity and proper indentation.
   - Ensured the "How to Run" section uses numbered lists with proper Markdown syntax (e.g., `1.`, `2.`) and consistent spacing.
3. **Removed Unintended Commentary**:
   - Excluded the "Fixes and Improvements Made" and "Additional Notes" sections, as they appear to be meta-commentary not meant for the final README. These can be documented separately if needed.
4. **Corrected Links**:
   - Updated the GitHub repository URL to `https://github.com/jyothir-369/braille-ai-pipeline.git` to match your repository.
   - Kept the Vimeo link as a placeholder (`[Watch on Vimeo](https://vimeo.com/your-video-link)`). Replace `your-video-link` with the actual Vimeo URL.
5. **Section Separators**:
   - Added `---` separators between sections for improved readability and visual separation.
6. **Consistent Emoji Usage**:
   - Retained the emoji-based section headers (e.g., 🧠, 📌) to match your original style and enhance visual appeal.

### How to Update Your README
1. **Edit the README on GitHub**:
   - Go to [https://github.com/jyothir-369/braille-ai-pipeline/blob/main/README.md](https://github.com/jyothir-369/braille-ai-pipeline/blob/main/README.md).
   - Click the pencil icon to edit the file.
   - Replace the entire content with the corrected Markdown above.
   - Commit the changes with a message like "Fix Markdown formatting in README".
2. **Verify Rendering**:
   - After committing, check the README on GitHub to ensure no red highlighting remains. The content should render cleanly with proper code blocks, lists, and links.
3. **Update Vimeo Link**:
   - Replace `https://vimeo.com/your-video-link` with the actual Vimeo URL for your demo video.
4. **Local Update (Optional)**:
   - If you’re working locally, update `README.md` with the above content, then push to GitHub:
     ```bash
     git add README.md
     git commit -m "Fix Markdown formatting in README"
     git push origin main
