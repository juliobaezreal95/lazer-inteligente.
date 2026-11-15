# -*- coding: utf-8 -*-
"""
🎯 Lazer Inteligente — Sistema Especialista
Design: Clean, profissional e harmonioso
"""

import streamlit as st
from src.inferencia import recomendar_atividade


st.set_page_config(
    page_title="Lazer Inteligente",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    /* Fundo suave e limpo */
    .stApp {
        background: linear-gradient(180deg, #f0f7ff 0%, #ffffff 100%);
    }

    .block-container {
       .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 42rem;
    }
    
    /* Títulos e textos */
    h1 {
        color: #1e40af;
        font-weight: 700;
    }

    h2, h3, h4 {
        color: #1e3a8a;
        font-weight: 600;
    }

    p, label, span {
        color: #334155;
    }

    /* Cartões */
    .card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 14px;
        box-shadow: 0 2px 10px rgba(59, 130, 246, 0.08);
        border: 1px solid #dbeafe;
        margin-bottom: 1.2rem;
    }

    /* Caixa de resultado */
    .resultado-sucesso {
        background: linear-gradient(135deg, #f0fdf4, #dcfce7);
        border-left: 5px solid #16a34a;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 3px 12px rgba(22, 163, 74, 0.12);
    }

    .resultado-sucesso h3 {
        color: #166534;
    }

    .resultado-sucesso h2 {
        color: #14532d;
        font-size: 1.6rem;
    }

    /* Botão principal */
    .stButton > button {
        background: linear-gradient(90deg, #3b82f6, #2563eb);
        border: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.6rem 2.2rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.25);
    }

    /* Caixas de seleção */
    .stSelectbox > div > div {
        background: #ffffff;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
    }

    /* Rodapé */
    .rodape {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 2.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid #e2e8f0;
    }

    /* Divisores */
    hr {
        border: none;
        border-top: 1px solid #e0e7ff;
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div style='text-align: center; padding: 1.5rem 0 1rem 0;'>
    <h1 style='font-size: 2rem; margin: 0;'>🎯 Lazer Inteligente</h1>
    <p style='font-size: 1.05rem; color: #475569; margin-top: 0.5rem;'>Sistema Especialista de Recomendação de Atividades</p>
    <hr style='margin-top: 1.5rem;'>
</div>
""", unsafe_allow_html=True)



st.markdown("### 📋 Responda para receber sua recomendação")
st.markdown("Preencha as três informações abaixo e o sistema irá sugerir a melhor atividade para você!")

st.markdown("<br>", unsafe_allow_html=True)

col1 = st.selectbox(
    "⏱️ Tempo disponível",
    ["Selecione...", "curto", "medio", "longo"]
)

col2 = st.selectbox(
    "🏡 Ambiente preferido",
    ["Selecione...", "interno", "externo", "indiferente"]
)

col3 = st.selectbox(
    "💫 Tipo de atividade",
    ["Selecione...", "tranquilidade", "movimento", "social"]
)

st.markdown("<br>", unsafe_allow_html=True)


col_esq, col_btn, col_dir = st.columns([1, 2, 1])
with col_btn:
    clicou = st.button("✨ Obter Recomendação", type="primary", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)


if clicou:
    if col1 != "Selecione..." and col2 != "Selecione..." and col3 != "Selecione...":
        with st.spinner("🔍 Analisando regras do sistema..."):
            resultado = recomendar_atividade({
                "tempo": col1,
                "ambiente": col2,
                "preferencia": col3
            })
        
        # 📊 Dados informados
        st.markdown("""
        <div class='card'>
            <h4 style='margin-top: 0;'>📊 Suas Preferências</h4>
        """, unsafe_allow_html=True)
        
        d1, d2, d3 = st.columns(3)
        d1.info(f"⏱️ Tempo:\n**{col1}**")
        d2.info(f"🏡 Ambiente:\n**{col2}**")
        d3.info(f"💫 Estilo:\n**{col3}**")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # 🧠 Regras verificadas
        st.markdown("""
        <div class='card'>
            <h4 style='margin-top: 0;'>🧠 Análise do Sistema</h4>
            <p style='margin-bottom: 0;'>Regras verificadas: <strong>{}</strong></p>
        </div>
        """.format(", ".join(resultado["regras_testadas"])), unsafe_allow_html=True)
        
        # 🎯 Resultado final
        st.markdown(f"""
        <div class='resultado-sucesso'>
            <h3>✅ Recomendação Pronta!</h3>
            <h2>🎯 {resultado['conclusao']}</h2>
            <p style='margin: 0;'><strong>Regra aplicada:</strong> {resultado['regra']} &nbsp;|&nbsp; <strong>Fonte:</strong> {resultado['fonte']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
        
    else:
        st.error("⚠️ Por favor, selecione uma opção em cada campo acima antes de continuar!")


st.markdown("""
<div class='rodape'>
    <p><strong>🎯 Lazer Inteligente</strong> — Sistema Especialista</p>
    <p>Desenvolvido em Python • Baseado em Regras • Interface com Streamlit</p>
</div>
""", unsafe_allow_html=True)
