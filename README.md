# 🫀 Heart Disease Prediction — TabPFN vs XGBoost

Projeto de classificação binária para predição de doenças cardíacas,
comparando o modelo TabPFN (foundation model para dados tabulares)
contra o XGBoost (modelo clássico de gradient boosting).

---

## 📊 Resultados

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
├── analise.ipynb       # Notebook principal com todo o projeto
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

---

## 💡 Principal aprendizado

O **TabPFN** é um transformer pré-treinado em milhões de datasets sintéticos.
Ele aprende padrões tabulares universais sem precisar de grid search ou
feature engineering — tornando-o extremamente eficiente para datasets
pequenos e médios.

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TabPFN](https://img.shields.io/badge/TabPFN-v3-purple)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6-red)

---

## ▶️ Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/edudatalytics/heart-disease-tabpfn.git

# 2. Ative o ambiente
conda activate olist

# 3. Instale as dependências
pip install tabpfn xgboost scikit-learn pandas matplotlib seaborn jupyter

# 4. Abra o notebook
jupyter notebook analise.ipynb
```

---

## 👤 Autor

**Eduardo Matos**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-eduardo--matos-blue)](https://linkedin.com/in/matos-eduardo)
[![GitHub](https://img.shields.io/badge/GitHub-edudatalytics-black)](https://github.com/edudatalytics)