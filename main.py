# main.py

from agents import Agent, Runner
from tool import get_config

# 1. Create your assistant (no built-in memory needed)
agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian of Pakistan. Answer clearly. Maintain the context of the conversation."
)

# 2. Manual memory storage
conversation_history = []

print("🧠 Ask anything about Pakistan's history. Type 'exit' to stop.\n")

# 3. Conversation loop
while True:
    question = input("👤 You: ")
    if question.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    # 4. Build the full prompt by appending previous Q&As
    full_prompt = "\n".join(conversation_history + [f"User: {question}"])

    # 5. Run agent with context
    result = Runner.run_sync(agent, full_prompt, run_config=get_config())

    # 6. Print and store the conversation
    print(f"🤖 SultanAssistant: {result.final_output}\n")
    conversation_history.append(f"User: {question}")
    conversation_history.append(f"Assistant: {result.final_output}")
