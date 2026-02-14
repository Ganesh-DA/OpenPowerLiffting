# config.py
# File paths for data and saved models
MEETS_DATA = 'data/meets.csv'
LIFTING_DATA = 'data/openpowerlifting.csv'

MODEL_FILE = 'models/powerlifting_model.pkl'
FEATURES_FILE = 'models/feature_names.pkl'

# Training settings
SAMPLE_SIZE = 50000  # Number of rows to train on (increase for more accuracy)
TARGETS = ['BestSquatKg', 'BestBenchKg', 'BestDeadliftKg']
