
# Social-to-Lead Agentic Workflow – ServiceHive

## Overview
This project implements a conversational AI agent for a fictional SaaS product called AutoStream.
The agent can answer product queries, detect high-intent users, and capture leads using a mock tool.

## Tech Stack
- Python 3.9+
- LangChain-style modular architecture
- Rule-based intent detection
- Local RAG using JSON knowledge base

## How to Run
```
python main.py
```

## Architecture Explanation
The system is divided into modular components for intent detection, retrieval, and tool execution.
Intent detection classifies user input into greetings, product queries, or high-intent leads.
RAG is implemented using a local JSON knowledge base to ensure accurate, grounded responses.
State is maintained during runtime to manage multi-turn conversations.
This structure mirrors real-world GenAI agent design while remaining simple and extensible.

## WhatsApp Integration (Concept)
This agent could be integrated with WhatsApp using Webhooks via Twilio.
Incoming messages would trigger the agent backend, and responses would be sent back through the WhatsApp API.
Session IDs would maintain user state across messages.
