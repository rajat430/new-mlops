from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pandas as pd
import joblib

app = FastAPI(title="Titanic Survival Prediction")

# ---------------------------------------
# Load trained model
# ---------------------------------------
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "models" / "model.pkl"

model = joblib.load(model_path)
# ---------------------------------------
# Home Page
# ---------------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Titanic Survival Prediction</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 40px;
                }
                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    width: 400px;
                    margin: auto;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
                }
                h1 {
                    text-align: center;
                }
                input, select {
                    width: 100%;
                    padding: 10px;
                    margin-top: 10px;
                    margin-bottom: 20px;
                }
                button {
                    width: 100%;
                    padding: 10px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056b3;
                }
                .result {
                    margin-top: 20px;
                    text-align: center;
                    font-size: 20px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Titanic Prediction</h1>

                <form action="/predict" method="post">

                    <label>Pclass</label>
                    <select name="Pclass">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </select>

                    <label>Sex</label>
                    <select name="Sex">
                        <option value="1">Male</option>
                        <option value="0">Female</option>
                    </select>

                    <label>Age</label>
                    <input type="number" step="0.1" name="Age" required>

                    <label>Fare</label>
                    <input type="number" step="0.1" name="Fare" required>

                    

                    <button type="submit">Predict Survival</button>
                </form>
            </div>
        </body>
    </html>
    """

# ---------------------------------------
# Prediction Endpoint
# ---------------------------------------
@app.post("/predict", response_class=HTMLResponse)
def predict(
    Pclass: int = Form(...),
    Sex: int = Form(...),
    Age: float = Form(...),
    Fare: float = Form(...)
):

    # Create dataframe
    data = pd.DataFrame({
        "Pclass": [Pclass],
        "Sex": [Sex],
        "Age": [Age],
        "Fare": [Fare]
    })

    # Match datatype
    data = data.astype("float64")

    # Prediction
    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Passenger Survived"
    else:
        result = "Passenger Did Not Survive"

    return f"""
    <html>
        <head>
            <title>Prediction Result</title>
            <style>
                body {{
                    font-family: Arial;
                    background-color: #f4f4f4;
                    padding: 40px;
                }}
                .container {{
                    background: white;
                    width: 400px;
                    margin: auto;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
                    text-align: center;
                }}
                a {{
                    text-decoration: none;
                    color: white;
                    background: #007bff;
                    padding: 10px 20px;
                    border-radius: 5px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Prediction Result</h1>
                <h2>{result}</h2>
                <br>
                <a href="/">Try Another Prediction</a>
            </div>
        </body>
    </html>
    """

# ---------------------------------------
# Run Application
# ---------------------------------------
# Command:
# uvicorn app:app --reload
