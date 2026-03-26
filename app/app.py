import streamlit as st
import joblib
import sys
import os
from pathlib import Path

# Fix import path BEFORE importing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import preprocess_text

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://github.com",
        "Report a bug": "https://github.com",
        "About": "Fake News Detection System"
    }
)

# ================== THEME CONFIGURATION ==================
# Single fixed theme (dark) - remove switching logic
colors = {
    "bg_primary": "#0f172a",
    "bg_secondary": "#1e293b",
    "bg_tertiary": "#334155",
    "text_primary": "#f1f5f9",
    "text_secondary": "#cbd5e1",
    "accent_primary": "#3b82f6",
    "accent_secondary": "#8b5cf6",
    "success": "#10b981",
    "danger": "#ef4444",
    "border": "rgba(148, 163, 184, 0.2)",
    "shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.5)",
}

# Ensure persistent input state
if "article_input" not in st.session_state:
    st.session_state.article_input = ""

# Clear callback to avoid direct state mutation after widget init
def clear_article_input():
    st.session_state.article_input = ""

# ================== CUSTOM CSS STYLING ==================
def load_modern_css():
    """Load modern premium SaaS CSS styling"""
    st.markdown(f"""
    <style>
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    html, body {{
        background-color: {colors['bg_primary']};
        color: {colors['text_primary']};
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
    }}
    
    .main {{
        background-color: {colors['bg_primary']};
    }}
    
    .main .block-container {{
        padding: 0;
        max-width: 100%;
    }}
    
    section[data-testid="stSidebar"] {{
        display: none;
    }}
    
    /* Navigation Bar */
    .navbar {{
        position: sticky;
        top: -8px;
        z-index: 100;
        background: {colors['bg_secondary']};
        border-bottom: 1px solid {colors['border']};
        backdrop-filter: blur(10px);
        box-shadow: {colors['shadow']};
        margin-bottom: 1rem;
    }}
    
    .navbar-content {{
        max-width: 1600px;
        margin: 0 auto;
        padding: 0.85rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 2rem;
    }}

    .main-container {{
        margin-top: 1.5rem;
    }}
    
    .navbar-left {{
        display: flex;
        align-items: center;
        gap: 1rem;
    }}
    
    .navbar-logo {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {colors['accent_primary']};
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        transition: all 0.3s ease;
    }}
    
    .navbar-right {{
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }}
    
    .theme-toggle {{
        display: inline-flex;
        background: {colors['bg_tertiary']};
        border: 1px solid {colors['border']};
        border-radius: 24px;
        padding: 0.25rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    
    .theme-btn {{
        width: 36px;
        height: 36px;
        border: none;
        background: transparent;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        border-radius: 20px;
        transition: all 0.3s ease;
    }}
    
    .theme-btn.active {{
        background: {colors['accent_primary']};
        color: white;
    }}
    
    .avatar {{
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: linear-gradient(135deg, {colors['accent_primary']}, {colors['accent_secondary']});
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }}
    
    /* Main Layout Container */
    .main-container {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2.5rem;
        max-width: 1600px;
        margin: 0 auto;
        padding: 1.5rem;
        height: auto;
    }}
    
    @media (max-width: 1024px) {{
        .main-container {{
            grid-template-columns: 1fr;
            height: auto;
            gap: 1.5rem;
        }}
    }}
    
    /* Panel Styling */
    .panel {{
        background: {colors['bg_secondary']};
        border: 1px solid {colors['border']};
        border-radius: 14px;
        padding: 1.4rem;
        display: flex;
        flex-direction: column;
        height: auto;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        animation: slideIn 0.5s ease-out;
        margin-bottom: 1.25rem;
    }}
    
    @keyframes slideIn {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .panel-title {{
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
        color: {colors['text_primary']};
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }}
    
    /* Text Input Styling */
    .input-wrapper {{
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }}
    
    textarea {{
        flex: 1;
        padding: 1rem;
        border: 2px solid {colors['border']};
        border-radius: 8px;
        background: {colors['bg_tertiary']};
        color: {colors['text_primary']};
        font-family: inherit;
        font-size: 0.95rem;
        line-height: 1.5;
        resize: none;
        transition: all 0.3s ease;
        outline: none;
        min-height: 250px;
    }}
    
    textarea:focus {{
        border-color: {colors['accent_primary']};
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }}
    
    /* Button Group */
    .button-group {{
        display: flex;
        gap: 1rem;
        margin-top: 1.5rem;
    }}
    
    .btn {{
        flex: 1;
        padding: 0.875rem 1.5rem;
        border: none;
        border-radius: 8px;
        font-size: 0.95rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }}
    
    .btn-primary {{
        background: linear-gradient(135deg, {colors['accent_primary']}, {colors['accent_secondary']});
        color: white;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }}
    
    .btn-primary:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }}
    
    /* Result Panel */
    .result-section {{
        display: flex;
        flex-direction: column;
        gap: 1.25rem;
        margin-top: 0.75rem;
    }}
    
    .result-card {{
        background: linear-gradient(135deg, {colors['bg_tertiary']}, {colors['bg_secondary']});
        border: 1px solid {colors['border']};
        border-radius: 14px;
        padding: 1.1rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        animation: slideIn 0.5s ease-out;
        margin-bottom: 1rem;
    }}
    
    .result-label {{
        display: block;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: {colors['text_secondary']};
        margin-bottom: 0.75rem;
    }}
    
    .prediction-badge {{
        display: inline-block;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-size: 1.25rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        min-width: 150px;
        text-align: center;
        animation: pulse 2s ease-in-out infinite;
    }}
    
    .badge-real {{
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(16, 185, 129, 0.1));
        color: {colors['success']};
        border: 2px solid {colors['success']};
    }}
    
    .badge-fake {{
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(239, 68, 68, 0.1));
        color: {colors['danger']};
        border: 2px solid {colors['danger']};
    }}
    
    @keyframes pulse {{
        0%, 100% {{
            opacity: 1;
        }}
        50% {{
            opacity: 0.8;
        }}
    }}
    
    /* Confidence Score */
    .confidence-label {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.9rem;
        font-weight: 600;
        color: {colors['text_secondary']};
        margin-bottom: 0.75rem;
    }}
    
    .confidence-value {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {colors['accent_primary']};
    }}
    
    .progress-bar {{
        width: 100%;
        height: 8px;
        background: {colors['bg_tertiary']};
        border-radius: 4px;
        overflow: hidden;
    }}
    
    .progress-fill {{
        height: 100%;
        background: linear-gradient(90deg, {colors['accent_primary']}, {colors['accent_secondary']});
        border-radius: 4px;
        animation: fillProgress 1s ease-out;
    }}
    
    @keyframes fillProgress {{
        from {{
            width: 0;
        }}
    }}
    
    /* Probability Distribution */
    .probability-row {{
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }}
    
    .prob-label {{
        width: 100px;
        font-weight: 600;
        font-size: 0.9rem;
        color: {colors['text_secondary']};
    }}
    
    .prob-bar {{
        flex: 1;
        height: 24px;
        background: {colors['bg_tertiary']};
        border-radius: 6px;
        overflow: hidden;
        position: relative;
    }}
    
    .prob-bar-real {{
        background: linear-gradient(90deg, rgba(16, 185, 129, 0.2), rgba(16, 185, 129, 0.1));
    }}
    
    .prob-bar-fake {{
        background: linear-gradient(90deg, rgba(239, 68, 68, 0.2), rgba(239, 68, 68, 0.1));
    }}
    
    .prob-fill {{
        height: 100%;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 0.75rem;
        font-size: 0.8rem;
        font-weight: 700;
        color: white;
        animation: fillProgress 1s ease-out;
    }}
    
    .prob-fill-real {{
        background: linear-gradient(90deg, {colors['success']}, rgba(16, 185, 129, 0.6));
    }}
    
    .prob-fill-fake {{
        background: linear-gradient(90deg, {colors['danger']}, rgba(239, 68, 68, 0.6));
    }}
    
    .prob-value {{
        width: 60px;
        text-align: right;
        font-weight: 600;
        color: {colors['text_primary']};
        font-size: 0.9rem;
    }}
    
    /* Empty State */
    .empty-state {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
        text-align: center;
        color: {colors['text_secondary']};
    }}
    
    .empty-state-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }}
    
    .empty-state-text {{
        font-size: 1rem;
        line-height: 1.5;
    }}
    
    /* Messages */
    .error-message {{
        padding: 1rem;
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(239, 68, 68, 0.05));
        border: 1px solid {colors['danger']};
        border-radius: 8px;
        color: {colors['danger']};
        font-size: 0.9rem;
    }}
    
    /* Hover effects */
    [data-testid="stButton"] > button {{
        transition: all 0.3s ease;
    }}
    
    [data-testid="stButton"] > button:hover {{
        transform: translateY(-2px) !important;
    }}
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {{
        width: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {colors['bg_tertiary']};
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {colors['border']};
        border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {colors['accent_primary']};
    }}
    </style>
    """, unsafe_allow_html=True)

