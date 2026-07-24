from specialists.technology import technology_specialist
from specialists.medicine import medicine_specialist
from specialists.business import business_specialist
from specialists.history import history_specialist
from specialists.sports import sports_specialist
from specialists.fashion import fashion_specialist

def route(domain):
    routes = {
        "Technology": technology_specialist,
        "Medicine": medicine_specialist,
        "Business": business_specialist,
        "History": history_specialist,
        "Sports": sports_specialist,
        "Fashion": fashion_specialist
    }
    return routes.get(domain)