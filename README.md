# AI-Powered Cybersecurity Data Analysis Dashboard

Generative AI destekli bir siber güvenlik veri analizi projesi. IBM Cybersecurity Analyst ve Microsoft Generative AI for Data Analysis sertifikalarında öğrenilen bilgilerimle uygulamalı bir portfolyo projesine dönüştürülmesi amacıyla geliştirilmiştir.

## Proje Amacı

Ham güvenlik log verilerini (network traffic, intrusion detection, phishing/malware olayları vb.) alıp:
- Python + SQL ile temizleme ve yapılandırma
- Generative AI (Copilot / Azure OpenAI / açık kaynak LLM) ile anomali tespiti, özetleme ve doğal dil sorgulama
- Power BI ile interaktif dashboard

üreten uçtan uca bir veri analizi hattı kurmak.

## Tech Stack

| Katman | Araç |
|---|---|
| Veri temizleme & analiz | Python (pandas, numpy) |
| Veri saklama & sorgulama | SQL (SQLite / PostgreSQL) |
| AI destekli analiz | Microsoft Copilot / Azure OpenAI / (opsiyonel: Ollama, lokal LLM) |
| Görselleştirme | Power BI |
| Versiyon kontrolü | Git & GitHub |

## 📁 Klasör Yapısı

```
ai-cybersec-dashboard/
├── data/
│   ├── raw/            # Ham veri (ör. Kaggle cybersecurity dataset)
│   └── processed/      # Temizlenmiş, analiz edilmeye hazır veri
├── notebooks/          # Keşifsel veri analizi (EDA) notebook'ları
├── src/                # Python script'leri (temizleme, AI entegrasyonu)
├── sql/                # Şema ve sorgular
├── powerbi/             # .pbix dosyaları / dashboard ekran görüntüleri
├── docs/                # Proje dokümantasyonu, AI kullanım şeffaflığı notu
└── README.md
```

## Yol Haritası (Microsoft Sertifikası ile Paralel)

- [x] **Modül 1 — GenAI temelleri & araçlar**: Hangi AI aracını kullanacağımıza karar verdik (Copilot öncelikli, Ollama/LM Studio yedek).
- [ ] **Modül 2 — Workflow entegrasyonu**: `src/data_cleaning.py` — AI destekli veri temizleme
- [ ] **Modül 3 — EDA & pattern bulma**: `notebooks/eda.ipynb` — anomali/pattern analizi
- [ ] **Modül 4 — Prompt engineering**: `src/ai_insights.py` — otomatik insight/rapor üretimi
- [ ] **Modül 5 — Responsible AI**: `docs/responsible_ai.md` — AI kullanım şeffaflığı ve etik notlar
- [ ] Power BI dashboard'unun kurulması ve AI-generated narratives eklenmesi
- [ ] GitHub'a push + README görselleri
- [ ] CV & LinkedIn'e ekleme

## Veri Kaynağı Önerisi

Henüz seçilmedi. Aday datasetler (Kaggle üzerinden):
- CICIDS2017 / CICIDS2018 (Intrusion Detection)
- Phishing Website Dataset
- Malware Detection Dataset

## Sorumlu AI Kullanımı

Bu projede üretilen AI çıktıları (özetler, anomali tespitleri, öneriler) her zaman insan gözetiminde doğrulanır. AI, karar verme sürecinin yerini almaz, analisti destekler.
