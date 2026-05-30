import pandas as pd
import yaml
import mlflow
import joblib
# Start MLflow  
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Titanic_MLOps")

mlflow.sklearn.autolog()
from sklearn.tree import DecisionTreeClassifier

# Load params
with open("params.yaml") as f:
    params = yaml.safe_load(f)

max_depth = params["model"]["max_depth"]

# Load data
X_train = pd.read_csv("data/processed/X_train.csv")
y_train = pd.read_csv("data/processed/y_train.csv")

with mlflow.start_run():

    # Train model
    model = DecisionTreeClassifier(max_depth=max_depth)
    X_train = X_train.astype("float64")
    model.fit(X_train, y_train.values.ravel())

    # Log params
    mlflow.log_param("max_depth", max_depth)

    # Save model
    joblib.dump(model, "models/model.pkl")

    # Log artifact
    mlflow.log_artifact("models/model.pkl")

print("Model trained successfully")