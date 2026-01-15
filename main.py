
from agent.intent import detect_intent
from agent.rag import answer_query
from tools.lead_capture import mock_lead_capture

state = {}

print("AutoStream AI Agent (type 'exit' to quit)")

while True:
    user = input("User: ")
    if user.lower() == "exit":
        break

    intent = detect_intent(user)

    if intent == "greeting":
        print("Agent: Hi! How can I help you today?")

    elif intent == "product_query":
        response = answer_query(user)
        print(f"Agent: {response}")

    elif intent == "high_intent":
        print("Agent: Great! I just need a few details.")
        name = input("Name: ")
        email = input("Email: ")
        platform = input("Creator Platform: ")
        mock_lead_capture(name, email, platform)

    else:
        print("Agent: Can you please clarify your request?")
