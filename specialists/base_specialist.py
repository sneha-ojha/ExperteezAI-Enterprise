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


def run_specialist(

    query,

    domain,

    sources

):

    # -----------------------------------------
    # STEP 1 : Create Research Plan
    # -----------------------------------------

    plan = create_research_plan(

        domain,

        query

    )

    # -----------------------------------------
    # STEP 2 : Execute Research
    # -----------------------------------------

    results = execute_research(

        query=query,

        sources=sources

    )

    # -----------------------------------------
    # STEP 3 : Organize Evidence
    # -----------------------------------------

    evidence = synthesize_evidence(

        domain,

        query,

        plan,

        results

    )

    # -----------------------------------------
    # STEP 4 : Build Report Section-by-Section
    # -----------------------------------------

    report = "# ExperteezAI Research Report\n\n"

    for section in REPORT_SECTIONS:

        print(f"Writing {section}...")

        chapter = reflect_on_results(

            domain=domain,

            query=query,

            plan=plan,

            evidence=evidence,

            section=section

        )

        report += chapter.strip()

        report += "\n\n"

    # -----------------------------------------
    # STEP 5 : Return Everything
    # -----------------------------------------

    return {

        "plan": plan,

        "evidence": evidence,

        "reflection": report

    }