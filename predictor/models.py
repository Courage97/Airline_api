import os
import joblib
import pandas as pd
from django.db import models

# --- MODEL LOADING ---

# Get the path to the current directory (predictor/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained model
model_path = os.path.join(BASE_DIR, 'xgboost_airline_model_v1.0.joblib')
model = joblib.load(model_path)

# Load expected input column names (used for one-hot encoding alignment)
columns_path = os.path.join(BASE_DIR, 'model_columns.joblib')
model_columns = joblib.load(columns_path)

# --- PREDICTION FUNCTION ---

def predict_passenger_satisfaction(input_data: dict) -> dict:
    """Takes raw input data and returns a prediction + confidence from the trained model."""
    df = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df)
    df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df_encoded)[0]
    confidence = model.predict_proba(df_encoded)[0][1]  # Probability for class 1 (satisfied)

    return {
        "prediction": "satisfied" if prediction == 1 else "dissatisfied",
        "confidence": round(confidence, 2)
    }

# --- PREDICTION LOG MODEL ---

class PredictionLog(models.Model):
    input_data = models.JSONField()  # AI-relevant fields only
    prediction = models.CharField(max_length=20)
    confidence = models.FloatField()

    # Metadata (not used in prediction but helpful for tracking)
    seat_number = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    flight_date = models.DateField(null=True, blank=True)
    flight_number = models.CharField(max_length=20, null=True, blank=True)
    note_to_attendant = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Seat {self.seat_number or 'N/A'}: {self.prediction} ({self.confidence})"
