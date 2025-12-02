# 🖼️ Multilingual Image Caption Generator with Text-to-Speech 🎤

This project is a Flask-based web application that generates captions for uploaded images in multiple languages, with **text-to-speech** functionality and a **modern UI**. It uses a Vision Encoder-Decoder model for captioning and MarianMT models for translation.

---

## ✨ Features

- Upload any image and get a descriptive caption
- Translate the caption into **10 international languages**
- Listen to the translated caption via **Text-to-Speech (TTS)**
- Clean, modern, responsive UI built with HTML, CSS, and Bootstrap

---

## 🌐 Supported Languages

- English 🇺🇸 *(Default)*
- French 🇫🇷
- German 🇩🇪
- Spanish 🇪🇸
- Japanese 🇯🇵
- Chinese 🇨🇳
- Korean 🇰🇷
- Russian 🇷🇺
- Arabic 🇸🇦
- Portuguese 🇵🇹

*(Note: Hindi is intentionally excluded.)*

---

## 🧠 Models Used

- **Image Captioning:** [`nlpconnect/vit-gpt2-image-captioning`](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)
- **Translation:** [`Helsinki-NLP/opus-mt-<lang1>-<lang2>` models](https://huggingface.co/Helsinki-NLP)
- **Text-to-Speech:** Python `gTTS` (Google Text-to-Speech)

---

## 🛠️ Installation

```bash
git clone https://github.com/srinijakk/multilingual-caption-generator.git
'''

cd multilingual-caption-generator
├── app.py
├── requirements.txt
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   └── caption.html
├── uploads/
│   └── [uploaded_images]
└── README.md
