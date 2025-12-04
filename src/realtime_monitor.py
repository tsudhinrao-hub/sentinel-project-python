import time
import joblib
from log_parser import parse_log_line
import requests  # <-- Add this
import yaml

# Load configuration
with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)

SLACK_WEBHOOK_URL = config["slack_webhook"]
MODEL_PATH = config["model_file"]
LOG_PATH = config["log_file"]

SLACK_WEBHOOK_URL = "YOUR_WEBHOOK_HERE"
def send_to_slack(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    print("Slack response status:", response.status_code)
    if response.status_code != 200:
        print("Slack Error:", response.text)

MODEL_PATH = "../models/model.pkl"
LOG_PATH = "../logs/live.log"

model = joblib.load(MODEL_PATH)

def score_log(parsed):
    status = int(parsed["status"])
    result = model.predict([[status]])
    return result[0]  # -1 anomaly, 1 normal

def tail_log(file_path):
    with open(file_path) as file:
        file.seek(0, 2)  # start at end of file

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.2)
                continue

            parsed = parse_log_line(line)

            if parsed:
                if score_log(parsed) == -1:
                    alert_msg = f"🚨 ANOMALY DETECTED: {line.strip()}"
                    print(alert_msg)
                    send_to_slack(alert_msg)    
                else:
                    print("OK:", line.strip())

if __name__ == "__main__":
    print("Monitoring real-time logs...")
    tail_log(LOG_PATH)