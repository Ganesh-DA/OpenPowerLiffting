# 🏋️‍♂️ Powerlifting Strength AI Predictor

A machine learning-powered Streamlit application that predicts your potential Squat, Bench Press, and Deadlift poundages based on global competition data from OpenPowerlifting.

## 🎯 Features

- **AI-Powered Predictions**: Uses trained machine learning model to estimate your lifting potential
- **Personalized Results**: Input your age, bodyweight, sex, and equipment type for accurate predictions
- **Multiple Metrics**: Predicts Squat, Bench Press, and Deadlift separately
- **Total Strength Score**: Calculates your predicted total (all three lifts combined)
- **Visual Insights**: Bar charts to visualize your predicted lifts
- **Interactive Interface**: Easy-to-use Streamlit web interface

## 📋 Project Structure

```
├── app.py                      # Streamlit web application
├── train.py                    # Model training script
├── predict.py                  # Prediction module
├── config.py                   # Configuration settings
├── powerlifting_model.pkl      # Trained ML model
├── feature_names.pkl           # Feature names for predictions
├── openpowerlifting.csv        # Main competition dataset
├── meets.csv                   # Meets/competitions data
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ganesh-DA/OpenPowerLiffting.git
   cd OpenPowerLiffting
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

The app will open in your default browser at `http://localhost:8501`

## 📊 How It Works

### Training the Model
```bash
python train.py
```
This script:
- Loads OpenPowerlifting competition data
- Preprocesses and engineers features
- Trains a machine learning model
- Saves the model and features to `.pkl` files

### Making Predictions
1. Launch the app: `streamlit run app.py`
2. Use the sidebar to input your information:
   - **Age**: Your current age (14-90 years)
   - **Bodyweight**: Your weight in kilograms
   - **Sex**: Male (M) or Female (F)
   - **Equipment**: Raw, Wraps, Single-ply, or Multi-ply
3. Click "Predict My Strength"
4. View your predictions and strength profile

## 📦 Requirements

```
streamlit>=1.28.0
pandas>=2.0.0
scikit-learn>=1.3.0
joblib>=1.3.0
```

Install all with:
```bash
pip install streamlit pandas scikit-learn joblib
```

## 📈 Data Source

- **OpenPowerlifting**: International powerlifting competition database
  - 400,000+ competition records
  - Multiple lifting federations
  - Global competitor data
- **Meets Data**: Competition/event information

## 🎓 What You'll Learn

- Machine Learning model training with scikit-learn
- Feature engineering from competition data
- Streamlit for interactive web applications
- Data preprocessing and analysis with pandas
- Model serialization with joblib

## 💡 Model Details

- **Algorithm**: Regression model (predicts continuous lifting values)
- **Features**: Age, Bodyweight, Sex, Equipment type
- **Target Variables**: Squat, Bench Press, Deadlift (kg)
- **Training Data**: 400,000+ actual competition lifts
- **Accuracy**: Based on real-world competition standards

## 🔄 Model Training

The model is trained on actual competition data, meaning predictions reflect what real athletes achieve at international powerlifting competitions. Results vary based on:
- Your training experience
- Genetic factors
- Individual technique
- Current training status

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

Suggestions:
- Add more demographic features
- Implement different ML algorithms
- Create strength standard comparison
- Add historical progress tracking

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Ganesh-DA**
- GitHub: [@Ganesh-DA](https://github.com/Ganesh-DA)
- Email: ganeshshimpi330@gmail.com
