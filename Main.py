import json
import os
import random as rd
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Configuration
client = genai.Client(api_key=os.getenv("gemini_api_key"))
TARGET_WEBHOOK_URL = os.getenv("TARGET_WEBHOOK_URL")


def analyse_customer_query(customer_text):
    """Core AI Logic: Extracts sentiment and intent using British English context."""
    prompt = f"""
    Analyse the following customer support message and return ONLY a JSON object:
    "{customer_text}"
    
    JSON keys: category, priority, sentiment, suggested_action
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        config={'response_mime_type': 'application/json'}
    )
    return response.text


def apply_business_rules(analysis):
    """Consultancy Logic: Customises AI findings into actionable business rules."""
    # Rule 1: High Priority + Negative Sentiment = Urgent Escalation
    if analysis.get("priority") == "High" and analysis.get("sentiment") == "Negative":
        analysis["internal_note"] = "🚨 URGENT: High-risk customer. Immediate callback required."
        analysis["routing_target"] = "Senior Support Manager"

    # Rule 2: Positive Feedback = Marketing Opportunity
    elif analysis.get("sentiment") == "Positive":
        analysis["internal_note"] = "✨ Opportunity: Request a testimonial or Case Study."
        analysis["routing_target"] = "Marketing/Success Team"

    else:
        analysis["internal_note"] = "Standard processing."
        analysis["routing_target"] = "General Support Queue"

    return analysis


def push_to_client_system(data):
    """Integration Logic: Pushes structured data to the client's CRM via REST API."""
    try:
        response = requests.post(TARGET_WEBHOOK_URL, json=data)
        return response.status_code
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return 500


def run_simulation(iterations=3):
    """Enhanced Simulation: Demonstrates batch stability and error handling."""
    print(f"🚀 Starting AI Triage Simulation ({iterations} rounds)...")

    if not os.path.exists("queries.txt"):
        print("❌ Error: queries.txt not found.")
        return

    with open("queries.txt", "r", encoding="utf-8") as f:
        test_queries = [line.strip() for line in f.readlines() if line.strip()]

    for i in range(iterations):
        print(f"\n--- Round {i + 1} ---")
        sample_query = rd.choice(test_queries)
        print(f"🎲 Selected Query: '{sample_query}'")

        # 1. AI Analysis
        raw_analysis = analyse_customer_query(sample_query)
        analysis_dict = json.loads(raw_analysis)

        # 2. Business Rules (The 'Implementation Engineer' Step)
        final_payload = apply_business_rules(analysis_dict)

        # 3. Delivery
        print(f"📤 Pushing Enhanced JSON: {json.dumps(final_payload, indent=2)}")
        status = push_to_client_system(final_payload)

        if status == 200:
            print(f"✅ Round {i + 1} completed successfully!")


if __name__ == "__main__":
    run_simulation(iterations=3)
