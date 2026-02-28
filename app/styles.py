"""
All CSS styles for the MediAssist RAG Streamlit app.

Centralised here so main.py stays lean.  The single public function
`inject_css()` writes the <style> block into the page via
`st.markdown(unsafe_allow_html=True)`.

Design tokens
─────────────
Background    : #ffffff (white)
Surface       : #f8fafc
Border        : #e2e8f0
Primary       : #0e7490  (teal-700)
Primary hover : #0c5e73
Accent green  : #16a34a / #22c55e
Text dark     : #0f172a
Text muted    : #64748b / #94a3b8
"""

import streamlit as st

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ══════════════════════════════════════
   BASE
   ══════════════════════════════════════ */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
#MainMenu, footer, header { visibility: hidden; }

/* White background everywhere */
.stApp, .main, section[data-testid="stSidebar"],
[data-testid="stAppViewBlockContainer"] {
    background-color: #ffffff !important;
}
.main .block-container {
    padding-top: 1.25rem;
    padding-bottom: 3rem;
    max-width: 1120px;
}

/* ══════════════════════════════════════
   HERO / HEADER
   ══════════════════════════════════════ */
.app-header {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.25rem 1.75rem;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.header-icon {
    flex-shrink: 0;
    width: 44px;
    height: 44px;
    background: #0e7490;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px rgba(14,116,144,0.15);
}
.header-icon svg { width: 24px; height: 24px; }
.header-icon svg path, .header-icon svg circle { fill: #ffffff; }
.header-text { flex: 1; }
.app-title {
    font-size: 1.3rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.03em;
    margin: 0;
    line-height: 1.2;
}
.app-meta {
    font-size: 0.76rem;
    color: #64748b;
    margin-top: 0.25rem;
    font-weight: 400;
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
}
.meta-sep { color: #cbd5e1; }
.app-badge {
    display: inline-block;
    background: #fefce8;
    color: #854d0e;
    border: 1px solid #fde047;
    border-radius: 5px;
    font-size: 0.6rem;
    font-weight: 700;
    padding: 2px 8px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* ══════════════════════════════════════
   SECTION LABELS
   ══════════════════════════════════════ */
.section-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* ══════════════════════════════════════
   PATIENT FORM
   ══════════════════════════════════════ */
div[data-testid="stForm"] {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.75rem 2rem 1.25rem 2rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.03);
}

/* Labels */
div[data-testid="stForm"] label {
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: #1e293b !important;
    letter-spacing: 0.01em;
    margin-bottom: 4px !important;
}

/* Text inputs + textareas */
div[data-testid="stForm"] input,
div[data-testid="stForm"] textarea {
    background: #f8fafc !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 10px !important;
    font-size: 0.86rem !important;
    color: #0f172a !important;
    padding: 0.65rem 0.9rem !important;
    line-height: 1.5 !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease !important;
}
div[data-testid="stForm"] input::placeholder,
div[data-testid="stForm"] textarea::placeholder {
    color: #94a3b8 !important;
    font-weight: 400 !important;
}
div[data-testid="stForm"] input:focus,
div[data-testid="stForm"] textarea:focus {
    background: #ffffff !important;
    border-color: #0e7490 !important;
    box-shadow: 0 0 0 3px rgba(14,116,144,0.10) !important;
    outline: none !important;
}
div[data-testid="stForm"] input:hover,
div[data-testid="stForm"] textarea:hover {
    border-color: #cbd5e1 !important;
}

/* Select box */
/* Select box - Main Container */
div[data-testid="stForm"] div[data-baseweb="select"] > div {
    background: #ffffff !important; /* Changed to Pure White */
    border-radius: 10px !important;
    border: 1.5px solid #e2e8f0 !important;
    min-height: 42px !important;
    transition: all 0.2s ease !important;
}

/* Force text to be Slate-Black (#0f172a) */
div[data-testid="stForm"] div[data-baseweb="select"] span, 
div[data-testid="stForm"] div[data-baseweb="select"] div {
    color: #0f172a !important;
    font-weight: 500 !important;
}

/* Hover State */
div[data-testid="stForm"] div[data-baseweb="select"] > div:hover {
    border-color: #cbd5e1 !important;
}

/* Focus State */
div[data-testid="stForm"] div[data-baseweb="select"] > div:focus-within {
    background: #ffffff !important;
    border-color: #0e7490 !important;
    box-shadow: 0 0 0 3px rgba(14,116,144,0.10) !important;
}

/* Target the actual Dropdown Menu (The pop-over list) */
div[data-baseweb="menu"] {
    background-color: #ffffff !important;
}

div[data-baseweb="option"] {
    color: #0f172a !important;
    background-color: #ffffff !important;
}

div[data-baseweb="option"]:hover {
    background-color: #f1f5f9 !important; /* Light gray highlight on hover */
}

/* Number input */
div[data-testid="stForm"] div[data-testid="stNumberInput"] input {
    border-radius: 10px !important;
    min-height: 42px !important;
}
div[data-testid="stForm"] div[data-testid="stNumberInput"] button {
    border-radius: 8px !important;
    border: 1px solid #e2e8f0 !important;
    background: #f8fafc !important;
    color: #475569 !important;
    transition: background 0.15s ease !important;
}
div[data-testid="stForm"] div[data-testid="stNumberInput"] button:hover {
    background: #f0fdfa !important;
    border-color: #0e7490 !important;
    color: #0e7490 !important;
}

/* ══════════════════════════════════════
   SUBMIT BUTTON
   ══════════════════════════════════════ */
.stFormSubmitButton > button {
    background: linear-gradient(135deg, #0e7490 0%, #0891b2 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    padding: 0.7rem 2rem !important;
    letter-spacing: 0.02em;
    transition: all 0.2s ease !important;
    width: 100%;
    box-shadow: 0 2px 8px rgba(14,116,144,0.18) !important;
}
.stFormSubmitButton > button:hover {
    background: linear-gradient(135deg, #0c5e73 0%, #0e7490 100%) !important;
    box-shadow: 0 4px 16px rgba(14,116,144,0.28) !important;
    transform: translateY(-1px);
}
.stFormSubmitButton > button:active {
    transform: translateY(0px);
    box-shadow: 0 1px 4px rgba(14,116,144,0.15) !important;
}

/* ══════════════════════════════════════
   STREAM BOX (live JSON output)
   ══════════════════════════════════════ */
.stream-box {
    background: #0f172a;
    color: #a5b4c8;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'Courier New', monospace;
    font-size: 0.76rem;
    line-height: 1.75;
    white-space: pre-wrap;
    word-break: break-word;
    min-height: 80px;
    border: 1px solid #1e293b;
    position: relative;
    overflow: hidden;
}
.stream-box::before {
    content: 'AI Processing';
    position: absolute;
    top: 0; right: 0;
    background: #1e293b;
    color: #475569;
    font-family: 'Inter', sans-serif;
    font-size: 0.6rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 0 12px 0 6px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ══════════════════════════════════════
   TABS
   ══════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    gap: 2px;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 0;
    background: transparent;
}
.stTabs [data-baseweb="tab"] {
    font-size: 0.8rem;
    font-weight: 500;
    color: #64748b;
    padding: 0.5rem 1.1rem;
    border-radius: 8px 8px 0 0;
    border: none;
    background: transparent;
    transition: all 0.15s ease;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #0e7490;
    background: #f0fdfa;
}
.stTabs [aria-selected="true"] {
    color: #0e7490 !important;
    border-bottom: 2.5px solid #0e7490 !important;
    font-weight: 700;
    background: #f0fdfa;
}
div[data-testid="stTabPanel"] {
    padding-top: 1.25rem;
}

/* ══════════════════════════════════════
   DIAGNOSIS CARDS
   ══════════════════════════════════════ */
.dx-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.1rem 1.35rem;
    margin-bottom: 0.75rem;
    transition: box-shadow 0.2s ease, border-color 0.2s ease;
}
.dx-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    border-color: #cbd5e1;
}
.dx-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.55rem;
}
.dx-name {
    font-size: 0.88rem;
    font-weight: 700;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 6px;
}
.dx-num {
    width: 22px; height: 22px;
    border-radius: 6px;
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    color: #0369a1;
    font-size: 0.65rem;
    font-weight: 800;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.badge-high   { background:#dcfce7; color:#166534; border:1px solid #bbf7d0; border-radius:5px; font-size:0.65rem; font-weight:700; padding:3px 10px; letter-spacing:0.06em; }
.badge-medium { background:#fff7ed; color:#9a3412; border:1px solid #fdba74; border-radius:5px; font-size:0.65rem; font-weight:700; padding:3px 10px; letter-spacing:0.06em; }
.badge-low    { background:#fef2f2; color:#991b1b; border:1px solid #fca5a5; border-radius:5px; font-size:0.65rem; font-weight:700; padding:3px 10px; letter-spacing:0.06em; }
.dx-reasoning {
    font-size: 0.82rem;
    color: #475569;
    line-height: 1.7;
}

/* ══════════════════════════════════════
   LIST ITEMS  (info / warn / red-flag)
   ══════════════════════════════════════ */
.info-item {
    background: #f0fdfa;
    border-left: 3px solid #0e7490;
    border-radius: 0 8px 8px 0;
    padding: 0.75rem 1.1rem;
    margin-bottom: 0.6rem;
    font-size: 0.82rem;
    color: #134e4a;
    line-height: 1.6;
    display: flex;
    align-items: flex-start;
    gap: 8px;
    transition: background 0.15s ease;
}
.info-item:hover { background: #e0fdf6; }
.info-icon { flex-shrink: 0; margin-top: 1px; }

.warn-item {
    background: #fffbeb;
    border-left: 3px solid #f59e0b;
    border-radius: 0 8px 8px 0;
    padding: 0.75rem 1.1rem;
    margin-bottom: 0.6rem;
    font-size: 0.82rem;
    color: #78350f;
    line-height: 1.6;
    display: flex;
    align-items: flex-start;
    gap: 8px;
    transition: background 0.15s ease;
}
.warn-item:hover { background: #fef3c7; }

.red-flag-item {
    background: #fef2f2;
    border-left: 3px solid #dc2626;
    border-radius: 0 8px 8px 0;
    padding: 0.75rem 1.1rem;
    margin-bottom: 0.6rem;
    font-size: 0.82rem;
    color: #7f1d1d;
    line-height: 1.6;
    display: flex;
    align-items: flex-start;
    gap: 8px;
    transition: background 0.15s ease;
}
.red-flag-item:hover { background: #fee2e2; }

.empty-state {
    background: #f8fafc;
    border: 1px dashed #cbd5e1;
    border-radius: 12px;
    padding: 2rem 1.5rem;
    text-align: center;
    font-size: 0.82rem;
    color: #94a3b8;
}

/* ══════════════════════════════════════
   SOURCES
   ══════════════════════════════════════ */
.sources-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 0.5rem;
}
.source-chip {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    font-size: 0.68rem;
    font-weight: 500;
    color: #475569;
    padding: 3px 12px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: background 0.15s ease;
}
.source-chip:hover { background: #e2e8f0; }

/* ══════════════════════════════════════
   MISC
   ══════════════════════════════════════ */
.divider {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 1.75rem 0;
}
.disclaimer {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 0.85rem 1.15rem;
    font-size: 0.73rem;
    color: #94a3b8;
    line-height: 1.65;
    margin-top: 1.75rem;
    display: flex;
    align-items: flex-start;
    gap: 8px;
}
.analysis-header {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 12px;
    padding: 0.85rem 1.25rem;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 1.25rem;
}
.status-dot {
    width: 9px; height: 9px;
    background: #22c55e;
    border-radius: 50%;
    display: inline-block;
    box-shadow: 0 0 6px rgba(34,197,94,0.4);
    animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 6px rgba(34,197,94,0.4); }
    50%      { box-shadow: 0 0 12px rgba(34,197,94,0.6); }
}
.analysis-title {
    font-size: 0.88rem;
    font-weight: 700;
    color: #166534;
}

/* ── Hero banner (above form) ── */
.hero-banner {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 1rem 1.35rem;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.03);
}
.hero-text {
    font-size: 0.82rem;
    color: #475569;
    line-height: 1.55;
}
.hero-text strong {
    color: #0f172a;
    font-weight: 700;
}

/* ══════════════════════════════════════
   EVIDENCE PANEL
   ══════════════════════════════════════ */
.evidence-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    transition: box-shadow 0.2s ease, border-color 0.2s ease;
}
.evidence-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    border-color: #cbd5e1;
}
.evidence-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 0.5rem;
}
.evidence-idx {
    width: 22px; height: 22px;
    border-radius: 6px;
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    color: #0369a1;
    font-size: 0.65rem;
    font-weight: 800;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.evidence-source {
    font-size: 0.76rem;
    font-weight: 600;
    color: #334155;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    flex: 1;
}
.evidence-score {
    font-size: 0.7rem;
    font-weight: 600;
    color: #64748b;
    flex-shrink: 0;
}
.score-track {
    height: 4px;
    background: #f1f5f9;
    border-radius: 4px;
    margin-bottom: 0.65rem;
    overflow: hidden;
}
.score-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.4s ease;
}
.score-bar-high { background: #22c55e; }
.score-bar-med  { background: #f59e0b; }
.score-bar-low  { background: #ef4444; }
.evidence-text {
    font-size: 0.8rem;
    color: #475569;
    line-height: 1.7;
    background: #f8fafc;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    border: 1px solid #f1f5f9;
}

/* ══════════════════════════════════════
   RETRIEVAL STRENGTH BADGE
   ══════════════════════════════════════ */
.rs-badge-wrapper {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
}
.rs-label {
    font-size: 0.65rem;
    font-weight: 600;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
.rs-track {
    width: 60px;
    height: 5px;
    background: #f1f5f9;
    border-radius: 5px;
    overflow: hidden;
}
.rs-fill {
    height: 100%;
    border-radius: 5px;
    transition: width 0.4s ease;
}
.rs-fill.rs-strong  { background: #22c55e; }
.rs-fill.rs-moderate { background: #f59e0b; }
.rs-fill.rs-weak    { background: #ef4444; }
.rs-value {
    font-size: 0.72rem;
    font-weight: 700;
    color: #334155;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
.rs-tag {
    font-size: 0.58rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 5px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.rs-tag.rs-strong  { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
.rs-tag.rs-moderate { background: #fff7ed; color: #9a3412; border: 1px solid #fdba74; }
.rs-tag.rs-weak    { background: #fef2f2; color: #991b1b; border: 1px solid #fca5a5; }

/* ══════════════════════════════════════
   LATENCY BAR
   ══════════════════════════════════════ */
.lat-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    margin-bottom: 1.25rem;
}
.lat-title {
    font-size: 0.62rem;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-right: 4px;
}
.lat-pill {
    font-size: 0.68rem;
    font-weight: 500;
    color: #475569;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 2px 10px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
.lat-total {
    margin-left: auto;
    font-size: 0.68rem;
    font-weight: 700;
    color: #0e7490;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
}

/* ══════════════════════════════════════
   DRUG INTERACTION CARDS
   ══════════════════════════════════════ */
.drug-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    transition: box-shadow 0.2s ease, border-color 0.2s ease;
}
.drug-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    border-color: #fde68a;
}
.drug-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
}
.drug-name {
    font-size: 0.84rem;
    font-weight: 700;
    color: #78350f;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}
.drug-detail {
    font-size: 0.8rem;
    color: #475569;
    line-height: 1.7;
}
.badge-high-drug { background:#fef2f2; color:#991b1b; border:1px solid #fca5a5; border-radius:5px; font-size:0.65rem; font-weight:700; padding:3px 10px; letter-spacing:0.06em; }
.badge-mod-drug  { background:#fff7ed; color:#9a3412; border:1px solid #fdba74; border-radius:5px; font-size:0.65rem; font-weight:700; padding:3px 10px; letter-spacing:0.06em; }
.badge-low-drug  { background:#f0fdf4; color:#166534; border:1px solid #bbf7d0; border-radius:5px; font-size:0.65rem; font-weight:700; padding:3px 10px; letter-spacing:0.06em; }
</style>
"""


def inject_css() -> None:
    """Write the global <style> tag into the Streamlit page."""
    st.markdown(_CSS, unsafe_allow_html=True)
