# main.py  2. RUN LEVEL  V.V.IMPORTANT  !!!!

from agents import Agent, Runner
from tool import get_config

# Create the agent with custom name and instructions
agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian specialized in Pakistan's history. Answer all questions truthfully and clearly."
)

# Define the question
question = "Who was the first Prime Minister of Pakistan?"

# Run the agent synchronously
result = Runner.run_sync(agent, question, run_config=get_config())

# Output result
print("Answer:", result.final_output)
