# 📈 WebP to PDF Converter

A simple web-based app to convert `.webp`, `.png`, `.jpg`, and `.jpeg` images into a single downloadable PDF file.

🚀 Built using Python Flask and Pillow.

## 🌟 Features

- Upload multiple image files (`.webp`, `.png`, `.jpg`, `.jpeg`)
- Convert images into a single PDF (in upload order)
- Auto-downloads the generated PDF
- Temporary uploads auto-cleaned every hour
- Lightweight and simple UI

## 🔧 Installation

### Requirements

- Python 3.8+
- pip

### Setup Instructions

```bash
git clone https://github.com/mrzcx8/convert-webpto-pdf.git
cd convert-webpto-pdf
pip install -r requirements.txt
python main.py
```

Open `http://localhost:81` in your browser.

## 📁 Project Structure

```
.
├── main.py              # Flask app
├── templates/
│   └── index.html       # Frontend page with loading & fallback
├── static/
│   └── uploads/         # Uploaded images (auto-cleaned)
├── output/              # Generated PDFs
└── log.txt              # Session logs
```

## 📸 Screenshot

![Screenshot (4194)](https://github.com/user-attachments/assets/65356f69-17ab-491a-947e-0048dea3242d)


*(Optional: Add a screenshot of your web interface)*

## 🔒 License

This project is licensed under the MIT License.

---

## 🙌 Made with ❤️ by [Mr. Syah](https://kxdevs.khaltrix.com/)
