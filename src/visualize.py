import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('reports/figures', exist_ok=True)
sns.set_theme(style='whitegrid')

colors = {'BENIGN': '#2ecc71', 'DDoS': '#e74c3c'}
conn = sqlite3.connect('sql/cybersecurity.db')
query = 'SELECT Label, Flow_Duration, Average_Packet_Size FROM network_traffic'
df = pd.read_sql_query(query, conn)
conn.close()

plt.figure(figsize=(12, 5))

# Ortalama Paket Boyutu
plt.subplot(1, 2, 1)
sns.barplot(x='Label', y='Average_Packet_Size', hue='Label', data=df, estimator='mean', errorbar=None, palette=colors, legend=False)
plt.title('Average Packet Size: Normal vs DDoS (Bytes)', fontsize=12, fontweight='bold')
plt.xlabel('Traffic Type')
plt.ylabel('Mean Packet Size (Bytes)')

# Trafik Dagitim Orani
plt.subplot(1, 2, 2)
label_counts = df['Label'].value_counts()
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', colors=[colors[l] for l in label_counts.index], startangle=140, explode=[0.05 if l == 'DDoS' else 0 for l in label_counts.index])
plt.title('Traffic Volume Distribution', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('reports/figures/soc_traffic_overview.png', dpi=300)
print('Basarili: reports/figures/soc_traffic_overview.png olusturuldu.')
