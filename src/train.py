import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import yaml

# Load config
with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)

model_path = config["model_file"]

# Load new log CSV
df = pd.read_csv("../logs/sample.csv")

df["status"] = df["status"].astype(int)
X = df[["status"]]

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

joblib.dump(model, model_path)
print("Model retrained & saved:", model_path)