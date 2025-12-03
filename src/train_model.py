import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Read log data
df = pd.read_csv("../logs/sample.csv")

# Convert status code to number feature
df["status"] = df["status"].astype(int)

X = df[["status"]]

# Train model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# Save model
joblib.dump(model, "../models/model.pkl")

print("Model saved successfully!")





