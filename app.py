
import streamlit as st

from validator import validate_domain
from config import DOMAINS
from agent import run_agent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ExperteezAI Enterprise",
    page_icon="✦",
    layout="wide"
)


# ============================================================
# ENTERPRISE UI STYLES
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


/* ============================================================
   GLOBAL
   ============================================================ */

:root {
    --bg: #f8fafc;
    --surface: #ffffff;
    --surface-soft: #f1f5f9;

    --border: #cbd5e1;
    --border-strong: #94a3b8;

    --text-main: #0f172a;
    --text-muted: #475569;
    --text-light: #64748b;

    --accent-dark: #064e3b;
    --accent-hover: #022c22;
    --accent-emerald: #059669;

    --accent-soft: #ecfdf5;
    --accent-border: #a7f3d0;
}


html,
body,
.stApp {
    font-family: 'Inter', sans-serif !important;
}


.stApp {
    background: var(--bg) !important;
    color: var(--text-main) !important;
}


.block-container {
    max-width: 1120px !important;
    padding-top: 1.5rem !important;
    padding-bottom: 5rem !important;
}


header[data-testid="stHeader"] {
    background: transparent !important;
}


#MainMenu,
footer,
[data-testid="stToolbar"] {
    visibility: hidden !important;
}


/* ============================================================
   HEADER
   ============================================================ */

.enterprise-header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 0 0 18px 0;
    margin-bottom: 30px;

    border-bottom: 1px solid var(--border);
}


.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}


.brand-mark {
    width: 42px;
    height: 42px;

    border-radius: 10px;

    background: var(--accent-dark);

    display: flex;
    align-items: center;
    justify-content: center;

    color: white;
    font-size: 24px;
    font-weight: 700;


}


.brand-name {
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--text-main);
}


.brand-subtitle {
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 2px;
}


.header-badge {
    padding: 6px 14px;

    border: 1px solid var(--border-strong);
    border-radius: 999px;

    background: var(--surface);

    color: var(--text-main);

    font-size: 12px;
    font-weight: 600;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    max-width: 820px;

    margin: 30px auto 36px auto;

    text-align: center;

    animation: heroEnter .55s cubic-bezier(.2,.8,.2,1);
}


.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;

    padding: 7px 16px;

    border: 1px solid var(--accent-border);
    border-radius: 999px;

    background: var(--accent-soft);

    color: var(--accent-dark);

    font-size: 12px;
    font-weight: 700;

    letter-spacing: .05em;
    text-transform: uppercase;

    margin-bottom: 20px;
}


.hero-icon {
    font-size: 16px;
    line-height: 1;
}


.hero-title {
    font-size: 42px;
    line-height: 1.15;

    font-weight: 800;

    letter-spacing: -0.035em;

    color: var(--text-main);
}


.hero-description {
    max-width: 680px;

    margin: 18px auto 0 auto;

    color: var(--text-muted);

    font-size: 16px;
    line-height: 1.65;
}


/* ============================================================
   WALKTHROUGH
   ============================================================ */

.walkthrough-screen,
.step-shell {
    animation: screenEnter .42s cubic-bezier(.2,.8,.2,1);
}


.step-title {
    display: flex;
    align-items: center;
    gap: 14px;

    margin: 0 0 14px 0;

    color: var(--text-main);

    font-size: 26px;
    font-weight: 700;

    letter-spacing: -0.03em;
}


.step-icon {
    width: 44px;
    height: 44px;

    flex: 0 0 44px;

    border-radius: 10px;

    background: var(--accent-dark);

    display: flex;
    align-items: center;
    justify-content: center;

    color: white;

    font-size: 21px;
    font-weight: 700;
}


.step-description {
    max-width: 760px;

    margin-bottom: 24px;

    color: var(--text-muted);

    font-size: 15px;
    line-height: 1.7;
}


/* ============================================================
   FEATURE CARDS
   ============================================================ */

.feature-grid {
    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 18px;

    margin-top: 20px;
}


.feature-card {
    min-height: 180px;

    padding: 24px;

    background: var(--surface);

    border: 1px solid var(--border);

    border-radius: 12px;



    transition:
        transform .2s ease,
        border-color .2s ease,
        box-shadow .2s ease;
}


.feature-card:hover {
    transform: translateY(-2px);

    border-color: var(--accent-emerald);

    box-shadow: 0 10px 20px rgba(15,23,42,.06);
}


