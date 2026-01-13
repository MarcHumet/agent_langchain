import requests
import json

URL = "http://localhost:11434/api/chat"

messages = [
    {"role": "system", "content": "Eres un asistente experto en Python."},
    {"role": "user", "content": "Escribe una función que calcule la media de una lista."},
]

payload = {
    "model": "llama3.2",
    "messages": messages,
    "stream": True,
}

with requests.post(URL, json=payload, stream=True) as resp:
    resp.raise_for_status()
    for line in resp.iter_lines():
        if not line:
            continue
        data = json.loads(line)
        msg = data.get("message", {})
        content = msg.get("content", "")
        print(content, end="", flush=True)
        if data.get("done"):
            break