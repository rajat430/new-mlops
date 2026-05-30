import pandas as pd
import mlflow
import joblib

from sklearn.metrics import accuracy_score

# Load data
X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv")

# Load model
model = joblib.load("models/model.pkl")

# Prediction
preds = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, preds)

print(f"Accuracy: {accuracy}")

# Log metric
mlflow.set_tracking_uri("sqlite:///mlflow.db")

with mlflow.start_run():
    mlflow.log_metric("accuracy", accuracy)