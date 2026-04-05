import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("heart_disease_model.pkl")

# App Title
st.title("❤️ Jabed AI Health System")
st.subheader("Heart Disease Risk Assessment")

st.write("Answer a few simple questions about the patient:")

# -------------------------
# INPUTS (USER FRIENDLY)
# -------------------------

# Age
age = st.number_input("Age", min_value=20, max_value=100, value=50)

# Sex
sex_option = st.radio("Gender", ["Male", "Female"])
sex = 1 if sex_option == "Male" else 0

# Chest Pain
cp_option = st.selectbox(
    "Do you experience chest pain?",
    ["No Pain", "Mild Pain", "Moderate Pain", "Severe Pain"]
)

cp_map = {
    "No Pain": 0,
    "Mild Pain": 1,
    "Moderate Pain": 2,
    "Severe Pain": 3
}
cp = cp_map[cp_option]

# Blood Pressure
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)

# Cholesterol
chol = st.number_input("Cholesterol Level", 100, 400, 200)

# Blood Sugar
fbs_option = st.radio("Is fasting blood sugar high (>120)?", ["No", "Yes"])
fbs = 1 if fbs_option == "Yes" else 0

# ECG
restecg_option = st.selectbox(
    "ECG Result",
    ["Normal", "Minor Abnormality", "Severe Abnormality"]
)
restecg_map = {
    "Normal": 0,
    "Minor Abnormality": 1,
    "Severe Abnormality": 2
}
restecg = restecg_map[restecg_option]

# Max Heart Rate
thalach = st.number_input("Maximum Heart Rate Achieved", 70, 210, 150)

# Angina
exang_option = st.radio("Do you feel chest pain during exercise?", ["No", "Yes"])
exang = 1 if exang_option == "Yes" else 0

# Oldpeak
oldpeak = st.slider("ST Depression Level (Oldpeak)", 0.0, 6.0, 1.0)

# Slope
slope_option = st.selectbox(
    "Heart Rate Trend during Exercise",
    ["Normal", "Flat", "Downward"]
)
slope_map = {
    "Normal": 0,
    "Flat": 1,
    "Downward": 2
}
slope = slope_map[slope_option]

# Vessels
ca = st.selectbox("Number of Major Vessels Detected", [0,1,2,3,4])

# Thalassemia
thal_option = st.selectbox(
    "Thalassemia Condition",
    ["Normal", "Fixed Defect", "Reversible Defect"]
)
thal_map = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}
thal = thal_map[thal_option]

# -------------------------
# PREDICTION
# -------------------------

if st.button("🔍 Analyze Risk"):
    data = np.array([[age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak,
                      slope, ca, thal]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.write("---")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease\n\nRisk Level: {probability*100:.2f}%")
    else:
        st.success(f"✅ Low Risk of Heart Disease\n\nRisk Level: {probability*100:.2f}%")