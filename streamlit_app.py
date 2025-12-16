import streamlit as st
import threading
from humanizer import humanize

model_lock = threading.Lock()

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="AI Text Humanizer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------
if "output_text" not in st.session_state:
    st.session_state.output_text = ""

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# --------------------------------------------------
# Sidebar: API Key Input (NEW)
# --------------------------------------------------
with st.sidebar:
    st.markdown("### 🔐 API Configuration")
    api_key_input = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="Paste your API key here"
    )

    if api_key_input:
        st.session_state.api_key = api_key_input
        st.success("API key saved for this session")

# --------------------------------------------------
# Custom CSS (UNCHANGED)
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #020617;
        color: #e5e7eb;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    h1 {
        font-family: 'Inter', sans-serif;
        text-align: center;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0 !important;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }

    .stTextArea textarea {
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        font-size: 16px;
        line-height: 1.5;
    }

    div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        border-radius: 8px !important;
        border: 1px solid #475569 !important;
        color: white !important;
    }

    .stButton button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border: none;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("<h1>✨ AI Text Humanizer</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Rewrite text to sound natural, clear, and human-edited</p>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Main Layout (UNCHANGED)
# --------------------------------------------------
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    input_text = st.text_area(
        "✍️ Input Text",
        height=400,
        placeholder="Paste your text here..."
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        style = st.selectbox(
            "Tone",
            ["Professional", "Casual", "Friendly"],
            index=0,
            label_visibility="collapsed"
        )

    with c2:
        process_btn = st.button(
            "Humanize Text ✨",
            use_container_width=True,
            disabled=not bool(st.session_state.api_key)
        )

with col2:
    st.text_area(
        "🪄 Humanized Result",
        value=st.session_state.output_text,
        height=400,
        placeholder="The result will appear here..."
    )

# --------------------------------------------------
# Logic
# --------------------------------------------------
if process_btn:
    if not input_text.strip():
        st.toast("⚠️ Please enter some text first!", icon="⚠️")

    elif not st.session_state.api_key:
        st.toast("🔑 Please enter your API key in the sidebar.", icon="🔑")

    else:
        with st.spinner("Rewriting..."):
            try:
                with model_lock:
                    result = humanize(
                        input_text,
                        style=style.lower(),
                        api_key=st.session_state.api_key
                    )

                st.session_state.output_text = result
                st.rerun()

            except Exception as e:
                st.error(str(e))
