# 🛡️ AI-Powered Cybersecurity Traffic Analytics Pipeline

> 🚧 **Aktif geliştirme aşamasında.** Şu an Modül 1 (veri temizleme + SQLite + EDA) tamamlandı, Modül 2 (Power BI dashboard) üzerinde çalışılıyor.

Bu proje, CIC-IDS-2017 ağ trafiği veri kümesindeki DDoS anomalilerini tespit etmek için geliştirdiğim bir analitik hat. Ham veriyi temizliyor, SQLite veritabanına yüklüyor, ardından trafik davranışını normal ve saldırı akışları arasında karşılaştıran otomatik bir tehdit raporu üretiyor.

## 🔍 Öne Çıkan Bulgular

| Metrik | Normal (BENIGN) | DDoS | Fark |
|---|---|---|---|
| Ortalama paket boyutu | 224.37 bayt | 736.89 bayt | ~%228 daha büyük |
| Ortalama akış süresi | — | — | ~%11 daha uzun |
| Akış sayısı | 97.686 (%43.3) | 128.025 (%56.7) | toplam 225.711 akış |

Bu tablo, `sql/schema.sql` içindeki sorgularla üretilen özet istatistiklere dayanıyor.

## 🛠 Kullanılan Teknolojiler

* **Python 3** — Pandas, NumPy
* **SQLite3 / SQL** — veri katmanı
* **Power BI** — görselleştirme (Modül 2, devam ediyor)
* **Git & GitHub** — sürüm kontrolü

## 🚀 Nasıl Çalıştırılır

```bash
# 1. Repoyu klonla
git clone https://github.com/EylulNur/ai-cybersec-dashboard.git
cd ai-cybersec-dashboard

# 2. Gerekli kütüphaneleri kur
pip install -r requirements.txt

# 3. Veriyi temizle
python src/data_cleaning.py

# 4. SQLite'a yükle
python src/load_to_sql.py

# 5. Otomatik tehdit raporu üret
python src/ai_narrative.py
```

Ham veri (`data/raw/`) büyük olduğu için repoya dahil edilmedi — CIC-IDS-2017 veri setini [buradan](https://www.unb.ca/cic/datasets/ids-2017.html) indirip `data/raw/` klasörüne koymanız gerekiyor.

## 📂 Klasör Yapısı

```
ai-cybersec-dashboard/
├── data/
│   ├── raw/                # Ham CIC-IDS-2017 verisi (.gitignore ile korunur)
│   └── processed/          # Temizlenmiş 225k satırlık ddos_cleaned.csv
├── docs/
│   ├── responsible_ai.md   # Güvenlik etiği ve sorumlu yapay zeka notları
│   └── threat_summary.txt  # Üretilen otomatik tehdit analiz raporu
├── sql/
│   ├── cybersecurity.db    # Yerel SQLite veritabanı (binary, git-ignored)
│   └── schema.sql          # Tablo tanımları ve analitik sorgular
├── src/
│   ├── data_cleaning.py    # NaN/Inf temizleme ve şema standartlaştırma
│   ├── load_to_sql.py      # SQLite aktarım ve metrik sorgulama hattı
│   └── ai_narrative.py     # Metriklerden anomali raporu üreten anlatım motoru
├── requirements.txt
└── README.md
```

## 📝 Notlar

Bu proje bir öğrenme/portföy çalışması olarak geliştiriliyor. Şu an kural/istatistik tabanlı bir anomali analizi yapıyor; ileride bir sınıflandırma modeli (örn. Random Forest) eklemeyi planlıyorum. Geri bildirim ve katkılara açığım.
