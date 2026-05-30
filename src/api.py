import mlflow
import pandas as pd

mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Get experiment
experiment = mlflow.get_experiment_by_name("Titanic_MLOps")

# Search runs
runs = mlflow.search_runs(
    experiment_ids=[experiment.experiment_id]
)

print(experiment)