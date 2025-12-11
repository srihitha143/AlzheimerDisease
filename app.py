import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🧠 Alzheimer’s Disease Prediction App")
st.write("Enter patient details to predict the risk of Alzheimer’s Disease.")

# ---- INPUT FEATURES ----
Age = st.number_input("Age", 40, 100, 60)
Gender = st.selectbox("Gender", ["Male", "Female"])
Smoking = st.selectbox("Smoking", ["Yes", "No"])
AlcoholConsumption = st.selectbox("Alcohol Consumption", ["Yes", "No"])
PhysicalActivity = st.selectbox("Physical Activity", ["Low", "Moderate", "High"])
SleepQuality = st.slider("Sleep Quality (1–10)", 1, 10, 5)
CholesterolHDL = st.number_input("HDL Cholesterol", 10, 100, 45)

# Encoding categorical inputs
Gender = 1 if Gender == "Male" else 0
Smoking = 1 if Smoking == "Yes" else 0
AlcoholConsumption = 1 if AlcoholConsumption == "Yes" else 0

PhysicalActivity_map = {"Low": 0, "Moderate": 1, "High": 2}
PhysicalActivity = PhysicalActivity_map[PhysicalActivity]

# Prepare input data for model
input_data = np.array([[Age, Gender, Smoking, AlcoholConsumption,
                        PhysicalActivity, SleepQuality, CholesterolHDL]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ High risk of Alzheimer's Disease")
    else:
        st.success("✅ Low risk of Alzheimer's Disease")
