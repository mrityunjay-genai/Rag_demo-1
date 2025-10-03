
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("EURI_API_KEY")

def generate_completion(prompt):
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "messages": [{"role": "user","content": prompt}],
        "model": "gpt-4.1-nano",
        "max_tokens": 100,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()['choices'][0]["message"]["content"]
