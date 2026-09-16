# 🥔 Potato Leaf Disease Classifier

An end-to-end deep learning web application for automated detection and classification of potato leaf diseases using TensorFlow, Keras, and Flask.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Flask](https://img.shields.io/badge/Flask-3.x-green.svg)
![Validation Accuracy](https://img.shields.io/badge/Model%20Accuracy-97.67%25-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Model Information](#-model-information)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [API Reference](#-api-reference)
- [License](#-license)

---

## 🌟 Overview

Potato crops are highly vulnerable to fungal diseases such as **Early Blight** and **Late Blight**, which can destroy entire yields if not identified early. 

This application provides a fast, user-friendly interface for farmers, researchers, and agronomists to upload leaf images and instantly receive accurate disease diagnoses along with detailed class-wise probability breakdowns.

---

## ✨ Key Features

- 🎯 **High Accuracy Inference:** Powered by a Convolutional Neural Network (CNN) trained with 97.67% validation accuracy.
- ⚡ **Instant Analysis:** Fast REST API response time returning diagnosis and class confidence percentages.
- 📊 **Probability Breakdown:** Visual progress bars displaying prediction confidence across all target classes.
- 🖼️ **Interactive UI:** Supports image upload via drag-and-drop or file selector with instant image preview.
- 🔒 **Local & Private:** Runs completely offline on your local environment without uploading images to third-party servers.

---

## 🛠️ Tech Stack

- **Backend Framework:** [Flask](https://flask.palletsprojects.com/) (Python)
- **Deep Learning Framework:** [TensorFlow](https://www.tensorflow.org/) / Keras
- **Image Processing:** [Pillow (PIL)](https://python-pillow.org/) & [NumPy](https://numpy.org/)
- **Frontend UI:** HTML5, CSS3, JavaScript (Fetch API)

---

## 📁 Project Structure

```text
Potato-Plant-Disease-Detection-Based-On-Leaf-Image/
│
├── model.h5              # Trained Keras/TensorFlow model file
├── app.py                # Flask server script (API & routes)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── index.html        # Web dashboard interface
```

---

## 🧪 Model Information

| Parameter | Details |
| :--- | :--- |
| **Model Type** | Convolutional Neural Network (CNN) |
| **Input Shape** | `(255, 255, 3)` |
| **Normalization** | Pixel values scaled by `1 / 255.0` |
| **Validation Accuracy** | **97.67%** |
| **Target Classes** | 1. `Potato___Early_blight`<br>2. `Potato___Late_blight`<br>3. `Potato___healthy` |

---

## 🚀 Installation & Setup

### Prerequisites
Make sure you have **Python 3.8 or higher** installed on your machine. You can check your version by running:
```bash
python --version
```

### 1. Clone or Download the Repository
Extract or place all files into a directory named `potato_disease_app`.

### 2. Prepare the Model File
Place your trained model file (`model.h5`) directly inside the root `potato_disease_app/` folder.

### 3. Install Dependencies
Run the following command in your terminal to install all required Python libraries:
```bash
pip install flask tensorflow pillow numpy
```

---

## 💻 Usage Guide

### 1. Navigate to the folder
Open your command prompt or terminal and use the cd command to navigate to the folder you just created:
```bash
cd path/..../potato_disease_app
```

### 2. Install dependencies
Run the following command to install the required Python libraries:
```bash
pip install flask tensorflow pillow numpy
```
```bash
pip install -r requirements.txt
```

### 3. Launch the Server
Navigate to the project folder and start the Flask application:
```bash
python app.py
```

### 4. Open the Web Application
Open your web browser and navigate to:
```text
http://127.0.0.1:5000
```

### 5. Diagnose Leaf Images
1. Click on the upload zone or drag and drop a potato leaf image (`.jpg`, `.png`, `.jpeg`).
2. Click **Analyze Disease**.
3. View the predicted class label along with individual percentage scores for all classes.

---

## 📡 API Reference

### POST `/predict`

Uploads an image file for classification.

#### Request Header
`Content-Type: multipart/form-data`

#### Request Parameters
| Field | Type | Description |
| :--- | :--- | :--- |
| `file` | File (`image/*`) | Leaf image file to analyze |

#### Response Example (`200 OK`)
```json
{
  "success": true,
  "prediction": "Potato Early Blight",
  "confidence": 98.45,
  "probabilities": {
    "Potato Early Blight": 98.45,
    "Potato Healthy": 0.12,
    "Potato Late Blight": 1.43
  },
  "model_accuracy": 97.67
}
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
