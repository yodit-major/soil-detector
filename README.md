# 🌱 Soil Detector

A web-based soil classification system built with **Django** and **TensorFlow**. Users can upload a soil image and receive a predicted soil type along with the model's confidence score.

## 📌 Project Overview

Soil Detector uses a deep learning image-classification model to identify soil from images.

The project started as a basic image-analysis application using OpenCV and color-based rules. It was later upgraded to a **TensorFlow deep learning model using MobileNetV2 transfer learning** for more reliable soil classification.

The system currently recognizes five soil types:

* Black Soil
* Cinder Soil
* Laterite Soil
* Peat Soil
* Yellow Soil

## ✨ Features

* 📷 Upload a soil image
* 🤖 Predict the soil type using a trained deep learning model
* 📊 Display prediction confidence
* 🌐 Django-based web interface
* 🧠 MobileNetV2 transfer learning
* 📈 Model evaluation using accuracy, precision, recall, and F1-score

## 🛠️ Technologies

* **Python**
* **Django**
* **TensorFlow / Keras**
* **MobileNetV2**
* **NumPy**
* **Pillow**
* **HTML / CSS**
* **Git & GitHub**

## 🧠 Machine Learning Model

The classifier uses **MobileNetV2**, a pretrained convolutional neural network, as the feature-extraction backbone.

The model was trained using:

* Image resizing: `224 × 224`
* Data augmentation
* Class weighting during initial training
* Transfer learning from ImageNet
* Dropout regularization
* Five output classes

A targeted augmentation experiment was also used to improve recognition of Peat Soil.

## 📊 Model Performance

The current model was evaluated on a separate test set containing **204 images**.

| Metric            |     Result |
| ----------------- | ---------: |
| Test Accuracy     | **95.10%** |
| Macro F1-score    |   **0.93** |
| Weighted F1-score |   **0.95** |

### Per-Class Performance

| Soil Type     | Precision | Recall | F1-score |
| ------------- | --------: | -----: | -------: |
| Black Soil    |      0.99 |   0.98 |     0.99 |
| Cinder Soil   |      1.00 |   0.92 |     0.96 |
| Laterite Soil |      0.79 |   1.00 |     0.88 |
| Peat Soil     |      0.86 |   0.83 |     0.84 |
| Yellow Soil   |      1.00 |   0.93 |     0.96 |

The model's main remaining challenge is distinguishing visually similar **Laterite Soil and Peat Soil** images.

## 📂 Dataset

The model was trained using the **Soil Type Identification** dataset from Roboflow.

The dataset contains the same five soil classes used by this project:

* Black Soil
* Cinder Soil
* Laterite Soil
* Peat Soil
* Yellow Soil

The dataset contains **4,202 images** across training, validation, and test sets.

The dataset is released under the **CC BY 4.0** license.

## 📁 Project Structure

```text
soil-detector/
│
├── classifier/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   └── ...
│
├── config/
│
├── media/
│
├── ml_models/
│
├── venv/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yodit-major/soil-detector.git
cd soil-detector
```

### 2. Create and activate a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Add the trained model

The trained `.keras` model is not included in this repository because the model file is larger than GitHub's standard file-size limit.

Place the trained model inside:

```text
ml_models/
```

The Django application currently expects:

```text
ml_models/best_peat_augmented_model.keras
```

### 5. Run the Django server

```powershell
python manage.py runserver
```

Then open the local development server in your browser.

## 🔬 Model Evaluation

The model was evaluated using a test set that was not used during training.

Evaluation included:

* Test accuracy
* Precision
* Recall
* F1-score
* Confusion matrix
* Real-world image testing through the Django application

The final model achieved **95.10% test accuracy**.

## 🚀 Future Improvements

Possible future improvements include:

* Collecting more real-world soil images
* Improving the distinction between Peat and Laterite Soil
* Testing additional pretrained architectures
* Improving model calibration and confidence estimates
* Deploying the application online
* Adding soil-related recommendations based on classification results
* Expanding the dataset while keeping the current five-class classification target

## 👩🏽‍💻 Author

**Yodit Major**

Computer Science Student | Aspiring Data & Machine Learning Engineer

GitHub: **yodit-major**

---

> This project is part of my journey in learning machine learning, computer vision, and backend web development.
