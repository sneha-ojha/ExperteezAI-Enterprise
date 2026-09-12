import time

from concurrent.futures import ThreadPoolExecutor, as_completed

from planner import create_research_plan
from executor import execute_research
from reflection import reflect_on_results
from synthesizer import synthesize_evidence


REPORT_SECTIONS = [
    "Executive Brief",
    "Research Objective",
    "Research Methodology",
    "Current State of Knowledge",
    "Evidence Analysis",
    "Comparative Discussion",
    "Scientific Consensus",
    "Research Limitations",
    "Future Research Directions",
    "Practical Implications",
    "Conclusion"
]


def generate_section(section, domain, query, plan, evidence):

    try:

        print(f"Writing {section}...")

        start = time.perf_counter()

        chapter = reflect_on_results(
            domain=domain,
            query=query,
            plan=plan,
            evidence=evidence,
            section=section
        )

        elapsed = time.perf_counter() - start

        print(
            f"   ⏱️ {section}: "
            f"{elapsed:.2f} seconds"
        )

        return section, chapter

    except Exception as e:

        print(
            f"❌ Error writing {section}: "
            f"{type(e).__name__}: {e}"
        )

        return section, (
            f"## {section}\n\n"
            f"Unable to generate this section."
        )


def run_specialist(
    query,
    domain,
    sources
):

    total_start = time.perf_counter()

    # -----------------------------------------
    # STEP 1 : Create Research Plan
    # -----------------------------------------

    start = time.perf_counter()

    plan = create_research_plan(
        domain,
        query
    )

    print(
        f"⏱️ Research Planner: "
        f"{time.perf_counter() - start:.2f} seconds"
    )

    # Send plan to Streamlit immediately
    yield {
        "type": "plan",
        "data": plan
    }

    # -----------------------------------------
    # STEP 2 : Execute Research
    # -----------------------------------------

    start = time.perf_counter()

    results = execute_research(
        query=query,
        sources=sources
    )

    print(
        f"⏱️ Parallel Search: "
        f"{time.perf_counter() - start:.2f} seconds"
    )

    # Send search completion immediately
    yield {
        "type": "search_complete"
    }

    # -----------------------------------------
    # STEP 3 : Organize Evidence
    # -----------------------------------------

    start = time.perf_counter()

    evidence = synthesize_evidence(
        domain,
        query,
        plan,
        results
    )

    print(
        f"⏱️ Evidence Synthesis: "
        f"{time.perf_counter() - start:.2f} seconds"
    )

    # Send evidence completion immediately
    yield {
        "type": "evidence",
        "data": evidence
    }

    # -----------------------------------------
    # STEP 4 : Generate Report Sections
    #          IN PARALLEL
    # -----------------------------------------

    reflection_start = time.perf_counter()

    MAX_CONCURRENT_SECTIONS = 2

    with ThreadPoolExecutor(
        max_workers=MAX_CONCURRENT_SECTIONS
    ) as executor:

        futures = {
            executor.submit(
                generate_section,
                section,
                domain,
                query,
                plan,
                evidence
            ): section
            for section in REPORT_SECTIONS
        }

        for future in as_completed(futures):

            section, chapter = future.result()

            # Send each section immediately
            yield {
                "type": "section",
                "section": section,
                "data": chapter
            }

    print(
        f"⏱️ Parallel Reflection: "
        f"{time.perf_counter() - reflection_start:.2f} seconds"
    )

    # -----------------------------------------
    # STEP 5 : Research Complete
    # -----------------------------------------

    print(
        f"\n🚀 TOTAL RESEARCH TIME: "
        f"{time.perf_counter() - total_start:.2f} seconds\n"
    )

    yield {
        "type": "complete"
    }