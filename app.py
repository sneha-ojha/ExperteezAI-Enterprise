import streamlit as st
from validator import validate_domain
from config import DOMAINS
from agent import run_agent

st.set_page_config(
    page_title="Research Specialist",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Research Specialist")

st.write(
    "Choose a research domain and enter your research topic."
)

domain = st.selectbox(
    "Choose Research Domain",
    list(DOMAINS.keys())
)

query = st.text_area(
    "Research Topic",
    height=120,
    placeholder="Example: Recent developments in Retrieval-Augmented Generation"
)

if st.button("🚀 Start Research", use_container_width=True):

    if query.strip() == "":
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Checking domain..."):

        detected_domain = validate_domain(query)

    st.write("Selected Domain:", domain)
    st.write("Detected Domain:", detected_domain)

    if detected_domain != domain:

        st.error("⚠ Domain Mismatch")

        st.info(
            f"""
Selected Domain: **{domain}**

Detected Domain: **{detected_domain}**
"""
        )

        if st.button(f"Switch to {detected_domain}"):

            result = run_agent(
                detected_domain,
                query
            )

            st.subheader("Research Plan")
            st.markdown(result["plan"])

            st.subheader("Reflection")
            st.markdown(result["reflection"])

    else:
        

        result = run_agent(domain, query)

        st.subheader("📋 Research Plan")
        st.markdown(result["plan"])
        st.divider()

        st.subheader("🧩 Evidence Synthesis")
        st.markdown(result["evidence"])

        st.divider()

        st.subheader("📖 Final Research Report")
        st.markdown(result["reflection"])