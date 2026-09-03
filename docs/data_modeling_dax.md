# SOC Analytics Data Modeling & DAX Documentation
## Overview
This document outlines the analytical data models and DAX (Data Analysis Expressions) calculated measures used to monitor network security events and identify DDoS anomalies.
## Data Schema
- **Fact Table:** `network_traffic`
  - `Flow_ID` (Text): Unique connection identifier
  - `Source_IP` (Text): Originating IP address
  - `Destination_IP` (Text): Target server IP address
  - `Flow_Duration` (Integer): Duration of connection in microseconds
  - `Average_Packet_Size` (Numeric): Mean size of transmitted packets in bytes
  - `Label` (Text): Classification (`Normal` or `DDoS`)
## Key DAX Measures
### 1. Total Incident Volume
```dax
Total Flows = COUNTROWS(network_traffic)
```
### 2. DDoS Attack Ratio (%)
```dax
DDoS Attack Rate = 
DIVIDE(
    CALCULATE(COUNTROWS(network_traffic), network_traffic[Label] = "DDoS"),
    [Total Flows],
    0
)
```
### 3. Mean Packet Discrepancy Index
```dax
Avg Packet Size Normal = 
CALCULATE(
    AVERAGE(network_traffic[Average_Packet_Size]),
    network_traffic[Label] = "Normal"
)

Avg Packet Size DDoS = 
CALCULATE(
    AVERAGE(network_traffic[Average_Packet_Size]),
    network_traffic[Label] = "DDoS"
)
```
