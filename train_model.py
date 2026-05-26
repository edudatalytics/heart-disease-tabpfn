import os
import joblib
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from tabpfn import TabPFNClassifier


# Configurando o token
os.environ["TABPFN_TOKEN"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNmZkYTc2ZGMtYjcxOC00MmE3LWFiZmYtNGJkZTY2YTZkMWEwIiwiZXhwIjoxODEwODYwOTAwfQ.77LdzTUd0gWHWOCfge7-832jqEyx7fAqHl9h8oJ66d0"

# Carregando o dataset
print("⏳ Carregando dataset...")
dataset = fetch_openml(name="heart-disease", version=1, as_frame=True, parser="auto")
X = dataset.data.copy()
y = X.pop("target").astype(int)
print(f"✅ Dataset carregado! Shape: {X.shape}")

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print(f"📦 Treino: {X_train.shape[0]} amostras | 🧪 Teste: {X_test.shape[0]} amostras")

# Treinando o modelo
print("\n⏳ Treinando TabPFN...")
modelo = TabPFNClassifier()
modelo.fit(X_train, y_train)
print("✅ Modelo treinado!")

# Salvando o modelo
joblib.dump(modelo, "model.pkl")
print("💾 Modelo salvo em model.pkl!")