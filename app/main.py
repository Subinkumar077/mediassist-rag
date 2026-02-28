"""
MediAssist RAG — main Streamlit entry-point.

All presentation logic lives in the `app` package:
    styles.py      – CSS injection
    icons.py       – inline SVG constants
    components.py  – render_* UI building blocks
    utils.py       – emoji stripping / sanitisation
"""

import json
import sys
import os
import time

import streamlit as st

# Make the project root importable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.styles import inject_css
from app.components import (
    render_header,
    render_intake_banner,
    render_patient_form,
    render_results,
    render_stream_label,
    render_stream_token,
)
from app.utils import extract_json, sanitize_result, compute_retrieval_score
from pipeline.retriever import retrieve
from pipeline.prompt_builder import build_prompt
from inference.llm_client import call_llm

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MediAssist RAG -- Clinical Decision Support",
    page_icon="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' "
              "viewBox='0 0 24 24'><path d='M12 21.35l-1.45-1.32C5.4 "
              "15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 "
              "4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 "
              "8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z' "
              "fill='%230e7490'/></svg>",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Inject styles + render static sections ─────────────────────────────────
inject_css()
render_header()
render_intake_banner()

# ─── Patient form ────────────────────────────────────────────────────────────
submitted, patient_data = render_patient_form()

if submitted and not patient_data["chief_complaint"]:
    st.warning("Chief Complaint is required to proceed.")

# ─── Analysis pipeline ──────────────────────────────────────────────────────
if submitted and patient_data["chief_complaint"]:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    timings = {}  # latency per stage

    t0 = time.perf_counter()
    with st.spinner("Retrieving relevant medical literature..."):
        chunks = retrieve(patient_data["chief_complaint"])
    timings["Retrieval"] = time.perf_counter() - t0

    # Compute aggregate retrieval confidence from chunk similarity scores
    retrieval_score = compute_retrieval_score(chunks)

    t0 = time.perf_counter()
    prompt = build_prompt(patient_data, chunks)
    timings["Prompt Build"] = time.perf_counter() - t0

    # Streaming response
    render_stream_label()
    stream_placeholder = st.empty()
    full_response = ""

    t0 = time.perf_counter()
    for token in call_llm(prompt, stream=True):
        full_response += token
        render_stream_token(stream_placeholder, full_response)
    timings["LLM Inference"] = time.perf_counter() - t0

    stream_placeholder.empty()

    # Parse + display
    try:
        t0 = time.perf_counter()
        clean_json = extract_json(full_response)
        result = sanitize_result(json.loads(clean_json))
        timings["Parsing"] = time.perf_counter() - t0
        render_results(result, chunks, retrieval_score, timings)
    except json.JSONDecodeError:
        st.warning("The model response was not valid JSON. Raw output below.")
        st.markdown(
            f'<div class="stream-box">{full_response}</div>',
            unsafe_allow_html=True,
        )
    except KeyError as e:
        st.error(f"Missing expected field in LLM response: {e}")
    except Exception as e:
        st.error(f"Unexpected error while parsing response: {e}")
