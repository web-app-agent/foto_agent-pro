"""
FotoAgent Pro - Streamlit App (UI Aprimorada com Alto Contraste e Textareas Maiores)
"""

import streamlit as st
from PIL import Image

# Configuração da Página
st.set_page_config(
    page_title="FotoAgent Pro - Arena.ai Studio",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Customizada (Alto Contraste, Textareas Maiores e Uploaders Destacados)
st.markdown("""
    <style>
    /* Fundo Geral */
    .stApp {
        background-color: #030712;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Legendas e Labels com Alto Contraste */
    .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* Placeholders mais claros e legíveis */
    ::placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }

    /* Inputs, Textareas e Selects */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #0b0f19 !important;
        border: 1px solid #334155 !important;
        color: #ffffff !important;
        border-radius: 0.75rem !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 1px #6366f1 !important;
    }

    /* File Uploaders com Alto Contraste */
    [data-baseweb="file-uploader"] {
        background-color: #0b0f19 !important;
        border: 2px dashed #475569 !important;
        border-radius: 0.75rem !important;
        padding: 10px !important;
    }
    [data-baseweb="file-uploader"] button {
        background-color: #4f46e5 !important;
        color: white !important;
        border-radius: 0.5rem !important;
        font-weight: 600 !important;
    }
    [data-baseweb="file-uploader"] span, [data-baseweb="file-uploader"] small {
        color: #cbd5e1 !important;
    }

    /* Estilização de Abas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0b0f19;
        padding: 6px;
        border-radius: 0.75rem;
        border: 1px solid #1e293b;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        color: #cbd5e1;
        border-radius: 0.5rem;
        font-weight: 600;
        font-size: 13px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4f46e5 !important;
        color: white !important;
    }

    /* Botões */
    .stButton button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        border-radius: 0.75rem;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        opacity: 0.9;
        transform: translateY(-1px);
        box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.4);
    }
    
    /* Header Principal */
    .hero-container {
        background: linear-gradient(90deg, #0f172a 0%, #1e1b4b 50%, #030712 100%);
        padding: 2rem;
        border-radius: 1rem;
        border: 1px solid #1e293b;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO HERO ---
st.markdown("""
    <div class="hero-container">
        <h1 style="color: #ffffff; font-size: 26px; margin-bottom: 5px; display: flex; align-items: center; gap: 10px;">
            <span>📸</span> FotoAgent Pro <span style="font-size: 11px; background: rgba(79, 70, 229, 0.2); color: #818cf8; padding: 4px 10px; border-radius: 20px; border: 1px solid rgba(79, 70, 229, 0.3);">Arena.ai Studio Edition</span>
        </h1>
        <p style="color: #cbd5e1; font-size: 14px; margin: 0;">Plataforma Profissional de Ensaios Fotográficos, Composição Multi-Imagem & Battle Mode (Side-by-Side)</p>
    </div>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO POR ABAS ---
tab1, tab2 = st.tabs(["🎨 Geração Direta & Blending", "💬 Ideação & Chat de Agente"])

# ==========================================
# ABA 1: GERAÇÃO DIRETA & MULTI-IMAGEM
# ==========================================
with tab1:
    col_left, col_right = st.columns([1.1, 1], gap="large")
    
    with col_left:
        st.markdown("### ⚙️ 1. Configuração & Prompt de Entrada")
        
        # Campo de prompt expandido verticalmente (height=160)
        existing_prompt = st.text_area(
            "Inserir Prompt Existente para Criação", 
            placeholder="Cole seu prompt pronto aqui (ex: Professional high-end photography of a stylish model in an urban studio...)",
            height=160
        )
        
        st.markdown("---")
        st.markdown("### 🖼️ Composição Multi-Imagem (Blending)")
        st.markdown("<p style='font-size: 13px; color: #cbd5e1; margin-top: -10px;'>Insira um fundo e um sujeito para mesclagem fotorrealista.</p>", unsafe_allow_html=True)
        
        blend_col1, blend_col2 = st.columns(2)
        with blend_col1:
            bg_file = st.file_uploader("📁 Imagem 1: Fundo / Ambiente", type=["jpg", "png", "jpeg"], key="bg_upload")
        with blend_col2:
            sub_file = st.file_uploader("📁 Imagem 2: Sujeito / Objeto", type=["jpg", "png", "jpeg"], key="sub_upload")
            
        blend_note = st.text_input("Instrução de Mesclagem", placeholder="Ex: Inserir a pessoa sentada confortavelmente na cadeira...")
        
        st.markdown("---")
        param_col1, param_col2, param_col3 = st.columns(3)
        with param_col1:
            camera = st.selectbox("Câmera", ["Hasselblad X1D", "Sony A7R V", "Canon EOS R5"])
        with param_col2:
            lighting = st.selectbox("Iluminação", ["Studio Softbox", "Rembrandt", "Golden Hour"])
        with param_col3:
            aspect_ratio = st.selectbox("Proporção", ["--ar 4:5", "--ar 1:1", "--ar 9:16", "--ar 16:9", "--ar 2:3"])
            
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        if st.button("⚔️ Gerar Imagens (Battle Mode / Side by Side)", use_container_width=True):
            st.session_state['generated'] = True
            st.success("Configuração processada e enviada para os modelos de IA!")

    with col_right:
        st.markdown("### ⚔️ 2. Resultado Gerado (Arena Battle)")
        st.markdown("<p style='font-size: 13px; color: #cbd5e1; margin-top: -10px;'>Compare duas opções de IAs distintas e escolha a melhor.</p>", unsafe_allow_html=True)
        
        if st.session_state.get('generated', False):
            res_col1, res_col2 = st.columns(2)
            
            with res_col1:
                st.markdown("<div style='background: #0b0f19; padding: 12px; border-radius: 12px; border: 1px solid #334155; text-align: center;'>", unsafe_allow_html=True)
                st.markdown("<strong style='color: #818cf8; font-size: 13px;'>Modelo A (Flux Pro)</strong>", unsafe_allow_html=True)
                st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&auto=format&fit=crop&q=60", use_column_width=True)
                if st.button("Escolher Modelo A", key="btn_a"):
                    st.success("🎉 Modelo A escolhido e salvo no workspace!")
                st.markdown("</div>", unsafe_allow_html=True)
                
            with res_col2:
                st.markdown("<div style='background: #0b0f19; padding: 12px; border-radius: 12px; border: 1px solid #334155; text-align: center;'>", unsafe_allow_html=True)
                st.markdown("<strong style='color: #a78bfa; font-size: 13px;'>Modelo B (Midjourney v6)</strong>", unsafe_allow_html=True)
                st.image("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&auto=format&fit=crop&q=60", use_column_width=True)
                if st.button("Escolher Modelo B", key="btn_b"):
                    st.success("🌟 Modelo B escolhido e salvo no workspace!")
                st.markdown("</div>", unsafe_allow_html=True)
                
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            if st.button("✨ Iniciar Novo Chat / Nova Imagem", use_container_width=True):
                st.session_state['generated'] = False
                st.rerun()
        else:
            st.markdown("""
                <div style='background: #0b0f19; border: 2px dashed #334155; border-radius: 1rem; height: 380px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #94a3b8; text-align: center; padding: 20px;'>
                    <span style='font-size: 32px; margin-bottom: 10px;'>🖼️</span>
                    <p style='font-size: 13px; margin: 0;'>Preencha o briefing ou prompt ao lado e clique em <b>Gerar Imagens</b> para iniciar o Arena Battle.</p>
                </div>
            """, unsafe_allow_html=True)

# ==========================================
# ABA 2: IDEAÇÃO & CHAT DE AGENTE
# ==========================================
with tab2:
    st.markdown("### 💬 Aba Exclusiva: Ideação & Criação de Prompt Técnico com Agente")
    st.markdown("<p style='font-size: 13px; color: #cbd5e1;'>Converse com o agente para estruturar conceitos, definir iluminação e gerar prompts profissionais do zero.</p>", unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_data = [] # safe init
        st.session_state.messages = [
            {"role": "assistant", "content": "Olá! Sou o FotoAgent Pro. Descreva o ensaio fotográfico que você tem em mente e criarei o prompt técnico perfeito."}
        ]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    if user_input := st.chat_input("Digite sua ideia de ensaio fotográfico..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        agent_reply = f"**Prompt Técnico Gerado:**\n`Professional high-end photography of {user_input}, shot on Hasselblad X1D II 50C, studio softbox lighting, 8k resolution, photorealistic, professional color grading --ar 4:5 --v 6.0`"
        st.session_state.messages.append({"role": "assistant", "content": agent_reply})
        with st.chat_message("assistant"):
            st.markdown(agent_reply)
