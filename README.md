📡 Network Connectivity and Performance Monitoring Tool

A simple Python script to monitor network connectivity and response times of multiple hosts using ICMP ping. It logs data to a CSV file and visualizes latency trends over time using matplotlib.

🚀 Features

✅ Periodically pings target hosts (e.g., 8.8.8.8, google.com)

✅ Logs results with timestamp, status (UP/DOWN), and response time

✅ Stores logs in a CSV file (network_log.csv)

✅ Generates a time-series chart of response times per host

✅ Minimal setup – works in Colab or any Python environment

🛠️ Technologies Used

Python 3

ping3 – ICMP ping utility

csv and datetime – for data logging and timestamping

matplotlib – for time series visualization

📦 Installation

Install required packages:

pip install ping3 matplotlib

If you're running this in Google Colab, add:

!pip install -q ping3 matplotlib

🧪 How It Works

Hosts Setup

Define the list of IPs/domains to ping:

hosts = ["8.8.8.8", "google.com", "cloudflare.com"]

Logging Status

The script:

Pings each host every 10 seconds

Logs results to network_log.csv with timestamp, status, and latency

Visualization

After collecting data, a time-series chart is plotted showing response times per host.

📊 Output Example

[2025-06-04 16:23:10] google.com → UP (18.45 ms)

[2025-06-04 16:23:10] cloudflare.com → UP (21.78 ms)

[2025-06-04 16:23:10] 8.8.8.8 → DOWN

Then generates a chart like this:

📶 Network Response Times Over Time

📁 File Generated

network_log.csv: A timestamped log of all ping attempts

🧩 Optional Extensions

You can extend this project with:

IP filtering (track only internal/private networks)

Alert system if a host goes down

SQL database integration for historical records

Upload results to Google Sheets

Export chart as PNG/PDF

⚠️ Limitations

Requires internet access to test external hosts

ICMP may be blocked by some networks

Not a real-time monitor; best suited for sampling trends

📝 Author

This script is created for educational purposes in Cloud Computing / Networking domains to demonstrate subprocess-level ping handling and visualization with Python.

Feel free to fork and modify!







