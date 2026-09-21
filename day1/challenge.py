"""A question none of the three systems was designed for."""
from day1.venv.workflow import workflow
from day1.venv.agent import agent
 
QUESTION = "I can pay Rs. 30,000. Which two courses can I take together within this budget?"
 
print("Q:", QUESTION)
print("\nWorkflow :", workflow(QUESTION))
print("\nAgent    :", agent(QUESTION))