load_modern_css()

# ================== LOAD MODEL ==================
@st.cache_resource
def load_model():
    """Load model and vectorizer with caching"""
    BASE_DIR = Path(__file__).resolve().parent
    MODEL_PATH = BASE_DIR.parent / "models" / "model.jb"
    VECTORIZER_PATH = BASE_DIR.parent / "models" / "vectorizer.jb"
    
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer, None
    except FileNotFoundError as e:
        return None, None, str(e)

model, vectorizer, model_error = load_model()

# ================== TOP NAVIGATION BAR ==================
st.markdown(f"""
<div class="navbar">
    <div class="navbar-content">
        <div class="navbar-left">
            <a class="navbar-logo">
                <span style="font-size: 1.8rem;"></span>
                <span>Fake News Detector</span>
            </a>
        </div>
        <div class="navbar-right">
            <div class="avatar">AI</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ================== MAIN LAYOUT ==================
left_col, right_col = st.columns([1, 1], gap="large")

# ================== LEFT PANEL: INPUT ==================
with left_col:
    st.markdown(f"""
    <div class="panel">
        <div class="panel-title">📝 Enter News Content</div>
        <div class="input-wrapper">
    """, unsafe_allow_html=True)
    
    news_input = st.text_area(
        "article_input",
        value=st.session_state.article_input,
        placeholder="Paste or type news article here...",
        height=350,
        label_visibility="collapsed",
        key="article_input"
    )
    
    btn_col1, btn_col2 = st.columns([1, 1])
    
    with btn_col1:
        analyze_clicked = st.button(
            "▶ Analyze",
            key="analyze",
            use_container_width=True,
            help="Analyze the news article"
        )
    
    with btn_col2:
        clear_clicked = st.button(
            "✕ Clear",
            key="clear",
            use_container_width=True,
            help="Clear text",
            on_click=clear_article_input
        )
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================== RIGHT PANEL: RESULTS ==================
with right_col:
    st.markdown(f"""
    <div class="panel">
        <div class="panel-title">Analysis Result</div>
        <div class="result-section">
    """, unsafe_allow_html=True)
    
    if not analyze_clicked:
        st.markdown(f"""
        <div class="empty-state">
            <div class="empty-state-icon">📋</div>
            <div class="empty-state-text">
                <p><strong>Ready to analyze</strong></p>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Paste a news article and click Analyze to get started</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if not news_input.strip():
            st.markdown(f"""
            <div class="error-message">
                ⚠️ Please enter news content before analyzing
            </div>
            """, unsafe_allow_html=True)
        elif model_error:
            st.markdown(f"""
            <div class="error-message">
                ❌ Model not found. Please train the model first using: python src/train.py
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("🔄 Analyzing..."):
                try:
                    prepared_text = preprocess_text(news_input)
                    vectorized = vectorizer.transform([prepared_text])
                    prediction = model.predict(vectorized)[0]
                    probabilities = model.predict_proba(vectorized)[0]
                    
                    is_real = prediction == 1
                    real_prob = probabilities[1]
                    fake_prob = probabilities[0]
                    confidence = max(real_prob, fake_prob)
                    
                    badge_class = "badge-real" if is_real else "badge-fake"
                    badge_text = "✓ REAL" if is_real else "✗ FAKE"
                    
                    # Prediction badge
                    st.markdown(f"""
                    <div class="result-card">
                        <span class="result-label">Prediction</span>
                        <div class="prediction-badge {badge_class}">{badge_text}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Confidence score
                    st.markdown(f"""
                    <div class="result-card">
                        <span class="result-label">Confidence Score</span>
                        <div class="confidence-label">
                            <span>Certainty</span>
                            <span class="confidence-value">{confidence*100:.1f}%</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: {confidence*100}%"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Probability distribution
                    st.markdown(f"""
                    <div class="result-card">
                        <span class="result-label">Probability Distribution</span>
                        <div style="margin-top: 1rem;">
                            <div class="probability-row">
                                <span class="prob-label">🟢 Real</span>
                                <div class="prob-bar prob-bar-real">
                                    <div class="prob-fill prob-fill-real" style="width: {real_prob*100}%;">
                                        {real_prob*100:.0f}%
                                    </div>
                                </div>
                                <span class="prob-value">{real_prob*100:.1f}%</span>
                            </div>
                            <div class="probability-row">
                                <span class="prob-label">🔴 Fake</span>
                                <div class="prob-bar prob-bar-fake">
                                    <div class="prob-fill prob-fill-fake" style="width: {fake_prob*100}%;">
                                        {fake_prob*100:.0f}%
                                    </div>
                                </div>
                                <span class="prob-value">{fake_prob*100:.1f}%</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Additional metrics
                    st.markdown(f"""
                    <div class="result-card">
                        <span class="result-label">Analysis Metrics</span>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                            <div style="text-align: center;">
                                <div style="font-size: 2rem; font-weight: 700; color: {colors['accent_primary']};">{len(news_input.split())}</div>
                                <div style="font-size: 0.85rem; color: {colors['text_secondary']}; margin-top: 0.25rem;">Words</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 2rem; font-weight: 700; color: {colors['accent_secondary']};">98.86%</div>
                                <div style="font-size: 0.85rem; color: {colors['text_secondary']}; margin-top: 0.25rem;">Accuracy</div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ Analysis Error: {str(e)}
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================== FOOTER ==================
st.divider()
st.markdown(f"""
<div style='text-align: center; padding: 2rem; color: {colors['text_secondary']}; font-size: 0.9rem;'>
    <p>Fake News Detector • Powered by Machine Learning • Built with Streamlit</p>
    <p style='margin-top: 0.5rem; font-size: 0.85rem;'>
        ⚠️ Use as a decision support tool. Always verify with trusted fact-checking sources.
    </p>
</div>
""", unsafe_allow_html=True)
