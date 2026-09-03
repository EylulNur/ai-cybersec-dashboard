-- Threat Hunting & SOC Detection Queries
-- Target: SQLite Database (cybersecurity.db)

-- 1. High-Volume Attack Source Detection
-- Identifies top source IP addresses generating disproportionate traffic flows
SELECT 
    Source_IP,
    COUNT(*) AS Total_Flows,
    ROUND(AVG(Average_Packet_Size), 2) AS Avg_Packet_Size,
    ROUND(AVG(Flow_Duration), 2) AS Avg_Duration
FROM network_traffic
GROUP BY Source_IP
ORDER BY Total_Flows DESC
LIMIT 10;

-- 2. Small-Packet Flooding Analysis (DDoS Signature)
-- Identifies flows with abnormally small payloads typical of resource-exhaustion floods
SELECT 
    Flow_ID,
    Source_IP,
    Destination_IP,
    Average_Packet_Size,
    Flow_Duration,
    Label
FROM network_traffic
WHERE Average_Packet_Size < 100 AND Label = 'DDoS'
ORDER BY Flow_Duration ASC
LIMIT 15;

-- 3. Target Asset Impact Analysis
-- Evaluates which server IPs received the heaviest concentration of attack telemetry
SELECT 
    Destination_IP,
    COUNT(CASE WHEN Label = 'DDoS' THEN 1 END) AS DDoS_Incident_Count,
    COUNT(CASE WHEN Label = 'Normal' THEN 1 END) AS Baseline_Traffic_Count,
    ROUND(
        100.0 * COUNT(CASE WHEN Label = 'DDoS' THEN 1 END) / COUNT(*), 
        2
    ) AS Attack_Exposure_Rate
FROM network_traffic
GROUP BY Destination_IP
ORDER BY DDoS_Incident_Count DESC;