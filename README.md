# 🎙️ Voice Gender Detection API

<html>
  <p align="center">
    <img src="https://img.shields.io/badge/Flask-API-blue?logo=flask" />
    <img src="https://img.shields.io/badge/MongoDB-Database-green?logo=mongodb" />
    <img src="https://img.shields.io/badge/HuggingFace-Transformer-orange?logo=huggingface" />
    <img src="https://img.shields.io/badge/PyTorch-2.0-lightblue?logo=pytorch" />
  </p>
</html>

A lightweight Flask API for detecting gender from voice (`.wav`) files using the pretrained model from HuggingFace:  
👉 [JaesungHuh/voice-gender-classifier](https://huggingface.co/JaesungHuh/voice-gender-classifier)

All requests are logged into **MongoDB** with:
- File Number (Unix Timestamp)
- Audio Filename
- Date (MM/DD/YYYY)
- Time (HH:MM:SS)
- Gender Classification Result

---

## 🚀 Features

- 📁 Upload `.wav` files via POST request
- 🤖 Pretrained `ECAPA_gender` model used for inference
- 📦 Records saved in MongoDB
- 🧪 REST API endpoint: `/predict`
- 🔧 Dockerized deployment (see below)
- 🧰 NoSQL backend (MongoDB via `pymongo`)

---

## 📁 Project Structure

        voice-gender-api/
        │
        ├── app/
        │ ├── api.py # Flask API logic
        │ ├── db.py # MongoDB handler
        │ ├── gender_model.py # Model inference logic
        │
        ├── uploads/ # Directory for uploaded audio files
        │
        ├── voice-gender-classifier/ # Cloned from HuggingFace repo
        │ └── ECAPA_model.py # Model definition
        │
        ├── requirements.txt
        ├── Dockerfile
        ├── docker-compose.yml
        └── README.md

---

## 🛠️ Setup Without Docker

### 1. Clone Repository & Create Virtual Environments

```bash
git clone https://github.com/YOUR_USERNAME/voice-gender-api.git
cd voice-gender-api
python -m venv envGenClass
.\envGenClass\Scripts\activate  # For Windows
