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


if st.button(
    "🚀 Generate Research Paper",
    use_container_width=True
):

    if not query.strip():

        st.warning("Please enter a research topic.")
        st.stop()


    # -----------------------------------------
    # STEP 1 : Domain Validation
    # -----------------------------------------

    with st.spinner("Identifying research domain..."):

        detected_domain = validate_domain(query)


    col1, col2 = st.columns(2)


    with col1:

        st.info(
            f"Selected Domain\n\n**{domain}**"
        )


    with col2:

        st.info(
            f"Detected Domain\n\n**{detected_domain}**"
        )


    if detected_domain != domain:

        st.error(
            "The selected domain does not match the detected topic."
        )

        if st.button(
            f"Switch to {detected_domain}"
        ):

            domain = detected_domain

        else:

            st.stop()


    # -----------------------------------------
    # RESEARCH STATUS
    # -----------------------------------------

    st.divider()

    st.subheader("🔬 Research Progress")


    plan_status = st.empty()
    search_status = st.empty()
    evidence_status = st.empty()


    plan_status.info(
        "📋 Creating research plan..."
    )

    search_status.info(
        "🔎 Waiting to search sources..."
    )

    evidence_status.info(
        "🧩 Waiting to organize evidence..."
    )


    # -----------------------------------------
    # REPORT AREA
    # -----------------------------------------

    st.divider()

    st.header("📖 ExperteezAI Research Paper")


    # Store placeholders for sections
    section_placeholders = {}

    # Keep track of completed sections
    completed_sections = set()


    # -----------------------------------------
    # RUN RESEARCH STREAM
    # -----------------------------------------

    for event in run_agent(domain, query):


        # -------------------------------------
        # RESEARCH PLAN
        # -------------------------------------

        if event["type"] == "plan":

            plan_status.success(
                "📋 Research plan ✓"
            )

            with st.expander(
                "📋 Research Plan",
                expanded=False
            ):

                st.markdown(
                    event["data"]
                )


        # -------------------------------------
        # SEARCH COMPLETE
        # -------------------------------------

        elif event["type"] == "search_complete":

            search_status.success(
                "🔎 Sources searched ✓"
            )


        # -------------------------------------
        # EVIDENCE
        # -------------------------------------

        elif event["type"] == "evidence":

            evidence_status.success(
                "🧩 Evidence organized ✓"
            )

            with st.expander(
                "🧩 Evidence Synthesis",
                expanded=False
            ):

                st.markdown(
                    event["data"]
                )


        # -------------------------------------
        # REPORT SECTION
        # -------------------------------------

        elif event["type"] == "section":

            section = event["section"]
            content = event["data"]

            completed_sections.add(section)


            # Create a placeholder if this is
            # the first time we see this section

            if section not in section_placeholders:

                section_placeholders[section] = st.empty()


            placeholder = section_placeholders[section]


            placeholder.markdown(
                content
            )


        # -------------------------------------
        # COMPLETE
        # -------------------------------------

        elif event["type"] == "complete":

            st.divider()

            st.success(
                "✅ Research completed successfully."
            )