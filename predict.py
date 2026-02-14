# predict.py
import joblib
import pandas as pd
import config

def predict_ui():
    # Load the trained brains
    try:
        model = joblib.load(config.MODEL_FILE)
        features = joblib.load(config.FEATURES_FILE)
    except:
        print("Error: Model files not found. Run train.py first!")
        return

    print("\n--- Powerlifting Strength Predictor ---")
    age = float(input("Enter Age: "))
    weight = float(input("Enter Bodyweight (kg): "))
    sex = input("Enter Sex (M/F): ").upper()
    equip = input("Enter Equipment (Raw/Wraps/Single-ply): ")

    # Create input row
    input_data = pd.DataFrame(0, index=[0], columns=features)
    input_data['Age'] = age
    input_data['BodyweightKg'] = weight
    
    if f'Sex_{sex}' in features: input_data[f'Sex_{sex}'] = 1
    if f'Equipment_{equip}' in features: input_data[f'Equipment_{equip}'] = 1
    
    # Predict
    preds = model.predict(input_data)[0]
    
    print(f"\nResults for {weight}kg {sex}:")
    print(f"Estimated Squat:    {preds[0]:.2f} kg")
    print(f"Estimated Bench:    {preds[1]:.2f} kg")
    print(f"Estimated Deadlift: {preds[2]:.2f} kg")
    print(f"Estimated Total:    {sum(preds):.2f} kg")

if __name__ == "__main__":
    predict_ui()