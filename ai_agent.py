import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = os.getenv("GEMINI_MODEL", "models/gemini-2.5-flash")
model = genai.GenerativeModel(MODEL_NAME)


def generate_test_steps(requirement: str):
    """
    Converts a natural language requirement into structured test steps.
    Output is STRICT JSON for Selenium compatibility.
    """

    prompt = f"""
You are a software QA engineer.

Requirement:
"{requirement}"

Task:
Convert the requirement into test steps in STRICT JSON format.

Rules:
- Output ONLY valid JSON
- No markdown, no explanations
- Use ONLY these actions: navigate, input, click, check
- Use ONLY id selectors
- Assume a login page with:
  - username (input id)
  - password (input id)
  - button (login button)
  - message (result text)

Expected JSON format:
[
  {{ "action": "navigate" }},
  {{ "action": "input", "selector": "username", "value": "wronguser" }},
  {{ "action": "input", "selector": "password", "value": "wrongpass" }},
  {{ "action": "click", "selector": "button" }},
  {{ "action": "check", "selector": "message", "value": "Invalid" }}
]
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON returned by Gemini:\n{text}")