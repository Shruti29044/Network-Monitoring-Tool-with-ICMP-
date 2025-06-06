!pip install -q ping3 matplotlib

import csv
import time
from datetime import datetime
import matplotlib.pyplot as plt
from ping3 import ping
import os

hosts = ["8.8.8.8", "google.com", "cloudflare.com"]
csv_file = "network_log.csv"

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Host", "Status", "ResponseTime(ms)"])

def log_status():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for host in hosts:
        response_time = ping(host, timeout=2)
        if response_time is not None:
            ms = round(response_time * 1000, 2)
            status = "UP"
        else:
            ms = None
            status = "DOWN"

        with open(csv_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, host, status, ms])
        print(f"[{timestamp}] {host} → {status} ({ms} ms)" if ms else f"[{timestamp}] {host} → {status}")

def visualize():
    data = {}
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            host = row["Host"]
            timestamp = row["Timestamp"]
            if row["Status"] == "UP":
                response = float(row["ResponseTime(ms)"])
                if host not in data:
                    data[host] = {"timestamps": [], "responses": []}
                data[host]["timestamps"].append(timestamp)
                data[host]["responses"].append(response)

    plt.figure(figsize=(12, 6))
    for host, vals in data.items():
        plt.plot(vals["timestamps"], vals["responses"], label=host)
    plt.xticks(rotation=45)
    plt.ylabel("Response Time (ms)")
    plt.xlabel("Timestamp")
    plt.title("📶 Network Response Times Over Time")
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# === Run ===
for _ in range(5):  # You can increase the loop for longer monitoring
    log_status()
    time.sleep(10)

print("\n📊 Generating chart...")
visualize()
