# app.py
import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('crop_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Fertilizer Recommendation Logic
def recommend_fertilizer(N, P, K):
    fertilizer = []
    if N < 40:
        fertilizer.append("Add Urea (Nitrogen-rich fertilizer)")
    if P < 40:
        fertilizer.append("Add Single Super Phosphate (Phosphorus-rich)")
    if K < 40:
        fertilizer.append("Add Muriate of Potash (Potassium-rich)")
    if not fertilizer:
        fertilizer.append("Soil NPK levels are balanced – no extra fertilizer needed.")
    return fertilizer

# Streamlit UI
st.title("🌱 Crop & Fertilizer Recommendation System")
st.write("Provide soil and weather parameters to get crop suggestions with fertilizer advice.")

N = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=50)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=150, value=50)
K = st.number_input("Potassium (K)", min_value=0, max_value=150, value=50)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0)

if st.button("Recommend"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_data)
    probabilities = model.predict_proba(input_scaled)[0]
    top_indices = np.argsort(probabilities)[::-1][:3]
    top_crops = [(model.classes_[i], round(probabilities[i] * 100, 2)) for i in top_indices]

    st.subheader("🌾 Recommended Crops:")
    for crop, prob in top_crops:
        st.write(f"- **{crop.capitalize()}** ({prob}% confidence)")

    st.subheader("🧪 Fertilizer Advice:")
    for advice in recommend_fertilizer(N, P, K):
        st.write(f"- {advice}")
