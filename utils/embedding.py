
import requests
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EURI_API_KEY")

def get_embeddings(text):
    url = "https://api.euron.one/api/v1/euri/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "input": text,
        "model": "text-embedding-3-small"
    }

    response = requests.post(url, headers=headers, json=payload)

    embedding = np.array(response.json()['data'][0]['embedding'])
    
    return embedding
    

# retrieve_embedding = get_embeddings(chunks[0])

# print(retrieve_embedding)
# print(retrieve_embedding.shape[0])