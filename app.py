
import streamlit as st
import requests

# Configuração da página
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="🫀",
    layout="centered"
)

# Título e descrição
st.title("🫀 Heart Disease Prediction")
st.markdown("### Predição de Doenças Cardíacas usando TabPFN")
st.markdown("Preencha os dados clínicos do paciente abaixo para obter o diagnóstico.")
st.divider()
# ================================
# Formulário de entrada
# ================================
# Criando um layout de duas colunas para organizar melhor os campos

col1, col2 = st.columns(2)

# Campos de entrada para o formulário, organizados em duas colunas
# primeira coluna
with col1:
    age = st.number_input("Idade", min_value=20, max_value=100, value=50)
    sex = st.selectbox("Sexo", options=[0, 1], format_func=lambda x: "Feminino" if x == 0 else "Masculino")
    cp = st.selectbox("Tipo de Dor no Peito", options=[0, 1, 2, 3],
                      format_func=lambda x: {0: "Angina Típica", 1: "Angina Atípica",
                                             2: "Dor Não Cardíaca", 3: "Assintomático"}[x])
    trestbps = st.number_input("Pressão Arterial em Repouso (mmHg)", min_value=80, max_value=220, value=120)
    chol = st.number_input("Colesterol (mg/dL)", min_value=100, max_value=600, value=240)
    fbs = st.selectbox("Glicemia em Jejum > 120mg/dL", options=[0, 1],
                       format_func=lambda x: "Não" if x == 0 else "Sim")
    restecg = st.selectbox("Eletrocardiograma em Repouso", options=[0, 1, 2],
                           format_func=lambda x: {0: "Normal", 1: "Anormalidade ST-T",
                                                  2: "Hipertrofia Ventricular"}[x])
    
# segunda coluna
with col2:
    thalach = st.number_input("Frequência Cardíaca Máxima", min_value=60, max_value=220, value=150)
    exang = st.selectbox("Angina Induzida por Exercício", options=[0, 1],
                         format_func=lambda x: "Não" if x == 0 else "Sim")
    oldpeak = st.number_input("Depressão do Segmento ST", min_value=0.0, max_value=10.0,
                               value=1.0, step=0.1)
    slope = st.selectbox("Inclinação do Segmento ST", options=[0, 1, 2],
                         format_func=lambda x: {0: "Descendente", 1: "Plana",
                                                2: "Ascendente"}[x])
    ca = st.selectbox("Nº de Vasos Principais", options=[0, 1, 2, 3])
    thal = st.selectbox("Talassemia", options=[0, 1, 2, 3],
                        format_func=lambda x: {0: "Normal", 1: "Defeito Fixo",
                                               2: "Defeito Reversível", 3: "Outro"}[x])

st.divider()

# Botão para enviar os dados para a API

if st.button("🔍 Analisar Paciente", use_container_width=True):

    # Montando os dados para enviar para a API
    dados = {
        "age": age, "sex": sex, "cp": cp,
        "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "restecg": restecg,
        "thalach": thalach, "exang": exang,
        "oldpeak": oldpeak, "slope": slope,
        "ca": ca, "thal": thal
    }

    # Chamando a API
    with st.spinner("⏳ Analisando dados do paciente..."):
        resposta = requests.post("http://127.0.0.1:8000/predict", json=dados)

    # Exibindo o resultado
    if resposta.status_code == 200:
        resultado = resposta.json()

        st.markdown("## 📊 Resultado do Diagnóstico")

        if resultado["predicao"] == 1:
            st.error(f"⚠️ **Diagnóstico: {resultado['diagnostico']}**")
        else:
            st.success(f"✅ **Diagnóstico: {resultado['diagnostico']}**")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Probabilidade Saudável",
                      f"{resultado['probabilidade_saudavel']*100:.1f}%")
        with col2:
            st.metric("Probabilidade Doente",
                      f"{resultado['probabilidade_doente']*100:.1f}%")
    else:
        st.error("❌ Erro ao conectar com a API. Verifique se ela está rodando.")