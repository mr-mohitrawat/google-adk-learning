from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",   # any non-empty string works
)

response = client.chat.completions.create(
    model="llama3.1:latest",
    messages=[
        {
            "role": "user",
            "content": "Who are you?"
        }
    ]
)

print(response.choices[0].message.content)