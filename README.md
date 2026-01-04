# 🌱 AI-Based Soil Health Analysis & Crop Recommendation System

## 📌 Project Overview
This project is an AI-based web application that analyzes soil health and climate parameters to recommend the most suitable crop.  
The system uses a Machine Learning model trained on agricultural data and is deployed as a web application using Streamlit.

---

## 🎯 Objectives
- Analyze soil nutrients and environmental factors
- Build a Machine Learning model for crop recommendation
- Provide real-time crop recommendations through a web interface
- Support data-driven decision-making in agriculture

---

## 🧠 Technologies Used
- **Programming Language:** Python  
- **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn  
- **Machine Learning Model:** Random Forest Classifier  
- **Web Framework:** Streamlit  
- **Deployment:** Streamlit Community Cloud  

---

## 📊 Dataset Description
The dataset contains soil and climate parameters such as:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

**Target Variable:** Crop Name

The dataset was used only during the training phase.

---

## ⚙️ System Architecture
1. User enters soil and climate parameters
2. Trained ML model processes the input
3. System predicts the most suitable crop
4. Result is displayed on the web interface

---

## 🚀 Machine Learning Workflow
- Data Loading
- Exploratory Data Analysis (EDA)
- Feature Selection
- Train-Test Split (80:20)
- Model Training (Random Forest)
- Model Evaluation (Accuracy, Confusion Matrix, Cross-Validation)
- Model Serialization using Pickle

---

## 📈 Model Performance
- **Training Accuracy:** 100%
- **Testing Accuracy:** ~99.32%
- **Cross-Validation Accuracy:** ~99.45%

These results indicate strong generalization and minimal overfitting.

---

## 🌐 Web Application
The trained model is deployed as a web application using Streamlit.  
Users can input soil and climate values and receive instant crop recommendations.

---

## ▶️ How to Run the Project Locally
1. Clone the repository
2. Install dependencies:
