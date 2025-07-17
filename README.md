# Simulated CPU Load Monitoring Stack

This project simulates CPU load using a lightweight Python HTTP server, which exposes custom `/metrics` for Prometheus to scrape. The stack includes:

- **Python script** to simulate CPU usage
- **Prometheus** to scrape and store the metrics
- **Grafana** to visualize metrics and send alerts to **Slack**

---

## 📦 Stack Overview

- `simulate_cpu.py`: Simulates a fluctuating CPU load and exposes metrics at `/metrics`
- `Prometheus`: Collects the simulated metrics
- `Grafana`: Dashboards and alerting (including Slack integration)
- `docker-compose.yml`: Spins up the entire stack for local testing

---

## 🧪 Simulated Metrics

The Python server returns:
```text
cpu_load_percent 57.23
cpu_load_timestamp 1721241634
