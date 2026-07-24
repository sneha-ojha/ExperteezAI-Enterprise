from specialists.base_specialist import run_specialist


def medicine_specialist(query):

    return run_specialist(
        query=query,
        system_prompt="Medicine"
    )