"""
Reusable Streamlit UI components for MediAssist RAG.

Each public function renders one self-contained section of the page.
They rely on icons from `app.icons`, styles from `app.styles`, and
helpers from `app.utils`.
"""

import streamlit as st

from app.icons import (
    ICON_CHECK,
    ICON_DRUG,
    ICON_FLAG,
    ICON_HEART,
    ICON_PULSE,
    ICON_SHIELD,
    ICON_SOURCE,
    ICON_STETHOSCOPE,
    ICON_STEPS,
)


# ─── Header ─────────────────────────────────────────────────────────────────

def render_header() -> None:
    """Top banner with logo, title and metadata."""
    st.markdown(
        f"""
        <div class="app-header">
            <div class="header-icon">{ICON_HEART}</div>
            <div class="header-text">
                <div class="app-title">MediAssist RAG</div>
                <div class="app-meta">
                    Clinical Decision Support
                    <span class="meta-sep">|</span>
                    LLaMA 3.3-70B via Groq
                    <span class="meta-sep">|</span>
                    PubMedQA Knowledge Base
                    <span class="meta-sep">|</span>
                    <span class="app-badge">Educational Use Only</span>
                </div>
            </div>
            <div style="flex-shrink:0;opacity:0.5;">{ICON_PULSE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─── Patient intake hero + form ─────────────────────────────────────────────

def render_intake_banner() -> None:
    """Brief informational banner shown above the patient form."""
    st.markdown(
        f"""
        <div class="hero-banner">
            {ICON_STETHOSCOPE}
            <div class="hero-text">
                <strong>Patient Intake Form</strong> &mdash;
                Enter the patient details below.  Fields marked with * are
                required.  The AI will cross-reference symptoms against the
                PubMedQA knowledge base.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_patient_form() -> tuple:
    """
    Render the two-column patient form inside a Streamlit form context.

    Returns
    -------
    tuple
        (submitted: bool, patient_data: dict)
    """
    with st.form("patient_form"):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            complaint = st.text_area(
                "Chief Complaint *",
                placeholder="e.g. Chest pain for 2 days, radiating to left arm",
                height=90,
            )
            age = st.number_input("Age", min_value=1, max_value=120, value=45)
            sex = st.selectbox("Biological Sex", ["Male", "Female", "Other"])
            vitals = st.text_input(
                "Vitals", placeholder="BP: 145/90, HR: 98, SpO2: 97%"
            )
        with col2:
            duration = st.text_input(
                "Duration of Symptoms",
                placeholder="e.g. 2 days, acute onset",
            )
            history = st.text_area(
                "Medical History",
                placeholder="Hypertension, Diabetes Type 2",
                height=90,
            )
            meds = st.text_area(
                "Current Medications",
                placeholder="Metformin 500mg, Amlodipine 5mg",
                height=90,
            )

        submitted = st.form_submit_button(
            "Run Clinical Analysis", use_container_width=True
        )

    patient_data = {
        "chief_complaint": complaint,
        "age": age,
        "sex": sex,
        "vitals": vitals,
        "duration": duration,
        "history": history,
        "medications": meds,
    }
    return submitted, patient_data


# ─── Streaming output ───────────────────────────────────────────────────────

def render_stream_label() -> None:
    st.markdown(
        f'<div class="section-label">{ICON_STETHOSCOPE} '
        f"AI Clinical Analysis &mdash; Streaming</div>",
        unsafe_allow_html=True,
    )


def render_stream_token(placeholder, text: str) -> None:
    placeholder.markdown(
        f'<div class="stream-box">{text}</div>',
        unsafe_allow_html=True,
    )


# ─── Parsed results ─────────────────────────────────────────────────────────

def render_analysis_header(retrieval_score: float = 0.0) -> None:
    pct = max(0, min(100, int(retrieval_score * 100)))
    if retrieval_score >= 0.7:
        strength_label = "Strong"
        strength_cls = "rs-strong"
    elif retrieval_score >= 0.4:
        strength_label = "Moderate"
        strength_cls = "rs-moderate"
    else:
        strength_label = "Weak"
        strength_cls = "rs-weak"

    st.markdown(
        f"""
        <div class="analysis-header">
            {ICON_CHECK}
            <span class="analysis-title">Analysis Complete</span>
            <div class="rs-badge-wrapper">
                <span class="rs-label">Retrieval Strength</span>
                <div class="rs-track"><div class="rs-fill {strength_cls}" style="width:{pct}%"></div></div>
                <span class="rs-value">{retrieval_score:.2f}</span>
                <span class="rs-tag {strength_cls}">{strength_label}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_diagnoses(diagnoses: list) -> None:
    if not diagnoses:
        st.markdown(
            '<div class="empty-state">No differential diagnoses returned.</div>',
            unsafe_allow_html=True,
        )
        return
    for idx, d in enumerate(diagnoses, 1):
        name = d.get("name", "Unknown")
        conf = d.get("confidence", "Unknown")
        reasoning = d.get("reasoning", "")
        badge_cls = {
            "high": "badge-high",
            "medium": "badge-medium",
            "low": "badge-low",
        }.get(conf.lower(), "badge-low")

        st.markdown(
            f"""
            <div class="dx-card">
                <div class="dx-header">
                    <span class="dx-name">
                        <span class="dx-num">{idx}</span> {name}
                    </span>
                    <span class="{badge_cls}">{conf.upper()}</span>
                </div>
                <div class="dx-reasoning">{reasoning}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_drug_interactions(interactions: list) -> None:
    if not interactions:
        st.markdown(
            '<div class="empty-state">No drug interactions identified.</div>',
            unsafe_allow_html=True,
        )
        return
    for item in interactions:
        # Support both old format (plain strings) and new format (dicts)
        if isinstance(item, dict):
            drugs = item.get("drugs", "Unknown")
            severity = item.get("severity", "Unknown")
            detail = item.get("detail", "")
            sev_lower = severity.lower()
            if sev_lower == "high":
                sev_cls = "badge-high-drug"
            elif sev_lower == "moderate":
                sev_cls = "badge-mod-drug"
            else:
                sev_cls = "badge-low-drug"
            st.markdown(
                f"""
                <div class="drug-card">
                    <div class="drug-header">
                        <span class="drug-name">{ICON_DRUG} {drugs}</span>
                        <span class="{sev_cls}">{severity.upper()}</span>
                    </div>
                    <div class="drug-detail">{detail}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="warn-item"><span class="info-icon">{ICON_DRUG}</span>'
                f"<span>{item}</span></div>",
                unsafe_allow_html=True,
            )


def render_red_flags(red_flags: list) -> None:
    if not red_flags:
        st.markdown(
            '<div class="empty-state">No red flags identified.</div>',
            unsafe_allow_html=True,
        )
        return
    for flag in red_flags:
        st.markdown(
            f'<div class="red-flag-item"><span class="info-icon">{ICON_FLAG}</span>'
            f"<span>{flag}</span></div>",
            unsafe_allow_html=True,
        )


def render_next_steps(steps: list) -> None:
    if not steps:
        st.markdown(
            '<div class="empty-state">No recommended next steps returned.</div>',
            unsafe_allow_html=True,
        )
        return
    for step in steps:
        st.markdown(
            f'<div class="info-item"><span class="info-icon">{ICON_STEPS}</span>'
            f"<span>{step}</span></div>",
            unsafe_allow_html=True,
        )


def render_sources(sources: list) -> None:
    if not sources:
        return
    chips = "".join(
        f'<span class="source-chip">{ICON_SOURCE} {s}</span>' for s in sources
    )
    st.markdown(
        f'<div style="margin-top:1.5rem">'
        f'<div class="section-label">{ICON_SOURCE} Sources Referenced</div>'
        f'<div class="sources-row">{chips}</div></div>',
        unsafe_allow_html=True,
    )


def render_disclaimer(text: str | None = None) -> None:
    text = text or (
        "This is AI-assisted decision support only. "
        "Final clinical judgment rests with the treating physician."
    )
    st.markdown(
        f'<div class="disclaimer">{ICON_SHIELD} {text}</div>',
        unsafe_allow_html=True,
    )


def render_evidence(chunks: list) -> None:
    """Render retrieved evidence chunks so the user can inspect what the
    AI based its answer on."""
    if not chunks:
        st.markdown(
            '<div class="empty-state">No evidence chunks were retrieved.</div>',
            unsafe_allow_html=True,
        )
        return
    for idx, chunk in enumerate(chunks, 1):
        score = chunk.get("score", 0)
        source = chunk.get("source", "Unknown")
        text = chunk.get("text", "")
        # Colour the score bar: green >=0.7, amber >=0.4, red <0.4
        if score >= 0.7:
            bar_cls = "score-bar-high"
        elif score >= 0.4:
            bar_cls = "score-bar-med"
        else:
            bar_cls = "score-bar-low"
        pct = max(0, min(100, int(score * 100)))
        st.markdown(
            f"""
            <div class="evidence-card">
                <div class="evidence-header">
                    <span class="evidence-idx">{idx}</span>
                    <span class="evidence-source">{ICON_SOURCE} {source}</span>
                    <span class="evidence-score">Similarity: {score:.3f}</span>
                </div>
                <div class="score-track"><div class="score-fill {bar_cls}" style="width:{pct}%"></div></div>
                <div class="evidence-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_latency(timings: dict) -> None:
    """Render a compact latency bar showing time spent in each pipeline stage."""
    if not timings:
        return
    total = sum(timings.values())
    pills = []
    for stage, secs in timings.items():
        if secs < 0.01:
            label = f"{stage}: <10ms"
        elif secs < 1:
            label = f"{stage}: {secs*1000:.0f}ms"
        else:
            label = f"{stage}: {secs:.2f}s"
        pills.append(f'<span class="lat-pill">{label}</span>')

    if total < 1:
        total_label = f"{total*1000:.0f}ms"
    else:
        total_label = f"{total:.2f}s"

    st.markdown(
        f"""
        <div class="lat-bar">
            <span class="lat-title">Pipeline Latency</span>
            {''.join(pills)}
            <span class="lat-total">Total: {total_label}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_results(result: dict, chunks: list | None = None, retrieval_score: float = 0.0, timings: dict | None = None) -> None:
    """
    Master renderer: given a parsed LLM JSON dict, render every
    results section (tabs, sources, disclaimer).
    """
    render_analysis_header(retrieval_score)
    render_latency(timings or {})

    tab_dx, tab_drug, tab_flags, tab_steps, tab_evidence = st.tabs(
        [
            "  Differential Diagnoses  ",
            "  Drug Interactions  ",
            "  Red Flags  ",
            "  Recommended Next Steps  ",
            "  Retrieved Evidence  ",
        ]
    )

    with tab_dx:
        render_diagnoses(result.get("top_diagnoses", []))
    with tab_drug:
        render_drug_interactions(result.get("drug_interactions", []))
    with tab_flags:
        render_red_flags(result.get("red_flags", []))
    with tab_steps:
        render_next_steps(result.get("recommended_next_steps", []))
    with tab_evidence:
        render_evidence(chunks or [])

    render_sources(result.get("sources_used", []))
    render_disclaimer(result.get("disclaimer"))
