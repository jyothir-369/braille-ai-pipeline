from newspaper import Article
import os
from config import RAW_DIR

# URLs to collect text from
urls = [
    "https://en.wikipedia.org/wiki/Braille",
    "https://en.wikipedia.org/wiki/Louis_Braille"
]

# Create raw directory if it doesn't exist
os.makedirs(RAW_DIR, exist_ok=True)

# Download and save articles as text files
for i, url in enumerate(urls):
    article = Article(url)
    article.download()
    article.parse()
    
    filename = f"doc_{i+1}.txt"
    filepath = os.path.join(RAW_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(article.text)
