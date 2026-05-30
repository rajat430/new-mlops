import mlflow
import pandas as pd

mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Get experiment
experiment = mlflow.get_experiment_by_name("Titanic_MLOps")
try:
    # Search runs
    runs = mlflow.search_runs(
        experiment_ids=[experiment.experiment_id]
    )
except Exception as e:
    print(f"Error fetching runs: {e}")
    runs = pd.DataFrame()  # Create an empty DataFrame if there's an error
# Save report
runs.to_csv("mlflow_report.csv", index=False)
print(runs)