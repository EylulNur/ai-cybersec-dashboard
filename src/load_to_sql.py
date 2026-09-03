import pandas as pd
import sqlite3
import os

print("1. Temizlenmiş veri okunuyor...")
df = pd.read_csv('data/processed/ddos_cleaned.csv')

# SQLite sütun adlarında boşluk veya özel karakter sevmez, standart hale getirelim
df.columns = [c.replace(' ', '_').replace('/', '_per_') for c in df.columns]

# Veritabanı bağlantısı
db_path = 'sql/cybersecurity.db'
os.makedirs('sql', exist_ok=True)
conn = sqlite3.connect(db_path)

print(f"2. {len(df)} satır SQLite veritabanına aktarılıyor ('network_traffic' tablosu)...")
df.to_sql('network_traffic', conn, if_exists='replace', index=False)

# Test sorgusu
cursor = conn.cursor()
cursor.execute("""
    SELECT 
        Label, 
        COUNT(*) as total_flows,
        ROUND(AVG(Flow_Duration), 2) as avg_duration,
        ROUND(AVG(Packet_Length_Mean), 2) as avg_packet_len
    FROM network_traffic
    GROUP BY Label
""")

print("\n--- SQL Test Sorgusu Sonucu ---")
print(f"{'Label':<10} | {'Total Flows':<12} | {'Avg Duration':<15} | {'Avg Packet Len':<15}")
print("-" * 60)
for row in cursor.fetchall():
    print(f"{row[0]:<10} | {row[1]:<12} | {row[2]:<15} | {row[3]:<15}")

conn.close()
print(f"\nVeritabanı hazır: {db_path}")
