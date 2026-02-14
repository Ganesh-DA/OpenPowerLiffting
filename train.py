# train.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import config

def train_model():
    print("Loading datasets...")
    meets = pd.read_csv(config.MEETS_DATA)
    lifting = pd.read_csv(config.LIFTING_DATA, low_memory=False)
    
    # 1. Merge the files
    df = pd.merge(lifting, meets[['MeetID', 'Federation']], on='MeetID', how='left')

    # 2. Clean Data
    df = df.dropna(subset=config.TARGETS + ['BodyweightKg', 'Equipment']).copy()
    df['Age'] = df['Age'].fillna(df['Age'].median())

    # 3. Handle Text Columns (Encoding)
    top_feds = df['Federation'].value_counts().nlargest(5).index
    df['Federation'] = df['Federation'].apply(lambda x: x if x in top_feds else 'Other')
    df_encoded = pd.get_dummies(df, columns=['Sex', 'Equipment', 'Federation'], drop_first=True)
    
    # 4. Define Features
    feature_cols = ['Age', 'BodyweightKg'] + [col for col in df_encoded.columns if any(p in col for p in ['Sex_', 'Equipment_', 'Federation_'])]
    X = df_encoded[feature_cols]
    y = df_encoded[config.TARGETS]

    # 5. Train
    print(f"Training on {config.SAMPLE_SIZE} samples...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
    model.fit(X_train.head(config.SAMPLE_SIZE), y_train.head(config.SAMPLE_SIZE))

    # 6. Save
    joblib.dump(model, config.MODEL_FILE)
    joblib.dump(feature_cols, config.FEATURESk_FILE)
    print("Success! Model and Features saved.")

if __name__ == "__main__":
    train_model()