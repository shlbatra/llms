import ollama

url = "http://localhost:11434/api/chat"

model = "smollm2"

messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]

response = ollama.chat(model=model, messages=messages)

# Print the response from the local Ollama server
print(response["message"]["content"])