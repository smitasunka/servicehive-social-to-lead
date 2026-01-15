def detect_intent(message: str):
    msg = message.lower()

    # High intent first
    if any(word in msg for word in ["sign up", "try", "subscribe", "buy", "start"]):
        return "high_intent"

    # Product or pricing inquiry
    if any(word in msg for word in ["price", "pricing", "cost", "plan", "features"]):
        return "product_query"

    # Casual greeting (lowest priority)
    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "greeting"

    return "unknown"

