import requests

url = "http://localhost:11434/api/chat"

data = {
    "model": "smollm2",
    "stream": False,
    "messages": [
        {"system": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
}

response = requests.post(url, json=data)
response.raise_for_status()

# Print the response from the local Ollama server
print(response.json()["message"]["content"])