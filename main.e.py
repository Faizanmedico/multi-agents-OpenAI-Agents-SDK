# main.py   ✅ Final Working main.py with .with_memory():       xxxxxx


from agents import Agent, Runner
from tool import get_config

# Create the agent and enable memory
agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian of Pakistan. Answer clearly and remember the conversation."
).with_memory()  # 🧠 This enables memory in supported SDK versions

print("🧠 Ask anything about Pakistan's history. Type 'exit' to stop.\n")

while True:
    question = input("👤 You: ")
    if question.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    result = Runner.run_sync(agent, question, run_config=get_config())
    print(f"🤖 SultanAssistant: {result.final_output}\n")
