from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # valor cualquiera, se ignora
)

resp = client.chat.completions.create(
    model="llama3.1",
    messages=[{"role": "user", "content": "Resume en 2 frases qué es Podman."}],
)

print(resp.choices[0].message.content)