from planner import create_research_plan
from executor import execute_research
from reflection import reflect_on_results
from synthesizer import synthesize_evidence

def run_specialist(

    query,

    domain,

    sources

):

    plan = create_research_plan(

        domain,

        query

    )

    results = execute_research(

        query=query,

        sources=sources

    )

    evidence = synthesize_evidence(

        domain,

        query,

        plan,

        results

    )

    report = reflect_on_results(

        domain,

        query,

        plan,

        evidence

    )

    return {

        "plan": plan,

        "evidence": evidence,

        "reflection": report

    }