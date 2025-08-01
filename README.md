
# PDF Heading Structure Extractor (Adobe India Hackathon - 1a)

This Python tool extracts the title and section-wise headings (H1, H2, H3...) from a PDF file by analyzing text characteristics like font size, word count, and punctuation. It outputs the structured outline in JSON format.

---

## 📁 Folder Structure

```

AdobeHackathon/1a/
├── extractor.py         # Main Python script
├── Dockerfile           # Docker setup for containerized execution
├── requirements.txt     # Python dependencies
├── input.pdf

````

---

## 🚀 Quick Start

You can run the project in two ways:

---

## 🐳 Option 1: Run with Docker (Recommended)

### ✅ Step 1: Build the Docker image

From inside the `1a/` folder:

```bash
docker build -t pdf-extractor-image 
````

### ✅ Step 2: Run the container

Make sure your input PDF (e.g., `input.pdf`) is in the same folder. Then run:

**On Linux/macOS:**

```bash
docker run --rm -v $(pwd):/app pdf-extractor-image
```

**On Windows (CMD):**

```cmd
docker run --rm -v %cd%:/app pdf-extractor-image
```

---

## 💻 Option 2: Run Manually (No Docker)

### ✅ Step 1: Create virtual environment (optional but good practice)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On Linux/macOS
```

### ✅ Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Step 3: Run the script

```bash
python extractor.py
```

---

## 📄 Input

Place your PDF file as `input.pdf` in the same directory. The script will attempt to read this file.

---

## 🧾 Output

Console output will show a structured JSON like:

```json
{
    "title": "Executive Summary",
    "outline": [
        {
            "level": "H2",
            "text": "Background and Motivation",
            "page": 2
        },
        {
            "level": "H3",
            "text": "Data Collection",
            "page": 3
        }
    ]
}
