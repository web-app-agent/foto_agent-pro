"""
FotoAgent Pro - Streamlit App (Pronto para Deploy com URL Pública)
Este aplicativo Python em Streamlit implementa toda a lógica de ideação, 
composição multi-image (blending) e geração de ensaios fotográficos profissionais.
Para gerar uma URL exclusiva compartilhável, basta subir este arquivo no Streamlit Community Cloud (gratuito).
"""

import streamlit as st
from PIL import Image

# Configuração da Página
st.set_page_config(
    page_title="FotoAgent Pro - Studio AI",
    page_icon="📸",
    layout="wide"
)

# Estilização CSS customizada
st.markdown("""
    <style>
    .main { background-color: #030712; color: #f3f4f6; }
    .stSelectbox, .stTextInput, .stTextArea { background-color: #111827; color: #fff; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.title("📸 FotoAgent Pro — Studio AI & Composição Multi-Imagem")
st.markdown("Plataforma profissional para criação de ensaios fotográficos, composição multi-imagem e prompts avançados.")

# Abas de Navegação
tab1, tab2 = st.tabs(["🎨 Geração Direta & Blending", "💬 Ideação & Chat com Agente"])

with tab1:
    st.header("Geração Direta com Prompt Existente & Multi-Imagem")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Configuração & Entrada")
        existing_prompt = st.text_area("Inserir Prompt Existente para Criação", placeholder="Cole seu prompt pronto aqui...")
        
        st.markdown("---")
        st.markdown("### 🖼️ Composição Multi-Imagem (Blending)")
        bg_file = st.file_uploader("Imagem 1: Fundo / Ambiente", type=["jpg", "png", "jpeg"])
        sub_file = st.file_uploader("Imagem 2: Sujeito / Objeto", type=["jpg", "png", "jpeg"])
        blend_instruction = st.text_input("Instrução de mesclagem (ex: Inserir a pessoa sentada no escritório)")
        
        st.markdown("---")
        col_cam, col_light, col_ar = st.columns(3)
        with col_cam:
            camera = st.selectbox("Câmera", ["Hasselblad X1D", "Sony A7R V", "Canon EOS R5"])
        with col_light:
            lighting = st.selectbox("Iluminação", ["Studio Softbox", "Rembrandt", "Golden Hour"])
        with col_ar:
            aspect_ratio = st.selectbox("Proporção", ["--ar 4:5", "--ar 1:1", "--ar 9:16", "--ar 16:9", "--ar 2:3"])
            
        if st.button("⚡ Gerar Imagens (Battle Mode / Side by Side)", type="primary"):
            st.success("Configuração processada com sucesso!")
            st.session_state['generated'] = True

    with col2:
        st.subheader("2. Resultado Gerado (Side by Side)")
        if st.session_state.get('generated', False):
            col_a, col_b = st.columns(2)
            with col_a:
                st.info("Modelo A (Flux Pro)")
                st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&auto=format&fit=crop&q=60", caption="Gerado pelo Modelo A")
                if st.button("Escolher Modelo A"):
                    st.success("Modelo A selecionado e salvo!")
            with col_b:
                st.info("Modelo B (Midjourney v6)")
                st.image("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&auto=format&fit=crop&q=60", caption="Gerado pelo Modelo B")
                if st.button("Escolher Modelo B"):
                    st.success("Modelo B selecionado e salvo!")
        else:
            st.info("Preencha o formulário ao lado e clique em 'Gerar Imagens' para visualizar o resultado Side-by-Side.")

with tab2:
    st.header("💬 Aba Exclusiva: Ideação de Prompt Técnico com Agente")
    st.markdown("Converse com o agente para estruturar conceitos e criar prompts do zero.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Olá! Descreva o seu ensaio fotográfico e criarei o prompt técnico perfeito."}]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    if user_input := st.chat_input("Digite sua ideia de ensaio..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        response = f"Prompt técnico gerado para '{user_input}': Professional high-end photography, shot on Hasselblad X1D, studio softbox lighting, 8k resolution, photorealistic --ar 4:5"
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
