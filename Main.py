import json
import os
import random as rd
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("gemini_api_key"))
TARGET_WEBHOOK_URL = os.getenv("TARGET_WEBHOOK_URL")


def analyze_customer_query(customer_text):
    prompt = f"""
    Analyze the following customer support message and return ONLY a JSON object:
    "{customer_text}"
    
    JSON keys: category, priority, sentiment, suggested_action
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
        config={
            'response_mime_type': 'application/json'
        }
    )
    return response.text


def push_to_client_system(data):
    response = requests.post(TARGET_WEBHOOK_URL, json=data)
    return response.status_code


def run_simulation():
    """Encapsulates the testing logic for easy execution."""
    if os.path.exists("queries.txt"):
        with open("queries.txt", "r") as f:
            test_queries = f.readlines()
        sample_query = rd.choice(test_queries).strip()
    else:
        sample_query = "Default query: The queries.txt file was not found!"

    print(f"🎲 Source: queries.txt | Selected: '{sample_query}'")
    print("🤖 Analyzing Query via Modern GenAI SDK...")

    # Run the core logic
    analysis = analyze_customer_query(sample_query)
    analysis_dict = json.loads(analysis)

    print(f"📤 Pushing Analysis: {analysis}")
    status = push_to_client_system(analysis_dict)

    if status == 200:
        print("✅ Success: Data delivered to Webhook.site.")


# This is the "Ignition Switch"
if __name__ == "__main__":
    run_simulation()
