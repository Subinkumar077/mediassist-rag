from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os
import yaml

load_dotenv()

_CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"
with open(_CONFIG_PATH) as f:
    config = yaml.safe_load(f)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt, stream=True):
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "llama3-70b-8192"),
        messages=[{"role": "user", "content": prompt}],
        max_tokens=config['max_tokens_output'],
        temperature=config['temperature'],
        stream=stream
    )
    if stream:
        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
    else:
        return response.choices[0].message.content
