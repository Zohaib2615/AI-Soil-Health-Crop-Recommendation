import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AI Crop Recommendation",
    page_icon="🌱",
    layout="centered"
)

# Load trained ML model
model = pickle.load(open("crop_recommendation_model.pkl", "rb"))

# App Title
st.title("🌱 AI-Based Soil Health & Crop Recommendation System")
st.write(
    "This web application recommends the most suitable crop based on soil nutrients "
    "and climate parameters using a Machine Learning model."
)

st.divider()

# Input Section
st.subheader("Enter Soil & Climate Parameters")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=50)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=150, value=50)
    K = st.number_input("Potassium (K)", min_value=0, max_value=150, value=50)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)

with col2:
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0)

st.divider()

# Prediction Button
if st.button("🌾 Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")

st.divider()

# Footer / Team Credit
st.caption(
    "Developed by a team of four | C-DAC – AI & Data Science using Python"
)
