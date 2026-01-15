
import json

def load_knowledge():
    with open("data/knowledge_base.json") as f:
        return json.load(f)

def answer_query(query):
    kb = load_knowledge()
    q = query.lower()

    if "basic" in q:
        plan = kb["pricing"]["Basic"]
        return (
            "Basic Plan:\n"
            f"- Price: {plan['price']}\n"
            f"- Features: {', '.join(plan['features'])}"
        )

    if "pro" in q:
        plan = kb["pricing"]["Pro"]
        return (
            "Pro Plan:\n"
            f"- Price: {plan['price']}\n"
            f"- Features: {', '.join(plan['features'])}"
        )

    basic = kb["pricing"]["Basic"]
    pro = kb["pricing"]["Pro"]

    return (
        "Here are our pricing plans:\n\n"
        "Basic Plan:\n"
        f"- Price: {basic['price']}\n"
        f"- Features: {', '.join(basic['features'])}\n\n"
        "Pro Plan:\n"
        f"- Price: {pro['price']}\n"
        f"- Features: {', '.join(pro['features'])}"
    )
