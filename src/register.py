import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")

model_uri = "models/model.pkl"

mlflow.register_model(
    model_uri=model_uri,
    name="TitanicModel"
)

print("Model Registered")