# main.py

from agents import Agent, Runner
from tool import get_config

agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian specialized in Pakistan's history. Answer clearly and truthfully."
)

print("🧠 Ask me anything about Pakistan's history. Type 'exit' to quit.\n")

while True:
    question = input("👤 You: ")
    if question.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    result = Runner.run_sync(agent, question, run_config=get_config())
    print(f"🤖 SultanAssistant: {result.final_output}\n")
