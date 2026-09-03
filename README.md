# AI-Powered SOC & Threat Intelligence Dashboard

An end-to-end cybersecurity data analysis and threat monitoring pipeline designed to ingest network telemetry, process traffic logs with SQLite, and detect DDoS attack patterns using analytical modeling and DAX formulations.

## SOC Telemetry Overview
Below is the automated exploratory analysis comparing legitimate traffic profiles against anomalous DDoS signatures.

<img src="reports/figures/soc_traffic_overview.png" alt="SOC Traffic Overview" width="850" />

## Key Technical Components
- **Data Engineering:** Ingested and structured CICIDS2017 network traffic into an optimized SQLite local database.
- **Threat Analysis:** Analyzed packet size variance, flow durations, and transmission frequencies between baseline and attack states.
- **Business Intelligence & Modeling:** Defined analytical DAX formulas in [docs/data_modeling_dax.md](docs/data_modeling_dax.md) for Power BI/SOC dashboard deployments.

## Repository Architecture
```text
ai-cybersec-dashboard/
├── data/                  # Telemetry datasets
├── docs/                  # Data models and DAX specifications
├── reports/
│   └── figures/           # Exported visual telemetry reports
├── sql/                   # SQLite schema and threat queries
├── src/                   # Pipeline execution scripts
└── README.md              # Project documentation
```
