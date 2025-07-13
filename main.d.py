# main.d.py  🧠 LEVEL 3: Make the Agent Remember Things  xxxxxx


from agents import Agent, Runner, ChatMessage
from tool import get_config

# Create the agent with memory
agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian of Pakistan. Answer clearly and remember the conversation.",
    use_memory=True  # 🧠 Enable memory!
)

# Welcome message
print("🧠 Ask anything about Pakistan's history. Type 'exit' to stop.\n")

# Conversation loop
while True:
    question = input("👤 You: ")
    if question.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    result = Runner.run_sync(agent, question, run_config=get_config())

    # Print the response
    print(f"🤖 SultanAssistant: {result.final_output}\n")
