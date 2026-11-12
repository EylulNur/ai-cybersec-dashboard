# SOC Threat Intelligence & Network Traffic Analysis

This project focuses on analyzing network traffic and identifying differences between legitimate traffic and DDoS attack traffic using the **CICIDS2017** dataset.

I built it as a hands-on cybersecurity analytics project to practice working with network flow data, SQL, Python, and Power BI-style SOC metrics.

## Project Overview
The project takes network flow records, stores the cleaned data in a local SQLite database, and uses Python to analyze traffic patterns.

The main focus is on metrics such as:
* Packet size
* Flow duration
* Traffic volume
* Connection frequency
* Differences between normal and attack traffic

The purpose is to see how these metrics can be used to support DDoS detection in a SOC environment.

## Key Findings
The analysis showed noticeable differences between legitimate and attack traffic:

<img src="reports/figures/soc_traffic_overview.png" alt="SOC Traffic Overview" width="850" />

* **Packet Size:** Legitimate traffic generally had larger packet sizes, while DDoS traffic contained a much higher number of smaller and short-lived flows.
* **Traffic Volume:** Attack traffic produced a large number of connections within a relatively short period. This creates a clear difference in traffic distribution compared with normal network activity.

These differences can be useful as indicators when building SOC monitoring and alerting dashboards.

## Project Structure
```text
ai-cybersec-dashboard/
├── docs/
│   └── data_modeling_dax.md
├── reports/
│   └── figures/soc_traffic_overview.png
├── sql/
│   ├── cybersecurity.db
│   └── threat_hunting_queries.sql
├── src/
│   └── visualize.py
└── README.mds