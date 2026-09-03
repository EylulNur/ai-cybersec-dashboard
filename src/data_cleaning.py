import pandas as pd
import numpy as np
import os

print("1. Veri seti yükleniyor (birkaç saniye sürebilir)...")
raw_path = 'data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'
df = pd.read_csv(raw_path)

print(f"Toplam Satır: {df.shape[0]}, Toplam Sütun: {df.shape[1]}")

# 1. Sütun adlarındaki gizli boşlukları temizle
df.columns = df.columns.str.strip()

# 2. Sonsuz (Inf) değerleri NaN yap ve ardından NaN olan satırları temizle
df.replace([np.inf, -np.inf], np.nan, inplace=True)
initial_rows = len(df)
df.dropna(inplace=True)
print(f"Eksik/Bozuk değer temizliği: {initial_rows - len(df)} satır temizlendi.")

# 3. Dashboard için en kritik ve anlamlı sütunları filtrele (80+ sütunun hepsine gerek yok)
key_columns = [
    'Destination Port',
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Total Length of Fwd Packets',
    'Flow Bytes/s',
    'Flow Packets/s',
    'Flow IAT Mean',
    'Packet Length Mean',
    'Packet Length Std',
    'Average Packet Size',
    'Label'
]

# Eğer bu sütunlardan bazıları farklı adlandırılmışsa kontrol et
df_filtered = df[[col for col in key_columns if col in df.columns]].copy()

# 4. Saldırı etiketlerinin dağılımını göster (BENIGN vs DDoS)
print("\n--- Veri Setindeki Trafik Dağılımı ---")
print(df_filtered['Label'].value_counts())

# 5. İşlenmiş ve hafifletilmiş veriyi kaydet
os.makedirs('data/processed', exist_ok=True)
processed_path = 'data/processed/ddos_cleaned.csv'
df_filtered.to_csv(processed_path, index=False)
print(f"\nTemizlenmiş veri başarıyla kaydedildi: {processed_path}")
