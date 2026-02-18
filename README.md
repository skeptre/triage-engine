# AI Customer Triage Engine 🤖

### **Overview**

This project is a technical implementation of an automated customer support triage pipeline. It demonstrates how to
bridge unstructured customer communication with structured business data. Using the **Google Gemini Flash SDK (2026
Standard)**, the engine analyzes incoming support queries, categorizes intent, assesses priority/sentiment, and pushes
the resulting analysis to a remote CRM endpoint via a REST API.

---

### **Key Features**

* **Intelligent Classification:** Uses an LLM to distinguish between nuanced categories like Billing, Technical, and
  Sales.
* **Dynamic Testing Suite:** Implements a synthetic test runner that pulls random scenarios from an external
  `queries.txt` source.
* **Strict JSON Schema:** Enforces structural integrity for all outputs to ensure seamless integration with downstream
  client systems.
* **Secure Configuration:** Fully decoupled architecture using `.env` files and industry-standard `.gitignore` security
  protocols.

---

### **Technical Stack**

* **Language:** Python 3.14
* **AI Orchestration:** `google-genai` (Modern 2026 SDK)
* **Data Delivery:** RESTful API (POST) via `requests`
* **Security:** `python-dotenv` for environment isolation

---

### **Project Structure**

```text
triage_engine/
├── .venv/               # Local virtual environment (ignored by Git)
├── .env                 # Private API keys (ignored by Git)
├── .gitignore           # Git exclusion rules
├── Main.py              # Core application logic
├── queries.txt          # Source file for synthetic test data
└── requirements.txt     # Project dependencies
```

Setup & Installation

Clone the repository:

git clone [https://github.com/skeptre/triage-engine.git](https://github.com/skeptre/triage-engine.git)
cd triage-engine

Set up your Virtual Environment:
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt


Configure Environment Variables:
Create a .env file in the root directory:
gemini_api_key=YOUR_GOOGLE_AI_STUDIO_KEY

Run the Engine:
python Main.py
Architecture Flow

```
Ingestion: The system selects a random customer query from queries.txt.

Processing: Gemini 1.5 Flash analyzes the text with a system-instruction prompt.

Serialization: The AI response is parsed into a Python dictionary.

Integration: The final payload is pushed via HTTP POST to a simulated CRM endpoint (Webhook.site).

Implementation Engineer Notes

During the development of this engine, I pivoted from an OpenAI-compatibility bridge to the native Google GenAI SDK.
This decision was made to ensure more robust pathing for the v1beta endpoint and to utilize native response_mime_type
enforcement, which significantly increases reliability in structured data extraction.
```
