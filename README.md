# Multilingual-AI-Image-Captioning-System# 🌍 Multilingual AI Image Captioning System

An advanced deep learning project that automatically generates **human-like captions** for images and **translates** them into multiple languages. This system combines **Computer Vision** and **Natural Language Processing (NLP)** using **CLIP** and **mBART50** models, making visual content accessible to a global audience.

---

## 🚀 Key Features

- 🖼️ **Image Captioning**  
  Generates high-quality captions using a **CLIP-based encoder** and Transformer-based decoder.

- 🌐 **Multilingual Translation**  
  Translates captions into **multiple languages** like French, German, Spanish, and Hindi using **mBART50**.

- 📦 **End-to-End Pipeline**  
  Input an image → Generate English caption → Translate → Output in selected language.

- 💻 **Interactive Web Interface**  
  Upload images and select target language through a **Flask-based web app**.

---

## 📊 Model Architecture

- **Encoder**: [OpenAI CLIP](https://github.com/openai/CLIP) (Pre-trained Vision-Language model)
- **Decoder**: Transformer-based language generator
- **Translation**: HuggingFace [mBART50](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)

---

## 🛠️ Technologies Used

| Component          | Tech Stack                      |
|--------------------|---------------------------------|
| Language           | Python                          |
| Deep Learning      | PyTorch, HuggingFace Transformers |
| Computer Vision    | CLIP (Contrastive Language–Image Pre-training) |
| NLP Translation    | mBART50                         |
| Deployment         | Flask, HTML/CSS (Web UI)        |
| Image Handling     | OpenCV, PIL                     |

---

## 📁 Dataset

- **Image-Caption Training**: [MS COCO](https://cocodataset.org/#home)  
- **Translation Dataset**: mBART50 pretrained multilingual dataset

---

## 🧪 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/multilingual-image-captioning.git
cd multilingual-image-captioning

# 2. Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Download CLIP model and mBART50 from HuggingFace
# (This will happen automatically if using the script)

# 4. Run the Flask app
python app.py
''''
