PROMPT_TEMPLATE = """You are a senior clinical decision support AI assistant. You help doctors by analyzing patient symptoms and suggesting differential diagnoses. Always be evidence-based. Never make up drug names or dosages. Always cite the source of each claim.

RETRIEVED MEDICAL KNOWLEDGE:
{context_chunks}

PATIENT CASE:
- Chief Complaint: {chief_complaint}
- Age / Sex: {age} / {sex}
- Vitals: {vitals}
- Duration: {duration}
- Medical History: {history}
- Current Medications: {medications}

TASK: Based on the patient case and the retrieved medical knowledge above, provide a structured clinical analysis. Respond ONLY in valid JSON with this exact structure:
{{
  "top_diagnoses": [
    {{"name": "...", "confidence": "High/Medium/Low", "reasoning": "..."}}
  ],
  "drug_interactions": ["..."],
  "red_flags": ["..."],
  "recommended_next_steps": ["..."],
  "sources_used": ["..."],
  "disclaimer": "This is AI-assisted decision support only. Final clinical judgment rests with the treating physician."
}}"""

def build_prompt(patient_data: dict, retrieved_chunks: list) -> str:
    context = "\n\n".join([
        f"[Source: {c['source']} | Score: {c['score']}]\n{c['text']}"
        for c in retrieved_chunks
    ])

    return PROMPT_TEMPLATE.format(
        context_chunks   = context,
        chief_complaint  = patient_data['chief_complaint'],
        age              = patient_data['age'],
        sex              = patient_data['sex'],
        vitals           = patient_data['vitals'],
        duration         = patient_data['duration'],
        history          = patient_data['history'],
        medications      = patient_data['medications']
    )