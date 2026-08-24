import streamlit as st

def apply_custom_css():
    st.markdown("""
<style>
/* ── Premium CSS ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

/* ── Typography and Background ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}
.stApp {
    background: linear-gradient(135deg, #0f111a 0%, #171923 100%) !important;
}

/* ── Main content width and padding ── */
.main { min-height: 100vh !important; }
.main .block-container {
    min-height: calc(100vh - 60px) !important;
    padding-top: 1.5rem !important;
    padding-bottom: 40px !important;
    display: flex !important;
    flex-direction: column !important;
}
section.main > div { min-height: 100vh !important; }

/* ── Main title ── */
.hero-title {
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 50%, #34d399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.2rem;
    font-weight: 900;
    line-height: 1.1;
    text-align: center;
    margin: 0;
}
.hero-subtitle {
    color: #64748b;
    font-size: 1.05rem;
    text-align: center;
    margin-top: 8px;
    margin-bottom: 32px;
}

/* ── Hide Sidebar collapse buttons ── */
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapseButton"],
button[aria-label="Close sidebar"],
button[aria-label="Collapse sidebar"],
button[aria-label="open sidebar"],
button[title="Collapse sidebar"] { display: none !important; }

/* ── Sidebar estilo ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d24 0%, #0f0f2d 100%) !important;
    border-right: 1px solid rgba(124, 58, 237, 0.25) !important;
}
[data-testid="stSidebar"] * { color: #cbd5e1 !important; }

/* ── Ajuste equilibrado de espacios en el sidebar ── */
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 16px !important;
}
[data-testid="stSidebar"] hr {
    margin: 12px 0 !important;
    border-color: rgba(124, 58, 237, 0.15) !important;
}
[data-testid="stSidebar"] [data-testid="stMetric"] {
    padding: 12px 14px !important;
    margin-bottom: 8px !important;
}
[data-testid="stSidebar"] .stSelectbox {
    margin-bottom: 4px !important;
}

/* ── Sidebar section header ── */
.sidebar-header {
    color: #a78bfa !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    margin: 4px 0 2px !important;
}

/* ── Cards ── */
.glass-card {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 28px;
    margin: 12px 0;
    transition: border-color 0.3s ease;
}
.glass-card:hover { border-color: rgba(124, 58, 237, 0.3); }

/* ── History item ── */
.history-item {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 14px;
    padding: 16px 20px;
    margin: 8px 0;
    cursor: pointer;
    transition: all 0.25s ease;
}
.history-item:hover {
    background: rgba(124, 58, 237, 0.1);
    border-color: rgba(124, 58, 237, 0.4);
    transform: translateX(4px);
}
.history-meta {
    color: #64748b;
    font-size: 0.78rem;
    margin-top: 4px;
}
.history-preview {
    color: #94a3b8;
    font-size: 0.9rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 24px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.35) !important;
    letter-spacing: 0.01em !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(124, 58, 237, 0.55) !important;
}
.stDownloadButton > button {
    background: rgba(255, 255, 255, 0.07) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
    box-shadow: none !important;
}
.stDownloadButton > button:hover {
    background: rgba(124, 58, 237, 0.2) !important;
    border-color: rgba(124, 58, 237, 0.5) !important;
    transform: translateY(-2px) !important;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    background: rgba(124, 58, 237, 0.04) !important;
    border: 2px dashed rgba(124, 58, 237, 0.35) !important;
    border-radius: 18px !important;
    padding: 12px !important;
    transition: all 0.3s ease !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(124, 58, 237, 0.7) !important;
    background: rgba(124, 58, 237, 0.08) !important;
}

/* ── iframes (Custom Components like audio recorder) ── */
iframe { background-color: transparent !important; }
[data-testid="stIFrame"] { background-color: transparent !important; }

/* ── Text area ── */
.stTextArea textarea {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 14px !important;
    color: #e2e8f0 !important;
    font-size: 15px !important;
    line-height: 1.75 !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextArea textarea:focus {
    border-color: rgba(124, 58, 237, 0.6) !important;
    box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.12) !important;
}

/* ── Progress bar & Metric & Tabs ── */
.stProgress > div > div {
    background: linear-gradient(90deg, #7c3aed, #60a5fa, #34d399) !important;
    border-radius: 999px !important;
    background-size: 200% 100% !important;
    animation: shimmer 1.5s infinite linear !important;
}
@keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 14px !important;
}
[data-testid="stMetricValue"] { color: #a78bfa !important; font-weight: 700 !important; }
[data-testid="stMetricLabel"] { color: #64748b !important; }

.stTabs [data-baseweb="tab-list"] {
    background: rgba(255, 255, 255, 0.03) !important;
    border-radius: 18px !important;
    padding: 6px !important;
    gap: 8px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 13px !important;
    color: #64748b !important;
    font-weight: 600 !important;
    padding: 14px 32px !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #a78bfa !important;
    background: rgba(124, 58, 237, 0.08) !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: white !important;
}
hr { border-color: rgba(255, 255, 255, 0.07) !important; }
</style>
    """, unsafe_allow_html=True)
