import joblib
import pandas as pd

# Load model
model = joblib.load("models/model.pkl")

# Sample input
data = {
    "Pclass": [-8],
    "Sex": [2],
    "Age": [100],
    "Fare": [8]
}

# Convert to dataframe
df = pd.DataFrame(data)

# Prediction
prediction = model.predict(df)

print("Prediction:", prediction[0])