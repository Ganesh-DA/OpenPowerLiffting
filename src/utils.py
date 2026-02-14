import joblib
import pandas as pd
import streamlit as st
import config


@st.cache_resource
def load_model_and_features():
    """Load and cache the trained model and feature names."""
    model = joblib.load(config.MODEL_FILE)
    features = joblib.load(config.FEATURES_FILE)
    return model, features


def prepare_input_df(features, age: int, weight: float, sex: str, equip: str) -> pd.DataFrame:
    """Create a single-row DataFrame matching the training features.

    This avoids creating a large temporary DataFrame repeatedly in the app.
    """
    # Create a zero-filled row using the feature names (keeps column order)
    input_df = pd.DataFrame(0, index=[0], columns=features)

    # Basic numeric values
    if 'Age' in input_df.columns:
        input_df.at[0, 'Age'] = age
    if 'BodyweightKg' in input_df.columns:
        input_df.at[0, 'BodyweightKg'] = weight

    # One-hot encoded flags (safe check)
    sex_col = f'Sex_{sex}'
    if sex_col in input_df.columns:
        input_df.at[0, sex_col] = 1

    equip_col = f'Equipment_{equip}'
    if equip_col in input_df.columns:
        input_df.at[0, equip_col] = 1

    return input_df


def predict_lifts(model, input_df: pd.DataFrame):
    """Return prediction array [squat, bench, deadlift]."""
    preds = model.predict(input_df)
    # Ensure we return a 1D array for the first sample
    if preds.ndim == 2 and preds.shape[0] >= 1:
        return preds[0]
    return preds
