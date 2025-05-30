import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"


def ask_ai(prompt):
    response = openai.ChatCompletion.create(
       model="mistralai/mistral-7b-instruct",
       messages=[{"role": "user", "content": prompt}]
    )
    return(response.choices[0].message["content"])
