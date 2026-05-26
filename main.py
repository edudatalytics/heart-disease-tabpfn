# ================================
# MAIN.PY — Parte 1: Importações
# ================================

import os
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Configurando o token
os.environ["TABPFN_TOKEN"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNmZkYTc2ZGMtYjcxOC00MmE3LWFiZmYtNGJkZTY2YTZkMWEwIiwiZXhwIjoxODEwODYwOTAwfQ.77LdzTUd0gWHWOCfge7-832jqEyx7fAqHl9h8oJ66d0"

# Carregando o modelo salvo
modelo = joblib.load("model.pkl")

# Iniciando a aplicação FastAPI
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API para predição de doenças cardíacas usando TabPFN",
    version="1.0.0"
)

print("✅ API iniciada e modelo carregado!")

class DadosPaciente(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

    # ================================
# MAIN.PY — Parte 3: Rotas
# ================================

@app.get("/")
def home():
    return {
        "mensagem": "Heart Disease Prediction API",
        "status": "online",
        "versao": "1.0.0",
        "docs": "/docs"
    }


@app.post("/predict")
def predict(dados: DadosPaciente):

    # Convertendo os dados recebidos para array numpy
    entrada = np.array([[
        dados.age, dados.sex, dados.cp, dados.trestbps,
        dados.chol, dados.fbs, dados.restecg, dados.thalach,
        dados.exang, dados.oldpeak, dados.slope, dados.ca, dados.thal
    ]])

    # Fazendo a predição
    predicao = modelo.predict(entrada)[0]
    probabilidade = modelo.predict_proba(entrada)[0]

    # Montando a resposta
    return {
        "predicao": int(predicao),
        "diagnostico": "Doente" if predicao == 1 else "Saudável",
        "probabilidade_saudavel": round(float(probabilidade[0]), 4),
        "probabilidade_doente": round(float(probabilidade[1]), 4)
    }