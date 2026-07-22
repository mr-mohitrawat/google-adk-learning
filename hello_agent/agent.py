from google.adk.agents import Agent

root_agent = Agent(
    name="hello_agent",
    model="gemini-2.5-flash",
    description="A simple chatbot",
    instruction="""
    You are a helpful AI assistant.
    Answer clearly and concisely.
    """,
)