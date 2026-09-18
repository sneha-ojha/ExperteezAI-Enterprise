from executor import execute_research
from reflection import reflect_on_results



def get_report_sections(output_type, output_length):

    # Concise = fewer, larger sections
    if output_length <= 2500:

        if output_type == "Leadership Brief":
            return [
                "Executive Summary",
                "Key Findings",
                "Business Implications",
                "Next Steps"
            ]

        if output_type == "Training & Onboarding":
            return [
                "Overview",
                "Key Concepts",
                "Practical Guidance",
                "Quick Reference"
            ]

        if output_type == "SOP / Process":
            return [
                "Purpose & Scope",
                "Procedure",
                "Important Checks",
                "Final Checklist"
            ]

        if output_type == "Decision Analysis":
            return [
                "Executive Summary",
                "Options & Comparison",
                "Risks & Trade-offs",
                "Decision Considerations"
            ]

        if output_type == "Knowledge Guide":
            return [
                "Overview",
                "Core Concepts",
                "Practical Understanding",
                "Key Takeaways"
            ]

        return [
            "Overview",
            "Key Findings",
            "Practical Guidance",
            "Next Steps"
        ]

    # Standard = balanced number of sections
    elif output_length <= 5000:

        if output_type == "Leadership Brief":
            return [
                "Executive Summary",
                "Business Context",
                "Key Findings",
                "Business Implications",
                "Risks & Considerations",
                "Next Steps"
            ]

        if output_type == "Training & Onboarding":
            return [
                "Overview",
                "Key Concepts",
                "How It Works",
                "Practical Examples",
                "Common Mistakes",
                "Quick Reference"
            ]

        if output_type == "SOP / Process":
            return [
                "Purpose & Scope",
                "Prerequisites",
                "Roles & Responsibilities",
                "Procedure",
                "Important Checks",
                "Exceptions & Risks",
                "Final Checklist"
            ]

        if output_type == "Decision Analysis":
            return [
                "Executive Summary",
                "Decision Context",
                "Available Options",
                "Evidence & Comparison",
                "Trade-offs & Risks",
                "Decision Considerations"
            ]

        if output_type == "Knowledge Guide":
            return [
                "Overview",
                "Core Concepts",
                "Detailed Explanation",
                "Examples",
                "Practical Considerations",
                "Key Takeaways"
            ]

        return [
            "Executive Summary",
            "Context",
            "Key Findings",
            "Detailed Analysis",
            "Practical Considerations",
            "Next Steps"
        ]

    # Detailed = more sections
    else:

        if output_type == "Leadership Brief":
            return [
                "Executive Summary",
                "Business Context",
                "Current Situation",
                "Key Findings",
                "Evidence Analysis",
                "Options & Alternatives",
                "Risks & Considerations",
                "Implementation Considerations",
                "Next Steps"
            ]

        if output_type == "Training & Onboarding":
            return [
                "Overview",
                "Prerequisites",
                "Core Concepts",
                "How It Works",
                "Detailed Explanation",
                "Practical Examples",
                "Common Mistakes",
                "Practical Exercises",
                "Quick Reference"
            ]

        if output_type == "SOP / Process":
            return [
                "Purpose & Scope",
                "Prerequisites",
                "Required Inputs",
                "Roles & Responsibilities",
                "Step-by-Step Procedure",
                "Important Checks",
                "Exceptions & Edge Cases",
                "Risks & Controls",
                "Final Checklist"
            ]

        if output_type == "Decision Analysis":
            return [
                "Executive Summary",
                "Decision Context",
                "Objectives & Criteria",
                "Available Options",
                "Evidence Analysis",
                "Detailed Comparison",
                "Trade-offs",
                "Risks & Constraints",
                "Decision Considerations"
            ]

        if output_type == "Knowledge Guide":
            return [
                "Overview",
                "Background",
                "Core Concepts",
                "Detailed Explanation",
                "How Different Concepts Connect",
                "Practical Examples",
                "Practical Considerations",
                "Limitations",
                "Key Takeaways"
            ]

        return [
            "Executive Summary",
            "Context",
            "Core Concepts",
            "Detailed Analysis",
            "Evidence",
            "Practical Applications",
            "Risks & Limitations",
            "Implementation Considerations",
            "Next Steps"
        ]


def run_specialist(
    query,
    domain,
    sources,
    output_type,
    output_length,
    public_sources
):

    # ---------------------------------------------------------
    # 1. SEARCH
    # ---------------------------------------------------------
    #
    # We intentionally skip the planner and evidence-synthesis
    # LLM calls here. They were adding latency before the user
    # saw anything.
    #
    search_results = execute_research(query, sources)

    # ---------------------------------------------------------
    # 2. CREATE THE REPORT STRUCTURE
    # ---------------------------------------------------------

    sections = get_report_sections(
        output_type,
        output_length
    )

    # ---------------------------------------------------------
    # 3. GENERATE SECTIONS ONE BY ONE
    # ---------------------------------------------------------

    for section in sections:

        content = reflect_on_results(
            domain=domain,
            query=query,
            plan="",
            evidence=search_results,
            section=section,
            output_type=output_type,
            output_length=output_length
        )

        yield {
            "type": "section",
            "section": section,
            "data": content
        }

    # ---------------------------------------------------------
    # 4. COMPLETE
    # ---------------------------------------------------------

    yield {
        "type": "complete"
    }