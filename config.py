# config.py
# File paths for data and saved models
MEETS_DATA = 'meets.csv'
LIFTING_DATA = 'openpowerlifting.csv'

MODEL_FILE = 'powerlifting_model.pkl'
FEATURES_FILE = 'feature_names.pkl'

# Training settings
SAMPLE_SIZE = 50000  # Number of rows to train on (increase for more accuracy)
TARGETS = ['BestSquatKg', 'BestBenchKg', 'BestDeadliftKg']
