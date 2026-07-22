from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama3.1:latest",
        messages=messages
    )

    answer = response.choices[0].message.content

    print(f"AI: {answer}")

    messages.append({
        "role": "assistant",
        "content": answer
    })