import requests
import json

URL = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2",  # o el modelo que tengas: llama3, qwen2.5, etc.
    "prompt": "Explícame la diferencia entre Podman y Docker en 3 puntos.",
    "stream": True,       # streaming token a token
}

with requests.post(URL, json=payload, stream=True) as resp:
    resp.raise_for_status()
    for line in resp.iter_lines():
        if not line:
            continue
        data = json.loads(line)
        chunk = data.get("response", "")
        print(chunk, end="", flush=True)
        if data.get("done"):
            break