import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import os

os.makedirs("data/processed", exist_ok=True)

# Load params 
with open("params.yaml") as f:
    params = yaml.safe_load(f)

test_size = params["train"]["test_size"]
random_state = params["train"]["random_state"]

#    L oad dataset
df = pd.read_csv("data/raw/Titanic-Dataset.csv")

# Select features
df = df[["Pclass", "Sex", "Age", "Fare", "Survived"]]

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())

# Encode categorical column
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# Split data
X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=test_size,
    random_state=random_state
)

# Save processed files
X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)

y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

print("Preprocessing completed")