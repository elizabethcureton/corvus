import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

response = openai.ChatCompletion.create(
    model="mistralai/mistral-7b-instruct",
    messages=[{"role": "user", "content": "What country is Paris in?"}]
)

print(response.choices[0].message["content"])
