from openai import OpenAI
import json

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
tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiply two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtract",
            "description": "Subtract two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
            "type": "function",
            "function": {
                "name": "temperature",
                "description": "Get the latest temperature",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                    },
                    "required": ["city"]
                }
            }
    }
]

def add(a: int, b: int):
    return a + b

def multiply(a: int, b: int):
    return a * b

def subtract(a: int, b: int):
    return a - b

def temperature(city: str):
    # Dummy implementation
    return f"The temperature in {city} is 28°C"

tool_functions = {
    "add": add,
    "multiply": multiply,
    "subtract": subtract,
    "temperature": temperature,
}

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="qwen3-coder:30b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:

        tool_call = message.tool_calls[0]

        tool_name = tool_call.function.name

        args = json.loads(tool_call.function.arguments)

        result = tool_functions[tool_name](**args)

        print("Tool Result:", result)

        messages.append(message)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })
        response = client.chat.completions.create(
            model="qwen3-coder:30b",
            messages=messages,
            tools=tools
        )

    answer = response.choices[0].message.content

    print(f"AI: {answer}")

    messages.append({
        "role": "assistant",
        "content": answer
    })