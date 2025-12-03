import time
import random

log_path = "../logs/live.log"

while True:
    status = random.choice([200, 200, 200, 500])  # 500 = anomaly sometimes
    with open(log_path, "a") as f:
        f.write(f"127.0.0.1 - - [27/Nov/2025:12:00:00 +0000] \"GET /test HTTP/1.1\" {status}\n")
    time.sleep(0.3)