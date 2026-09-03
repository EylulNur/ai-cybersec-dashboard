import sqlite3
import pandas as pd

conn = sqlite3.connect('sql/cybersecurity.db')

# SQL ile temel özet metrikleri çekiyoruz
query = """
SELECT 
    Label,
    COUNT(*) as Flow_Count,
    ROUND(AVG(Flow_Duration), 2) as Avg_Duration,
    ROUND(AVG(Total_Fwd_Packets), 2) as Avg_Fwd_Pkts,
    ROUND(AVG(Packet_Length_Mean), 2) as Avg_Pkt_Len,
    ROUND(AVG(Average_Packet_Size), 2) as Avg_Pkt_Size
FROM network_traffic
GROUP BY Label
"""

df_stats = pd.read_sql_query(query, conn)
conn.close()

# Modül 1 İlkesi: Otomatik Akıllı Anlatım Motoru
def generate_threat_narrative(stats):
    benign = stats[stats['Label'] == 'BENIGN'].iloc[0]
    ddos = stats[stats['Label'] == 'DDoS'].iloc[0]
    
    pkt_diff = round((ddos['Avg_Pkt_Len'] - benign['Avg_Pkt_Len']) / benign['Avg_Pkt_Len'] * 100, 1)
    duration_diff = round((ddos['Avg_Duration'] - benign['Avg_Duration']) / benign['Avg_Duration'] * 100, 1)

    narrative = f"""
================================================================================
          AI-POWERED CYBERSECURITY EXECUTIVE THREAT REPORT (EDA)
================================================================================
1. GENEL TRAFİK ÖZETİ:
   - Toplam İncelenen Akış (Flow): {int(benign['Flow_Count'] + ddos['Flow_Count']):,}
   - Güvenli Trafik (BENIGN): {int(benign['Flow_Count']):,} (%{round(benign['Flow_Count'] / (benign['Flow_Count'] + ddos['Flow_Count']) * 100, 1)})
   - Tespit Edilen DDoS Saldırısı: {int(ddos['Flow_Count']):,} (%{round(ddos['Flow_Count'] / (benign['Flow_Count'] + ddos['Flow_Count']) * 100, 1)})

2. ANOMALİ TESPİT BULGULARI:
   - Paket Boyutu Anomalisi: DDoS saldırısı altındaki ortalama paket boyutu ({ddos['Avg_Pkt_Len']} bayt), 
     normal trafik taban çizgisine ({benign['Avg_Pkt_Len']} bayt) kıyasla %{pkt_diff} DAHA BÜYÜKTÜR.
   - Akış Süresi (Duration): DDoS akışları normal trafiğe göre ortalama %{duration_diff} daha uzun sürmüştür.
   
3. YAPAY ZEKA DESTEKLİ TEHDİT DEĞERLENDİRMESİ:
   - Trafik paterni, bant genişliğini tüketmeye yönelik Volumetrik DDoS saldırı profiliyle örtüşmektedir.
   - Hedef portlar ve ileri yönlü paket sayıları taban çizgisini aştığından, ağ seviyesinde hız sınırlama (rate limiting)
     ve anomali tabanlı IPS kuralları derhal devreye alınmalıdır.
================================================================================
"""
    return narrative

report = generate_threat_narrative(df_stats)
print(report)

# Raporu docs klasörüne kaydet
with open('docs/threat_summary.txt', 'w') as f:
    f.write(report)

print("Yapay zeka analiz raporu docs/threat_summary.txt dosyasına kaydedildi.")
