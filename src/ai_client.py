import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

with open("prompt_templates/eval_LLM_template.txt", "r") as f:
    eval_template = f.read()

INSTRUCTIONS = """You are an AI assistant that extracts structured information from text.
Always return a JSON object matching this schema:

{
  "entities": {
    "person": [list of names, or empty list if none found],
    "organization": [list of organizations, or empty list if none found],
    "location": [list of locations, or empty list if none found],
    "technology": [list of technologies, or empty list if none found],
    "threat_actor": [list of named or anonymous threat actors, or empty list if none found],
    "vulnerabilities": [list of specific vulnerabilities, or empty list if none found],
    "events": [list of key events, or empty list if none found]
  },
  "threat_analysis": {
    "threat_type": "One of: Physical, Cybersecurity, Political, Other",
    "description": "Summary of the core threat described",
    "severity": "Low | Medium | High | Critical",
    "likelihood": "Unlikely | Possible | Likely | Certain",
    "recommended_actions": ["List of specific mitigations, or empty list if none found"]
  },
  "confidence": 0.0 to 1.0
}

Important:
- Always include ALL fields, even if empty
- Use empty lists [] for any entity type where no information was found
- Do not omit any fields from the response
- Only output valid JSON. Do not include any other commentary or add or remove fields."""

def ask_ai(prompt: str) -> dict:
    response = openai.ChatCompletion.create(
       model="mistralai/mistral-7b-instruct",
       messages=[{"role": "system", "content": INSTRUCTIONS + "Text to analyze: " + prompt}]
    )
    return(response.choices[0].message["content"])
