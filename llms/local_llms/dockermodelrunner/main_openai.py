from openai import OpenAI
import os

BASE_URL = "http://localhost:12434/engines/llama.cpp/v1/"

client = OpenAI(base_url=BASE_URL, api_key="anything")

MODEL_NAME = "ai/smollm2"

PROMPT = "Hello, how are you?"

messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": PROMPT}
           ]

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=messages
)

# Print the response from the local docker model runner server
print(response.choices[0].message.content)