.feature-icon {
    width: 40px;
    height: 40px;

    border-radius: 8px;

    background: var(--accent-soft);

    border: 1px solid var(--accent-border);

    display: flex;
    align-items: center;
    justify-content: center;

    margin-bottom: 16px;

    color: var(--accent-dark);

    font-size: 20px;
    font-weight: 700;
}


.feature-title {
    margin-bottom: 8px;

    color: var(--text-main);

    font-size: 16px;
    font-weight: 700;
}


.feature-description {
    color: var(--text-muted);

    font-size: 13.5px;

    line-height: 1.6;
}


/* ============================================================
   CALLOUT
   ============================================================ */

.custom-callout {
    background-color: var(--surface);

    border-left: 4px solid var(--accent-emerald);

    border-top: 1px solid var(--border);
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);

    padding: 16px 20px;

    border-radius: 0 8px 8px 0;

    margin: 20px 0;

    color: var(--text-main);

    font-size: 14px;
    font-weight: 500;
}


/* ============================================================
   PROGRESS TRACKER
   ============================================================ */

.progress-wrapper {
    max-width: 820px;

    margin: 0 auto 36px auto;
}


.progress-label {
    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 8px;

    color: var(--text-main);

    font-size: 13px;

    font-weight: 600;
}


.progress-track {
    height: 8px;

    background: var(--border);

    border-radius: 999px;

    overflow: hidden;
}


.progress-fill {
    height: 100%;

    background: var(--accent-dark);

    border-radius: 999px;

    transition: width .45s cubic-bezier(.2,.8,.2,1);
}


/* ============================================================
   CREATION PAGE
   ============================================================ */

.creation-header {
    margin-bottom: 28px;
}


.creation-title-row {
    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 8px;
}


.creation-title-icon {
    width: 42px;
    height: 42px;

    border-radius: 9px;

    background: var(--accent-dark);

    display: flex;
    align-items: center;
    justify-content: center;

    color: white;

    font-size: 21px;
    font-weight: 700;
}


.creation-title {
    font-size: 28px;

    font-weight: 800;

    letter-spacing: -0.03em;

    color: var(--text-main);

    margin: 0;
}


.creation-description {
    color: var(--text-muted);

    font-size: 15px;

    line-height: 1.65;

    margin: 0;
}


.form-section-title {
    color: var(--text-main) !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    margin-bottom: 8px !important;
}


/* ============================================================
   STREAMLIT CONTAINERS
   ============================================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--surface) !important;

    border: 1px solid var(--border) !important;

    border-radius: 12px !important;



    margin-bottom: 20px !important;
}


/* ============================================================
   ALL NORMAL TEXT
   ============================================================ */

.stMarkdown,
.stMarkdown p,
.stMarkdown span,
.stMarkdown strong,
.stCaption,
[data-testid="stCaptionContainer"] {
    color: var(--text-main);
}


/* ============================================================
   WIDGET LABELS
   ============================================================ */

div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] span,
div[data-testid="stWidgetLabel"] label {
    color: var(--text-main) !important;

    font-weight: 600 !important;

    font-size: 14px !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

div[data-baseweb="input"],
div[data-baseweb="select"],
div[data-baseweb="textarea"] {
    background-color: #ffffff !important;

    border-radius: 8px !important;
}


div[data-baseweb="input"] {
    border: 1.5px solid var(--border-strong) !important;
}


div[data-baseweb="select"] {
    border: 1.5px solid var(--border-strong) !important;
}


div[data-baseweb="textarea"] {
    border: 1.5px solid var(--border-strong) !important;
}


div[data-baseweb="input"]:focus-within,
div[data-baseweb="select"]:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: var(--accent-dark) !important;


}


/* INPUT TEXT */

input,
textarea {
    color: var(--text-main) !important;

    background-color: #ffffff !important;

    font-size: 14px !important;
}


/* SELECT TEXT */

div[data-baseweb="select"] * {
    color: var(--text-main) !important;
}


/* PLACEHOLDERS */

input::placeholder,
textarea::placeholder {
    color: #64748b !important;

    opacity: 1 !important;
}


/* ============================================================
   RADIO BUTTONS
   ============================================================ */

div[role="radiogroup"] label {
    color: var(--text-main) !important;
}


