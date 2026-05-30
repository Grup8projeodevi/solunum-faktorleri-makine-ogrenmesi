import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, mean_squared_error, log_loss, roc_curve

# --- 1. VERİ YÜKLEME VE TEMİZLEME ---
print("1/5: Veri yükleniyor ve temizleniyor...")
df = pd.read_csv(r'.vscode\ödev\brfss_survey_data_2024.csv')
df_grup8 = df[['_STATE', 'ASTHMA3', 'CHCCOPD3', 'EXERANY2']].copy()

for kolon in ['ASTHMA3', 'CHCCOPD3', 'EXERANY2']:
    df_grup8[kolon] = df_grup8[kolon].replace([7, 9, 77, 99], np.nan)

# --- 2. EKSİK VERİ DOLDURMA (GÜN 3-4) ---
print("2/5: KNN Imputation yapılıyor...")
df_sample = df_grup8.head(10000).copy()
imputer = KNNImputer(n_neighbors=5)
df_temiz = pd.DataFrame(imputer.fit_transform(df_sample), columns=df_grup8.columns)

# PROFESYONEL DOKUNUŞ: Sınıfları 1 (Astım) ve 0 (Sağlıklı) olarak standartlaştırıyoruz
df_temiz['ASTHMA3'] = df_temiz['ASTHMA3'].round().apply(lambda x: 1 if x == 1 else 0)

# --- 3. KEŞİFSEL VERİ ANALİZİ (EDA) VE KORELASYON - GÜN 5-6 ---
print("3/5: Korelasyon Matrisi çiziliyor (Açılan grafik penceresini kapattığınızda kod devam eder)...")
plt.figure(figsize=(8, 6))
sns.heatmap(df_temiz.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Değişkenler Arası Korelasyon Matrisi")
plt.show() # İlk grafik burada açılır, kullanıcı kapatana kadar kod bekler

# --- 4. VERİ BÖLME VE ÖLÇEKLENDİRME - GÜN 7 ---
print("4/5: Veri bölünüyor ve ölçeklendiriliyor (Data Leakage engellendi)...")
y = df_temiz['ASTHMA3']
X = df_temiz.drop('ASTHMA3', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- 5. MODELLERİN EĞİTİLMESİ VE KIYASLANMASI - GÜN 8-12 ---
print("5/5: Farklı modeller eğitiliyor ve sonuçlar hesaplanıyor...\n")

# Takvimde istenen tüm modeller sözlük (dictionary) yapısında kuruluyor
modeller = {
    "Lojistik Regresyon (Baseline)": LogisticRegression(),
    "Karar Ağacı (Baseline)": DecisionTreeClassifier(random_state=42),
    "Random Forest (Gelişmiş)": RandomForestClassifier(random_state=42),
    "Yapay Sinir Ağı (MLP)": MLPClassifier(max_iter=1000, random_state=42),
    "KNN (Optimize Edilmiş)": KNeighborsClassifier(n_neighbors=31, weights='distance')
}

plt.figure(figsize=(10, 8))

for isim, model in modeller.items():
    # Modeli Eğit
    model.fit(X_train_scaled, y_train)
    
    # Tahminleri ve Olasılıkları Al
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    # İstenen Metrikleri Hesapla
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    roc = roc_auc_score(y_test, y_prob)
    mse = mean_squared_error(y_test, y_pred)
    ll = log_loss(y_test, y_prob)
    
    # Terminale Yazdır
    print(f"--- {isim} ---")
    print(f"Accuracy: {acc:.4f} | F1: {f1:.4f} | ROC-AUC: {roc:.4f}")
    print(f"MSE (Hata): {mse:.4f} | Log Loss: {ll:.4f}\n")
    
    # ROC Eğrisi için X ve Y kordinatlarını topla ve grafiğe ekle
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=f"{isim} (AUC = {roc:.2f})")

# ROC Eğrisi Grafiğini Ekrana Bas (Gün 12)
plt.plot([0, 1], [0, 1], 'k--', label='Rastgele Tahmin (Yazı-Tura)')
plt.xlabel('False Positive Rate (Yalancı Pozitif Oranı)')
plt.ylabel('True Positive Rate (Doğru Pozitif Oranı)')
plt.title('Modellerin ROC-AUC Eğrileri Karşılaştırması')
plt.legend(loc='lower right')
plt.show()