import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title = "Fertilizer Prediction Model")
st.title("Optimal Fertilizer Prediction")
st.write("**Enter the values in the given range for better fertilizer prediction.**")

model = pickle.load(open('fertilizer_pred_model.pkl', 'rb'))
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: green; !important;
} 
</style>
""", unsafe_allow_html = True)

col1, col2 = st.columns(2)
with col1:
    temperature = st.number_input("Enter **temperature** in °C (25-38)")
with col2:
    humidity = st.number_input("Enter **humidity** in % (50-72)")

col3, col4 = st.columns(2)
with col3:
    moisture = st.number_input("Enter **moisture** in % (25-65)")
with col4:
    soil_type = st.selectbox("Select the **soil_type**", ['black', 'clayey', 'loamy', 'red', 'sandy'])
    soil_map = {'black': 0, 'clayey': 1, 'loamy': 2, 'red': 3, 'sandy': 4}
    soil_type = soil_map[soil_type]

col5, col6 = st.columns(2)
with col5:
    crop_type = st.selectbox("Select the **crop_type**", ['barely', 'cotton', 'ground nuts', 'maize',
                                                          'millets', 'oil seeds', 'paddy', 'pulses', 'sugarcane',
                                                          'tobacco', 'wheat'])
    crop_map = {'barely': 0, 'cotton': 1, 'ground nuts': 2, 'maize': 3, 'millets': 4, 'oil seeds': 5,
                'paddy': 6, 'pulses': 7, 'sugarcane': 8, 'tobacco': 9, 'wheat': 10}
    crop_type = crop_map[crop_type]

with col6:
    nitrogen = st.number_input("Enter **nitrogen** content (4-42)")

col7, col8 = st.columns(2)
with col7:
    potassium = st.number_input("Enter **potassium** content (0-19)")
with col8:
    phosphorous = st.number_input("Enter **phosphorous** content (0-42)")

fertilizer_map = {
    0: "10-26-26",
    1: "14-35-14",
    2: "17-17-17",
    3: "20-20",
    4: "28-28",
    5: "DAP",
    6: "Urea"
}

fertilizer_suggestions = {
    "10-26-26": "Balanced fertilizer, good for initial growth stages of most crops.",
    "14-35-14": "High phosphorus fertilizer, ideal for root development and early growth.",
    "17-17-17": "All-purpose fertilizer, suitable for most soils and crops.",
    "20-20": "Promotes balanced growth; best for vegetative and flowering stages.",
    "28-28": "High nutrient content for soils deficient in NPK.",
    "DAP": "Apply at sowing time for better root growth.",
    "Urea": "Use during vegetative growth for a nitrogen boost."
}

if st.button("Predict"):
    if temperature == 0 or humidity == 0 or moisture == 0 or nitrogen == 0 or potassium == 0 or phosphorous == 0:
        st.warning("⚠ Please enter all the input values before predicting.")
    else:
        input_values = np.array(
            [temperature / 100, humidity / 100, moisture / 100, soil_type, crop_type, nitrogen / 100, potassium / 100,
             phosphorous / 100])
        input_values = input_values.reshape(1, -1)

        prediction = model.predict(input_values)
        predicted_fertilizer = fertilizer_map[int(prediction[0])]

        st.markdown(f'<p class="big-font">Recommended Fertilizer: {predicted_fertilizer}</p>', unsafe_allow_html = True)
        st.info(f"💡 Suggestion: {fertilizer_suggestions[predicted_fertilizer]}")