div[role="radiogroup"] label p,
div[role="radiogroup"] label span {
    color: var(--text-main) !important;

    font-weight: 500 !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */

div.stButton > button {
    border-radius: 8px !important;

    font-weight: 600 !important;

    transition:
        transform .2s ease,
        box-shadow .2s ease,
        background-color .2s ease;
}


/* PRIMARY */

div.stButton > button[kind="primary"] {
    background-color: var(--accent-dark) !important;

    border: 1px solid var(--accent-dark) !important;

    color: #ffffff !important;

    font-weight: 700 !important;

    font-size: 15px !important;

    padding: 12px 28px !important;

    border-radius: 8px !important;


}


div.stButton > button[kind="primary"]:hover {
    background-color: var(--accent-hover) !important;

    border-color: var(--accent-hover) !important;

    color: #ffffff !important;



    transform: translateY(-1px);
}


div.stButton > button[kind="primary"] p,
div.stButton > button[kind="primary"] span {
    color: #ffffff !important;
}


/* SECONDARY */

div.stButton > button[kind="secondary"] {
    background-color: #ffffff !important;

    border: 1.5px solid var(--border-strong) !important;

    color: var(--text-main) !important;

    font-weight: 600 !important;

    font-size: 15px !important;

    padding: 12px 28px !important;

    border-radius: 8px !important;
}


div.stButton > button[kind="secondary"]:hover {
    border-color: var(--text-main) !important;

    background-color: var(--surface-soft) !important;
}


div.stButton > button[kind="secondary"] p,
div.stButton > button[kind="secondary"] span {
    color: var(--text-main) !important;
}


/* ============================================================
   ALERTS
   ============================================================ */

div[data-testid="stAlert"] {
    border-radius: 8px !important;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

hr {
    border-color: var(--border) !important;
}


/* ============================================================
   ANIMATIONS
   ============================================================ */

@keyframes heroEnter {

    from {
        opacity: 0;

        transform: translateY(12px);
    }

    to {
        opacity: 1;

        transform: translateY(0);
    }
}


@keyframes screenEnter {

    from {
        opacity: 0;

        transform: translateX(12px);
    }

    to {
        opacity: 1;

        transform: translateX(0);
    }
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 800px) {

    .feature-grid {
        grid-template-columns: 1fr;
    }

    .hero-title {
        font-size: 34px;
    }

    .header-badge {
        display: none;
    }

}

</style>
""")


# ============================================================
# HEADER
# ============================================================

st.html("""
<div class="enterprise-header">

    <div class="brand">

        <div class="brand-mark">
            ✦
        </div>

        <div>

            <div class="brand-name">
                ExperteezAI Enterprise
            </div>

            <div class="brand-subtitle">
                Enterprise Intelligence Platform <br> by Sneha Ojha - 2301010256
            </div>

        </div>

    </div>

    <div class="header-badge">
        Internal Use · Knowledge Owners
    </div>

</div>
""")


# ============================================================
# HERO
# ============================================================

st.html("""
<div class="hero">

    <div class="hero-eyebrow">

        <span class="hero-icon">✦</span>

        AI-powered enterprise intelligence

    </div>

    <div class="hero-title">

        From scattered knowledge<br>
        to decision-ready intelligence.

    </div>

    <div class="hero-description">

        Research, analyze and transform complex information into
        structured briefs, training material, SOPs and knowledge assets.

    </div>

</div>
""")


# ============================================================
# WALKTHROUGH STATE
# ============================================================

if "walkthrough_step" not in st.session_state:
    st.session_state.walkthrough_step = 0


step = st.session_state.walkthrough_step

total_steps = 4


# ============================================================
# WALKTHROUGH PROGRESS
# ============================================================

if step < 4:

    progress_percent = (step / (total_steps - 1)) * 100

    st.html(f"""
    <div class="progress-wrapper walkthrough-screen">

        <div class="progress-label">

            <span>
                ExperteezAI walkthrough
            </span>

            <span>
                Step {step + 1} of {total_steps}
            </span>

        </div>

        <div class="progress-track">

            <div
                class="progress-fill"
                style="width: {progress_percent}%;">
            </div>

        </div>

    </div>
    """)


# ============================================================
# STEP 1 — WELCOME
# ============================================================

if step == 0:

    st.html("""
    <div class="step-shell">

        <div class="step-title">



            Turn company knowledge into useful intelligence.

        </div>

        <div class="step-description">

            ExperteezAI helps internal teams turn scattered information,
            public documentation, project context, and external evidence
            into structured business knowledge.

            Instead of starting with a blank document, describe what you
            need and let the system organize the information into a useful
            professional artifact.

        </div>

        <div
            class="step-description"
            style="font-weight:700; color:#0f172a;">

            What can you create?

        </div>

        <div class="feature-grid">

            <div class="feature-card">

                <div class="feature-icon">
                    ◈
                </div>

                <div class="feature-title">
                    Leadership Brief
                </div>

                <div class="feature-description">

                    Turn a business question into a concise,
                    evidence-backed intelligence brief for leadership
                    and decision discussions.

                </div>

            </div>


            <div class="feature-card">

                <div class="feature-icon">
                    ◉
                </div>

                <div class="feature-title">
                    Training & Onboarding
                </div>

                <div class="feature-description">

                    Turn technical or organizational knowledge into
                    structured material that helps new employees learn
                    faster.

                </div>

            </div>


            <div class="feature-card">

                <div class="feature-icon">
                    ≡
                </div>

                <div class="feature-title">
                    SOP / Process
                </div>

                <div class="feature-description">

                    Convert process knowledge into structured,
                    actionable operating procedures and repeatable
                    workflows.

                </div>

            </div>

        </div>

    </div>
    """)

    st.write("")

    if st.button(
        "Continue",
        type="primary",
        use_container_width=True
    ):

        st.session_state.walkthrough_step = 1

        st.rerun()


# ============================================================
# STEP 2 — LEADERSHIP BRIEF
# ============================================================

elif step == 1:

    st.html("""
    <div class="step-shell">

        <div class="step-title">

            <div class="step-icon">
                ◈
            </div>

            Leadership Brief

        </div>

        <div class="step-description">

            Give ExperteezAI a business question and it can organize
            relevant information into a decision-oriented brief.

        </div>

    </div>
    """)

    st.markdown(
        "**Example**\n\n"
        "> Should our engineering team adopt a new backend technology "
        "for the next generation of our platform?"
    )

    st.markdown(
        "**The output can include**\n\n"
        "- Executive summary\n"
        "- Business context\n"
        "- Key findings\n"
        "- Options and trade-offs\n"
        "- Risks and considerations\n"
        "- Next steps"
    )

    st.html("""
    <div class="custom-callout">

        <strong>Best for:</strong>
        leadership discussions, business decisions,
        strategy preparation, and management briefs.

    </div>
    """)

    st.write("")

    back, next_button = st.columns(2)

    with back:

        if st.button(
            "Back",
            type="secondary",
            use_container_width=True
        ):

            st.session_state.walkthrough_step = 0

            st.rerun()

    with next_button:

        if st.button(
            "Next",
            type="primary",
            use_container_width=True
        ):

            st.session_state.walkthrough_step = 2

            st.rerun()


# ============================================================
# STEP 3 — TRAINING
# ============================================================

elif step == 2:

    st.html("""
    <div class="step-shell">

        <div class="step-title">

            <div class="step-icon">
                ◉
            </div>

            Training & Onboarding

        </div>

        <div class="step-description">

            Turn existing technical or organizational knowledge into
            structured learning material for new employees.

        </div>

    </div>
    """)

    st.markdown(
        "**Example**\n\n"
        "> Create an onboarding guide for a new developer joining our "
        "Node.js backend team."
    )

    st.markdown(
        "**The output can include**\n\n"
        "- Topic overview\n"
        "- Key concepts\n"
        "- How the system works\n"
        "- Practical examples\n"
        "- Common mistakes\n"
        "- Quick reference"
    )

    st.html("""
    <div class="custom-callout">

        <strong>Best for:</strong>
        employee onboarding, knowledge transfer,
        technical training, and learning material.

    </div>
    """)

    st.write("")

    back, next_button = st.columns(2)

    with back:

        if st.button(
            "Back",
            type="secondary",
            use_container_width=True
        ):

            st.session_state.walkthrough_step = 1

            st.rerun()

    with next_button:

        if st.button(
            "Next",
            type="primary",
            use_container_width=True
        ):

            st.session_state.walkthrough_step = 3

            st.rerun()


# ============================================================
# STEP 4 — SOP
# ============================================================

elif step == 3:

    st.html("""
    <div class="step-shell">

        <div class="step-title">

            <div class="step-icon">
                ≡
            </div>

            SOP / Process Builder

        </div>

        <div class="step-description">

            Turn process knowledge into a structured and actionable
            standard operating procedure.

        </div>

    </div>
    """)

    st.markdown(
        "**Example**\n\n"
        "> Create an SOP for our new employee onboarding process."
    )

    st.markdown(
        "**The output can include**\n\n"
        "- Purpose and scope\n"
        "- Required inputs\n"
        "- Step-by-step procedure\n"
        "- Roles and responsibilities\n"
        "- Important checks\n"
        "- Exceptions and risks\n"
        "- Final checklist"
    )

    st.html("""
    <div class="custom-callout">

        <strong>Best for:</strong>
        process documentation, standardization,
        knowledge transfer, and operational workflows.

    </div>
    """)

    st.write("")

    back, start = st.columns(2)

    with back:

        if st.button(
            "Back",
            type="secondary",
            use_container_width=True
        ):

            st.session_state.walkthrough_step = 2

            st.rerun()

    with start:

        if st.button(
            "Start Creating",
            type="primary",
            use_container_width=True
        ):

            st.session_state.walkthrough_step = 4

            st.rerun()


# ============================================================
# CREATION PAGE
# ============================================================

if st.session_state.walkthrough_step == 4:

    # --------------------------------------------------------
    # CREATION HEADER
    # --------------------------------------------------------

    st.html("""
    <div class="creation-header">

        <div class="creation-title-row">

            <div class="creation-title-icon">
                ▣
            </div>

            <h2 class="creation-title">
                Create Internal Intelligence Report
            </h2>

        </div>

        <p class="creation-description">

            Specify your intelligence requirement below.
            You can also paste optional public links such as GitHub,
            Google Drive or documentation URLs to include contextual
            evidence.

        </p>

    </div>
    """)


    # ========================================================
    # SECTION 1 — OUTPUT TYPE & DOMAIN
    # ========================================================

    with st.container(border=True):

        st.markdown(
            '<div class="form-section-title">'
            '1. Output Type & Knowledge Domain'
            '</div>',
            unsafe_allow_html=True
        )

        col_type, col_domain = st.columns(2)


        # ----------------------------------------------------
        # OUTPUT TYPE
        # ----------------------------------------------------

        with col_type:

            st.markdown(
                "**Output Type**"
            )

            output_type = st.selectbox(
                "Output Type",
                [
                    "Leadership Brief",
                    "Training & Onboarding",
                    "SOP / Process",
                    "Decision Analysis",
                    "Knowledge Guide",
                    "Other"
                ],
                label_visibility="collapsed"
            )


            custom_output_type = ""


            if output_type == "Other":

                custom_output_type = st.text_input(
                    "Describe output type",
                    placeholder=(
                        "E.g., Technical evaluation, "
                        "project handover document..."
                    )
                )


        # ----------------------------------------------------
        # DOMAIN
        # ----------------------------------------------------

        with col_domain:

            st.markdown(
                "**Knowledge Domain**"
            )


            domain_options = list(DOMAINS.keys()) + ["Other"]


            domain = st.selectbox(
                "Knowledge Domain",
                domain_options,
                label_visibility="collapsed"
            )


            custom_domain = ""


            if domain == "Other":

                custom_domain = st.text_input(
                    "Describe knowledge domain",
                    placeholder=(
                        "E.g., Cybersecurity, Legal, "
                        "Supply Chain..."
                    )
                )


    # ========================================================
    # SECTION 2 — TOPIC / QUESTION
    # ========================================================

    with st.container(border=True):

        st.markdown(
            '<div class="form-section-title">'
            '2. Intelligence Requirement'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            "**What is your topic, question, or knowledge requirement?**"
        )


        query = st.text_area(
            "Research Topic",
            height=140,
            placeholder=(
                "Example: Evaluate whether our engineering team "
                "should adopt a new backend technology for microservices."
            ),
            label_visibility="collapsed"
        )


    # ========================================================
    # SECTION 3 — DETAIL & SOURCES
    # ========================================================

    with st.container(border=True):

        st.markdown(
            '<div class="form-section-title">'
            '3. Detail & Supporting Sources'
            '</div>',
            unsafe_allow_html=True
        )


        col_length, col_sources = st.columns(2)


        # ----------------------------------------------------
        # OUTPUT LENGTH
        # ----------------------------------------------------

        with col_length:

            st.markdown(
                "**Detail & Length Level**"
            )


            output_length = st.radio(
                "Choose the level of detail",
                [
                    "Standard",
                    "Concise",
                    "Detailed",
                    "Custom"
                ],
                horizontal=True,
                label_visibility="collapsed"
            )


            if output_length == "Standard":

                max_words = 5000


            elif output_length == "Concise":

                max_words = 2500


            elif output_length == "Detailed":

                max_words = 7500


            else:

                max_words = st.number_input(
                    "Maximum word budget",
                    min_value=1000,
                    max_value=10000,
                    value=5000,
                    step=500
                )


            st.caption(
                f"Word target: **~{max_words:,} words**"
            )


        # ----------------------------------------------------
        # PUBLIC SOURCES
        # ----------------------------------------------------

        with col_sources:

            st.markdown(
                "**Additional Public Source Links (Optional)**"
            )


            source_links = st.text_area(
                "Public source links",
                height=110,
                placeholder=(
                    "Paste public GitHub, Google Drive, "
                    "or documentation URLs — one per line."
                ),
                label_visibility="collapsed"
            )


    # ========================================================
    # GENERATE BUTTON
    # ========================================================

    st.write("")


    if st.button(
        "Generate Intelligence",
        type="primary",
        use_container_width=True
    ):

        # ----------------------------------------------------
        # VALIDATE QUERY
        # ----------------------------------------------------

        if not query.strip():

            st.warning(
                "Please enter a business question or knowledge requirement."
            )

            st.stop()


        # ----------------------------------------------------
        # OUTPUT TYPE
        # ----------------------------------------------------

        final_output_type = output_type


        if output_type == "Other":

            if not custom_output_type.strip():

                st.warning(
                    "Please describe the output you want to create."
                )

                st.stop()


            final_output_type = custom_output_type.strip()


        # ----------------------------------------------------
        # DOMAIN
        # ----------------------------------------------------

        final_domain = domain


        if domain == "Other":

            if not custom_domain.strip():

                st.warning(
                    "Please enter a knowledge domain."
                )

                st.stop()


            final_domain = custom_domain.strip()


        # ====================================================
        # DOMAIN DETECTION
        # ====================================================

        with st.spinner(
            "Identifying knowledge domain..."
        ):

            detected_domain = validate_domain(query)


        col1, col2 = st.columns(2)


        with col1:

            st.html(f"""
            <div class="custom-callout">

                Selected Domain:
                <strong>{final_domain}</strong>

            </div>
            """)


        with col2:

            st.html(f"""
            <div class="custom-callout">

                Detected Domain:
                <strong>{detected_domain}</strong>

            </div>
            """)


        # ----------------------------------------------------
        # DOMAIN INFORMATION
        # ----------------------------------------------------

        if (
            final_domain in DOMAINS
            and detected_domain != final_domain
        ):

            st.caption(
                f"The question was also identified as "
                f"**{detected_domain}**, but your selected domain "
                f"**{final_domain}** will be used."
            )


        # ====================================================
        # GENERATION
        # ====================================================

        st.divider()


        st.subheader(
            "Building Intelligence"
        )


        research_status = st.empty()


        research_status.info(
            "Researching sources and preparing insights..."
        )


        st.divider()


        st.header(
            "ExperteezAI Intelligence"
        )


        section_placeholders = {}


        completed_sections = set()


        # ====================================================
        # RUN EXISTING AGENT
        # ====================================================

        for event in run_agent(
            domain=final_domain,
            query=query,
            output_type=final_output_type,
            output_length=max_words,
            public_sources=source_links
        ):


            # ------------------------------------------------
            # SECTION GENERATED
            # ------------------------------------------------

            if event["type"] == "section":

                research_status.info(
                    "Intelligence is being generated..."
                )


                section = event["section"]

                content = event["data"]


                completed_sections.add(
                    section
                )


                if section not in section_placeholders:

                    section_placeholders[section] = st.empty()


                placeholder = section_placeholders[
                    section
                ]


                placeholder.markdown(
                    content
                )


            # ------------------------------------------------
            # GENERATION COMPLETE
            # ------------------------------------------------

            elif event["type"] == "complete":

                research_status.success(
                    "Intelligence generation completed."
                )


                st.divider()


                st.success(
                    "Intelligence report completed successfully."
                )
