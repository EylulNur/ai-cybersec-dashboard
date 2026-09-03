# AI-Powered Cybersecurity Traffic Analytics Pipeline

Bu proje, **CIC-IDS-2017** ağ trafiği veri kümesi üzerindeki DDoS anomalilerini tespit etmek, verileri yerel bir ilişkisel veri tabanında (SQLite) yapılandırmak ve otomatik tehdit değerlendirme raporları üretmek amacıyla geliştirilmiş uçtan uca bir analitik veri hattıdır.

---

### 🔍 Key Findings (EDA & Threat Intelligence)

* **Volumetrik Anomali:** DDoS akışlarındaki ortalama paket boyutu (**736.89 bayt**), normal taban çizgisi trafiğine (**224.37 bayt**) kıyasla **%228.4 daha büyüktür**.
* **Akış Süresi Sapması:** DDoS saldırı akışlarının ortalama süresi normal oturumlara kıyasla **%10.7 daha uzun** seyretmiştir.
* **Trafik Hacmi:** İncelenen 225.711 akışın %56.7'si (128.025 adet) DDoS, %43.3'ü (97.686 adet) normal (BENIGN) trafikten oluşmaktadır.

---

### 🛠 Tech Stack

* **Dil & Kütüphaneler:** Python 3 (Pandas, NumPy)
* **Veritabanı Katmanı:** SQLite3, SQL
* **Görselleştirme & Dashboard:** Power BI (Modül 2)
* **Sürüm Kontrolü:** Git & GitHub

---

### 📂 Proje Mimarisi


