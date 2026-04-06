import streamlit as st

# PAGE CONFIG
st.set_page_config(page_title="SpendSense", layout="wide")

# CSS (FIXED LIGHT + DARK MODE)
st.markdown("""
<style>

/* DARK MODE ONLY */
@media (prefers-color-scheme: dark) {
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }

    input, textarea, select {
        background-color: rgba(255,255,255,0.08) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        color: white !important;
        padding: 10px !important;
    }
}

/* LIGHT MODE ONLY */
@media (prefers-color-scheme: light) {
    .stApp {
        background: #f5f7fb;
        color: #111 !important;
    }

    input, textarea, select {
        background-color: white !important;
        border-radius: 10px !important;
        border: 1px solid #ccc !important;
        color: black !important;
        padding: 10px !important;
    }
}

/* COMMON STYLING (UNCHANGED) */

.app-title {
    text-align: center;
    width: 100%;
    color: #A8E6CF;
    font-weight: 800;
    font-size: 48px;
    margin-bottom: 10px;
    text-shadow: 0px 0px 8px rgba(168, 230, 207, 0.3);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
    max-width: 950px;
    margin: auto;
}

.stForm {
    border-radius: 18px;
    padding: 30px;
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
}

input:focus, textarea:focus {
    border: 1px solid #A8E6CF !important;
    box-shadow: 0px 0px 8px rgba(168,230,207,0.4) !important;
}

div[data-testid="column"] {
    padding: 6px;
}

.stButton > button {
    background: linear-gradient(135deg, #6C63FF, #A8E6CF);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 10px rgba(168,230,207,0.5);
}

button[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #A8E6CF !important;
}

</style>
""", unsafe_allow_html=True)

# IMPORTS
from add_update_UI import add_update_tab
from analytics_ui import analytics_tab

# TITLE
st.markdown('<h1 class="app-title">💸 SpendSense</h1>', unsafe_allow_html=True)

# TABS
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()