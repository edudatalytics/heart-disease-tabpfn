# 🫀 Heart Disease Prediction — TabPFN + FastAPI + Streamlit

Aplicação completa de Machine Learning para predição de doenças cardíacas.
O projeto cobre todo o ciclo de Data Science: análise exploratória, treinamento,
API de predição e interface interativa.

---

## 🎥 Demo

![Demo](https://img.shields.io/badge/Status-Online-brightgreen)

Interface interativa onde o usuário preenche os dados clínicos do paciente
e recebe o diagnóstico com probabilidades em tempo real.

---

## 📊 Resultados do Modelo

| Modelo  | Accuracy | ROC-AUC | F1-Score | Falsos Negativos |
|---------|----------|---------|----------|-----------------|
| **TabPFN**  | **0.869** | **0.922** | **0.889** | **1** |
| XGBoost | 0.803    | 0.856   | 0.838    | 2               |

> O TabPFN superou o XGBoost em todas as métricas **sem nenhum tuning de hiperparâmetros**.

---

## 🗂️ Estrutura do Projeto

```
heart-disease/
│
├── analise.ipynb       # EDA completa + comparação TabPFN vs XGBoost
├── train_model.py      # Treina e salva o modelo em model.pkl
├── main.py             # API FastAPI com rota /predict
├── app.py              # Interface Streamlit
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
└── .gitignore          # Arquivos ignorados pelo Git
```

---

## 📋 Dataset

- **Nome:** Heart Disease (UCI)
- **Fonte:** OpenML via `sklearn.datasets.fetch_openml`
- **Amostras:** 303 pacientes
- **Features:** 13 variáveis clínicas (idade, colesterol, frequência cardíaca, etc.)
- **Target:** Presença (1) ou ausência (0) de doença cardíaca

---

## 🔬 Metodologia

1. **EDA** — análise exploratória com distribuições e boxplots
2. **Pré-processamento** — verificação de nulos, tipos e split estratificado (80/20)
3. **Treinamento** — TabPFN e XGBoost sem tuning para comparação justa
4. **Avaliação** — Accuracy, ROC-AUC, F1-Score e Matriz de Confusão
5. **API** — FastAPI com validação automática via Pydantic
6. **Interface** — Streamlit com campos interativos e resultado visual

---

## 💡 Arquitetura

```
Usuário preenche os dados no Streamlit
        ↓
Streamlit chama a FastAPI via requests.post()
        ↓
FastAPI valida os dados com Pydantic
        ↓
TabPFN faz a predição
        ↓
API retorna JSON com diagnóstico + probabilidades
        ↓
Streamlit exibe o resultado visualmente
```

---

## ▶️ Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/edudatalytics/heart-disease-tabpfn.git
cd heart-disease-tabpfn

# 2. Ative o ambiente
conda activate olist

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Treine e salve o modelo
python train_model.py

# 5. Em um terminal — suba a API
uvicorn main:app --reload

# 6. Em outro terminal — suba a interface
streamlit run app.py
```

Acesse:
- **Interface:** http://localhost:8501
- **API Docs:** http://localhost:8000/docs

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TabPFN](https://img.shields.io/badge/TabPFN-v3-purple)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45-red)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6-red)

---

## 👤 Autor

**Eduardo Matos**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-eduardo--matos-blue)](https://linkedin.com/in/matos-eduardo)
[![GitHub](https://img.shields.io/badge/GitHub-edudatalytics-black)](https://github.com/edudatalytics)