{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0aeae97e-d249-46bb-9e89-962f27d7b65c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import joblib\n",
    "\n",
    "# Load model\n",
    "model = joblib.load(\"heart_disease_model.pkl\")\n",
    "\n",
    "st.title(\"❤️ Heart Disease Prediction App\")\n",
    "\n",
    "st.write(\"Enter patient details:\")\n",
    "\n",
    "age = st.slider(\"Age\", 20, 80, 50)\n",
    "sex = st.selectbox(\"Sex\", [\"Male\", \"Female\"])\n",
    "cp = st.selectbox(\"Chest Pain Type\", [0,1,2,3])\n",
    "trestbps = st.slider(\"Resting Blood Pressure\", 90, 200, 120)\n",
    "chol = st.slider(\"Cholesterol\", 100, 400, 200)\n",
    "fbs = st.selectbox(\"Fasting Blood Sugar > 120\", [0,1])\n",
    "restecg = st.selectbox(\"Rest ECG\", [0,1,2])\n",
    "thalach = st.slider(\"Max Heart Rate\", 70, 210, 150)\n",
    "exang = st.selectbox(\"Exercise Induced Angina\", [0,1])\n",
    "oldpeak = st.slider(\"Oldpeak\", 0.0, 6.0, 1.0)\n",
    "slope = st.selectbox(\"Slope\", [0,1,2])\n",
    "ca = st.selectbox(\"Number of Vessels\", [0,1,2,3,4])\n",
    "thal = st.selectbox(\"Thalassemia\", [1,2,3])\n",
    "\n",
    "sex = 1 if sex == \"Male\" else 0\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    data = np.array([[age, sex, cp, trestbps, chol, fbs,\n",
    "                      restecg, thalach, exang, oldpeak,\n",
    "                      slope, ca, thal]])\n",
    "\n",
    "    prediction = model.predict(data)[0]\n",
    "\n",
    "    if prediction == 1:\n",
    "        st.error(\"⚠️ High Risk of Heart Disease\")\n",
    "    else:\n",
    "        st.success(\"✅ Low Risk of Heart Disease\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.11 (niw)",
   "language": "python",
   "name": "niw"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
