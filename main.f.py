# main.py    ✨ Updated main.py with Manual Memory      xxxxxx

from agents import Agent, Runner
from tool import get_config

# Create your stateless agent
agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian of Pakistan. Keep track of past conversation and answer clearly."
)

# Manual memory (list of strings)
conversation_history = []

print("🧠 Ask anything about Pakistan's history. Type 'exit' to stop.\n")

while True:
    question = input("👤 You: ")
    if question.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    # Combine history with current question
    full_prompt = "\n".join(conversation_history + [f"User: {question}"])

    # Run the agent with history
    result = Runner.run_sync(agent, full_prompt, run_config=get_config())

    # Save to memory
    conversation_history.append(f"User: {question}")
    conversation_history.append(f"Assistant: {result.final_output}")

    # Show result
    print(f"🤖 SultanAssistant: {result.final_output}\n")
