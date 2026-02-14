import streamlit as st
import pandas as pd
from src.utils import load_model_and_features, prepare_input_df, predict_lifts

# --- PAGE SETUP ---
st.set_page_config(page_title="Powerlifting Predictor", page_icon="🏋️‍♂️")

st.title("🏋️‍♂️ Powerlifting Strength AI")
st.write("Predict your potential Squat, Bench, and Deadlift based on global competition data.")

# --- LOAD MODEL ---
try:
    model, features = load_model_and_features()
except Exception:
    st.error("Model files not found! Please run train.py first.")
    st.stop()

# --- SIDEBAR INPUTS ---
st.sidebar.header("Your Information")
age = st.sidebar.slider("Age", 14, 90, 25)
weight = st.sidebar.number_input("Bodyweight (kg)", min_value=30.0, max_value=250.0, value=80.0)
sex = st.sidebar.selectbox("Sex", ["M", "F"])
equip = st.sidebar.selectbox("Equipment", ["Raw", "Wraps", "Single-ply", "Multi-ply"])

# --- PREDICTION LOGIC ---
if st.sidebar.button("Predict My Strength"):
    # Prepare input using helper (faster and clearer)
    input_df = prepare_input_df(features, age, weight, sex, equip)
    # Predict
    preds = predict_lifts(model, input_df)
    
    # --- DISPLAY RESULTS ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Squat", f"{preds[0]:.1f} kg")
    with col2:
        st.metric("Bench", f"{preds[1]:.1f} kg")
    with col3:
        st.metric("Deadlift", f"{preds[2]:.1f} kg")
        
    st.success(f"**Predicted Total: {sum(preds):.1f} kg**")
    
    # Add a little chart
    chart_data = pd.DataFrame({
        "Lift": ["Squat", "Bench", "Deadlift"],
        "Weight (kg)": [preds[0], preds[1], preds[2]]
    })
    st.bar_chart(data=chart_data, x="Lift", y="Weight (kg)")

else:
    st.info("Adjust the settings on the left and click 'Predict My Strength'")