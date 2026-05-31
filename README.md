# CDC BRFSS Veri Seti Üzerinden Solunum Yolu Hastalıkları ve Çevresel Faktörler Analizi (Grup 8)

Bu proje, Centers for Disease Control and Prevention (CDC) tarafından paylaşılan Behavioral Risk Factor Surveillance System (BRFSS) 2024 veri seti kullanılarak geliştirilen bir makine öğrenmesi çalışmasıdır. Projenin temel amacı; bireylerin astım (`ASTHMA3`) ve KOAH gibi kronik solunum yolu rahatsızlıkları ile fiziksel aktivite düzeyleri ve coğrafi/çevresel faktörler arasındaki çok boyutlu ilişkileri kurgulamaktır.

## 🚀 Proje Odak Noktası & Yöntem
* **Hedek Değişkenler:** Astım (ASTHMA3) ve KOAH (Kronik Obstrüktif Akciğer Hastalığı)
* **Temel Algoritma:** K-En Yakın Komşuluk (KNN - K-Nearest Neighbors) sınıflandırması ve mesafe ölçütleri analizi.
* **Veri Mühendisliği:** Eksik verilerin KNN Imputation yöntemi ile doldurulması, aykırı değer tespiti ve veri dengesizliğinin giderilmesi.

## 📁 Klasör Yapısı
Proje mimarisi veri bilimi standartlarına uygun olarak aşağıdaki gibi kurgulanmıştır:
* `/data`: İşlenmiş veri setleri ve veri sözlükleri.
* `/notebooks`: Keşifsel Veri Analizi (EDA) ve model deneme Jupyter Notebook dosyaları.
* `/src`:Analiz sonrası üretim (production) aşaması için planlanan Python scriptleri.
* `/analysis`: Model başarı metrikleri (F1, AUC-ROC), konfüzyon matrisleri ve grafik çıktıları.
* `/docs`: Akademik makale raporu (Cambria, APA 7 formatında) ve sunum dosyaları.

## 👥 Ekip Üyeleri (Grup 8)
* Eyüp Karakoç 
* Ozan Güneş 
* Ravza İbil 
* Elif Azra İşbilir 
