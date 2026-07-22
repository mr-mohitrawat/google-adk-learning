from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="hello_agent",
    model=LiteLlm(model = "ollama_chat/llama3.1:latest"),
    description="A simple chatbot",
    instruction="""
    You are a helpful AI assistant.
    Answer clearly and concisely.
    """,
)