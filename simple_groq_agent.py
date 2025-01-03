from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile")
)

user_prompt = input("Enter your prompt: ")

# Get and print the response
agent.print_response(user_prompt)
