import pandas as pd
import joblib

def test_model_prediction():

    model = joblib.load("models/model.pkl")

    data = pd.DataFrame({
        "Pclass": [3],
        "Sex": [1],
        "Age": [22],
        "Fare": [7.25]
    })

    prediction = model.predict(data)

    assert prediction[0] in [0, 1]