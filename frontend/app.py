import streamlit as st

# PAGE CONFIG
st.set_page_config(page_title="SpendSense", layout="wide")

st.markdown("""
<style>

/* ===== DARK MODE ===== */
.stApp[data-theme="dark"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.stApp[data-theme="dark"] input,
.stApp[data-theme="dark"] textarea,
.stApp[data-theme="dark"] select {
    background-color: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
}

/* ===== LIGHT MODE ===== */
.stApp[data-theme="light"] {
    background: #f5f7fb;
    color: #111 !important;
}

.stApp[data-theme="light"] input,
.stApp[data-theme="light"] textarea,
.stApp[data-theme="light"] select {
    background-color: white !important;
    border: 1px solid #ccc !important;
    color: black !important;
}

/* ===== KEEP YOUR DESIGN SAME ===== */

.app-title {
    text-align: center;
    width: 100%;
    color: #A8E6CF;
    font-weight: 800;
    font-size: 48px;
    margin-bottom: 10px;
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
}

.stButton > button {
    background: linear-gradient(135deg, #6C63FF, #A8E6CF);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
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