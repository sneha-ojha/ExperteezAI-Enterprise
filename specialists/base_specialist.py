from planner import create_research_plan
from executor import execute_research
from reflection import reflect_on_results
from synthesizer import synthesize_evidence


def run_specialist(query, system_prompt):

    plan = create_research_plan(
        domain=system_prompt,
        query=query
    )

    results = execute_research(query)

    evidence = synthesize_evidence(
        domain=system_prompt,
        query=query,
        plan=plan,
        search_results=results
    )

    reflection = reflect_on_results(
        domain=system_prompt,
        query=query,
        plan=plan,
        evidence=evidence
    )

    return {
        "plan": plan,
        "evidence": evidence,
        "reflection": reflection
    }