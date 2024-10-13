from openai import OpenAI

YOUR_API_KEY = "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"

messages = [
    {
        "role": "system",
        "content": (
            "You are an artificial intelligence assistant and you need to "
            "engage in a helpful, detailed, polite conversation with a user."
        ),
    },
    {
        "role": "user",
        "content": (
            "Count to 100, with a comma between each number and no newlines. "
            "E.g., 1, 2, 3, ..."
        ),
    },
]

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# demo chat completion without streaming
response = client.chat.completions.create(
    model="mistral-7b-instruct",
    messages=messages,
)
print(response)

# demo chat completion with streaming
response_stream = client.chat.completions.create(
    model="mistral-7b-instruct",
    messages=messages,
    stream=True,
)
for response in response_stream:
    print(response)