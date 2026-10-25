import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY not found!")
    print("Copy .env.example to .env and add your API key.")
    sys.exit(1)

client = OpenAI(api_key=api_key)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# Make the API call
print("Sending prompt: 'What is generative AI in one sentence?'")

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Be concise."
            },
            {
                "role": "user",
                "content": "What is generative AI in one sentence?"
            },
        ],
        temperature=0.7,
        max_tokens=100,
    )

    print(f"Response: {response.choices[0].message.content}")
    print(f"Tokens used: {response.usage.total_tokens}")

except AuthenticationError:
    print("Authentication failed. Check your OPENAI_API_KEY.")

except APIConnectionError:
    print("Could not connect to the OpenAI API. Check your internet connection.")

except Exception as e:
    print(f"Unexpected error: {e}")