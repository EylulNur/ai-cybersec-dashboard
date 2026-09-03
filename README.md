# ai-cybersec-dashboard

Bu projeyi CIC-IDS-2017 veri setiyle, siber güvenlik operasyonlarında veri analitiğinin uçtan uca nasıl çalıştığını görmek için yaptım. Ham ağ trafiğinden başlayıp veri tabanına, oradan da SOC analistlerinin işine yarayacak anlamlı metriklere ulaşan bir hat kurmak istedim.

### Neler Buldum?

* **Paket Boyutu Sıçraması:** DDoS saldırılarında ortalama paket boyutu 736.89 bayta fırlarken, normal taban çizgisi 224.37 bayt seviyesinde. Yaklaşık %228.4'lük bir hacim artışı var.
* **Oturum Süresi:** Saldırı akışları normal oturumlara kıyasla ortalama %10.7 daha uzun sürüyor.
* **Hacim:** 225.711 satırlık temizlenmiş akışın yaklaşık 128 bini DDoS, 97 bini normal trafik.

### Kullandığım Araçlar

* Python (pandas, numpy, sqlite3)
* SQL / SQLite
* Git & GitHub
* Power BI (Modül 2'de görselleştirme ve DAX metrikleri için bağlayacağım)

### Proje Yapısı

```text
ai-cybersec-dashboard/
├── data/
│   ├── raw/                # Ham CIC-IDS verisi (.gitignore'da)
│   └── processed/          # Temizlenmiş 225k satır: ddos_cleaned.csv
├── docs/
│   ├── responsible_ai.md   # Güvenlik etiği notları (yakında eklenecek — Modül 5 sonrası)
│   └── threat_summary.txt  # Üretilen tehdit özeti
├── sql/
│   ├── cybersecurity.db    # Yerel SQLite veritabanı
│   └── schema.sql          # Tablo şeması ve sorgular
├── src/
│   ├── data_cleaning.py    # NaN / Inf temizliği ve sütun düzeni
│   ├── load_to_sql.py      # SQLite aktarım hattı
│   └── ai_narrative.py     # İstatistiğe dayalı özet üreten script
├── requirements.txt
└── README.md
```

### Karşılaştığım Zorluklar ve Notlar

* Ham veri setindeki `Infinity` ve kayıp (`NaN`) değerler veritabanına aktarılırken sürekli tip hatalarına yol açtı; temizleme betiğinde bunları özel olarak filtreleyip sayısal tipleri sabitlemem gerekti.
* Büyük CSV dosyalarını ve yerel SQLite veritabanını repoya alıp şişirmemek adına `.gitignore` ve `.gitkeep` mantığını dikkatle kurdum; repoda sadece pipeline kodlarını ve dokümanları tutuyorum.
* Terminal ortamında çalışırken kimlik doğrulama (Personal Access Token) ve remote dal yapılandırması gibi Git pratiklerini bizzat deneyimledim.
* Sırada bu temiz veri tabanını Power BI'a bağlayıp SOC ekipleri için anomali odaklı bir gösterge paneli (dashboard) tasarlamak var.

> **Not:** Ham veri (`CIC-IDS-2017` - Friday Working Hours Afternoon DDoS) boyut nedeniyle repoya dahil edilmemiştir. 
> [Resmi kaynaktan](https://www.unb.ca/cic/datasets/ids-2017.html) indirip `data/raw/` klasörüne yerleştirmen gerekiyor.

### Nasıl Çalıştırılır?

```bash
pip install -r requirements.txt
python3 src/data_cleaning.py
python3 src/load_to_sql.py
python3 src/ai_narrative.py
```
