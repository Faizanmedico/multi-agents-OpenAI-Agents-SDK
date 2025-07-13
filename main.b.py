#  🧠 main.b.py (multi-question version)


from agents import Agent, Runner
from tool import get_config

# Step 1: Create your custom agent
agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian specialized in Pakistan's history. Answer clearly and truthfully."
)

# Step 2: List of questions to ask
questions = [
    "Who was the first Prime Minister of Pakistan?",
    "When did Pakistan become a nuclear power?",
    "Who was the founder of Pakistan?",
    "What is the significance of 23rd March in Pakistan?"
]

# Step 3: Ask each question one-by-one
for q in questions:
    print(f"\n🧠 Question: {q}")
    result = Runner.run_sync(agent, q, run_config=get_config())
    print(f"💬 Answer: {result.final_output}")
