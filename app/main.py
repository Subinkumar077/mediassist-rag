import streamlit as st
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline.retriever import retrieve
from pipeline.prompt_builder import build_prompt
from inference.llm_client import call_llm

st.set_page_config(page_title="MediAssist RAG", layout="wide", page_icon="🏥")
st.title("🏥 MediAssist RAG — Clinical Decision Support")
st.caption("Powered by LLaMA 3.1 on AMD MI300X via ROCm | For educational/demo use only")

with st.form("patient_form"):
    col1, col2 = st.columns(2)
    with col1:
        complaint = st.text_area("Chief Complaint *", placeholder="e.g. Chest pain for 2 days, radiating to left arm")
        age       = st.number_input("Age", 1, 120, 45)
        sex       = st.selectbox("Sex", ["Male", "Female", "Other"])
        vitals    = st.text_input("Vitals", placeholder="BP: 145/90, HR: 98, SpO2: 97%")
    with col2:
        duration  = st.text_input("Duration of Symptoms", placeholder="e.g. 2 days, acute onset")
        history   = st.text_area("Medical History", placeholder="Hypertension, Diabetes Type 2")
        meds      = st.text_area("Current Medications", placeholder="Metformin 500mg, Amlodipine 5mg")
    submitted = st.form_submit_button("🔍 Analyze Patient", use_container_width=True)

if submitted and complaint:
    with st.spinner("🔍 Retrieving medical knowledge..."):
        chunks = retrieve(complaint)

    patient_data = {
        'chief_complaint': complaint,
        'age': age,
        'sex': sex,
        'vitals': vitals,
        'duration': duration,
        'history': history,
        'medications': meds
    }

    prompt = build_prompt(patient_data, chunks)

    st.subheader("🧠 AI Clinical Analysis (AMD MI300X)")
    output_box = st.empty()
    full_response = ""

    for token in call_llm(prompt, stream=True):
        full_response += token
        output_box.code(full_response, language="json")

    try:
        result = json.loads(full_response)
        st.success("✅ Analysis Complete")
        t1, t2, t3 = st.tabs(["Diagnoses", "Drug Interactions", "Next Steps"])
        with t1:
            for d in result.get('top_diagnoses', []):
                st.metric(d['name'], d['confidence'])
                st.caption(d['reasoning'])
        with t2:
            for item in result.get('drug_interactions', []):
                st.warning(item)
        with t3:
            for step in result.get('recommended_next_steps', []):
                st.info(step)
    except json.JSONDecodeError:
        st.warning("⚠️ Response not in JSON format — showing raw output above.")
    except KeyError as e:
        st.error(f"❌ Missing expected field in LLM response: {e}")
    except Exception as e:
        st.error(f"❌ Unexpected error while parsing response: {e}")
