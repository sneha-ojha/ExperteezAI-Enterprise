import streamlit as st
from validator import validate_domain
from config import DOMAINS
from agent import run_agent
st.set_page_config(
    page_title="ExperteezAI Research",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 ExperteezAI Research")

st.markdown(
"""
Generate comprehensive, evidence-based research papers using specialized
domain research agents and trusted knowledge sources.
"""
)

domain = st.selectbox(
    "Research Domain",
    list(DOMAINS.keys())
)

query = st.text_area(
    "Research Topic",
    height=140,
    placeholder="Example: Recent developments in Retrieval-Augmented Generation"
)

if st.button("🚀 Generate Research Paper", use_container_width=True):

    if not query.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Identifying research domain..."):
        detected_domain = validate_domain(query)

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"Selected Domain\n\n**{domain}**")

    with col2:
        st.info(f"Detected Domain\n\n**{detected_domain}**")

    if detected_domain != domain:

        st.error("The selected domain does not match the detected topic.")

        if st.button(f"Switch to {detected_domain}"):

            domain = detected_domain

        else:
            st.stop()

    with st.spinner("ExperteezAI specialists are conducting research..."):

        result = run_agent(domain, query)

    st.divider()

    with st.expander("📋 Research Plan", expanded=False):
        st.markdown(result["plan"])

    with st.expander("🧩 Evidence Synthesis", expanded=False):
        st.markdown(result["evidence"])

    st.divider()

    st.header("📖 ExperteezAI Research Paper")

    reports = result["reflection"]

    if isinstance(reports, list):

        progress = st.progress(0)

        total = len(reports)

        for i, section in enumerate(reports):

            progress.progress((i + 1) / total)

            st.markdown(section)

            if i != total - 1:
                st.divider()

        progress.empty()

    else:

        st.markdown(reports)

    st.divider()

    st.success("Research completed successfully.")