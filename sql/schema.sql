-- schema.sql
-- Dataset seçildikten sonra kolon isimleri güncellenecek.

CREATE TABLE IF NOT EXISTS security_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_timestamp DATETIME,
    source_ip TEXT,
    destination_ip TEXT,
    event_type TEXT,       -- örn: intrusion, phishing, malware
    severity TEXT,          -- örn: low, medium, high, critical
    is_anomaly BOOLEAN DEFAULT 0,
    ai_summary TEXT         -- AI tarafından üretilen olay özeti
);

-- Örnek analiz sorgusu: severity'e göre olay dağılımı
-- SELECT severity, COUNT(*) as event_count
-- FROM security_events
-- GROUP BY severity
-- ORDER BY event_count DESC;
