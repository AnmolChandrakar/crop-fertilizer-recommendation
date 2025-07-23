import streamlit as st
import pickle
import numpy as np

# Load model, scaler, and crop info
model = pickle.load(open("crop_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
crop_info = pickle.load(open("crop_info.pkl", "rb"))

st.title("🌱 Crop & Fertilizer Recommendation System")

# Input values
N = st.number_input("Nitrogen (N)", 0, 200, 50)
P = st.number_input("Phosphorus (P)", 0, 200, 50)
K = st.number_input("Potassium (K)", 0, 200, 50)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
ph = st.number_input("pH", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

if st.button("Recommend Crop"):
    # Prepare input
    input_data = scaler.transform([[N, P, K, temperature, humidity, ph, rainfall]])
    
    # Predict top 3 crops
    probs = model.predict_proba(input_data)[0]
    crop_labels = model.classes_
    top_indices = np.argsort(probs)[::-1][:3]
    top_crops = [(crop_labels[i], round(probs[i]*100, 2)) for i in top_indices]

    st.subheader("🌾 Top Crop Recommendations:")
    for crop, confidence in top_crops:
        st.write(f"**{crop.capitalize()}** - {confidence}% confidence")
        ideal = crop_info[crop]
        st.write(f"**Ideal Soil for {crop.capitalize()}:** N={ideal['N']}, P={ideal['P']}, K={ideal['K']}")
        st.write(f"**Your Soil:** N={N}, P={P}, K={K}")
        
        # Fertilizer advice
        fert = []
        if N < ideal['N']:
            fert.append(f"Add {ideal['N'] - N:.1f} units of Nitrogen (e.g., Urea)")
        if P < ideal['P']:
            fert.append(f"Add {ideal['P'] - P:.1f} units of Phosphorus (e.g., SSP)")
        if K < ideal['K']:
            fert.append(f"Add {ideal['K'] - K:.1f} units of Potassium (e.g., MOP)")
        if not fert:
            fert.append("Soil NPK levels are optimal for this crop.")
        
        st.write("**Fertilizer Advice:**")
        for f in fert:
            st.write("- " + f)

        # Water requirement
        st.write(f"**Water Requirement:** ~{ideal['rainfall']} mm per season")
        st.markdown("---")
