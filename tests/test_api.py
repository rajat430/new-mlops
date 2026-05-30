from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction_api():

    response = client.post(
        "/predict",
        data={
            "Pclass": 3,
            "Sex": 1,
            "Age": 22,
            "Fare": 7.25
        }
    )

    assert response.status_code == 200