# AI Customer Triage Engine 🤖

## Overview

This project is a technical implementation of an automated customer support triage pipeline. It demonstrates how to
bridge unstructured customer communication with structured business data.

Using the Google Gemini Flash SDK (2026 Standard), the engine analyzes incoming support queries, categorizes intent,
assesses priority and sentiment, and pushes the resulting structured analysis to a remote CRM endpoint via a REST API.

---

## Key Features

### Intelligent Classification

Uses an LLM to distinguish between nuanced categories such as:

- Billing
- Technical
- Sales

### Dynamic Testing Suite

Implements a synthetic test runner that pulls random scenarios from an external `queries.txt` source file.

### Strict JSON Schema

Enforces structural integrity for all outputs to ensure seamless integration with downstream systems.

### Containerized Infrastructure

Fully Dockerized for:

- Environment parity
- Simplified deployment
- Cross-platform compatibility

### Secure Configuration

Decoupled architecture using:

- `.env` files
- Industry-standard `.gitignore`
- `.dockerignore` protocols

---

## Technical Stack

- **Language:** Python 3.11 (optimized via Docker Slim)
- **AI Orchestration:** `google-genai` (Modern 2026 SDK)
- **Infrastructure:** Docker & Docker Compose
- **Architecture:** Multi-platform support (`linux/amd64`, `linux/arm64`)
- **Security:** `python-dotenv` for environment isolation and non-root Docker execution

---

## Project Structure

```text
triage_engine/
├── .dockerignore        # Build-context optimization
├── .gitignore           # Git exclusion rules
├── Dockerfile           # Multi-platform build instructions
├── docker-compose.yml   # Orchestration for environment & volumes
├── Main.py              # Core application logic
├── queries.txt          # Source file for synthetic test data
└── requirements.txt     # Project dependencies
```

---

## Getting Started (The Containerized Way)

The most reliable way to run the Triage Engine is using Docker. This ensures environment parity and handles all
dependencies automatically.

### 1. Clone the Repository

```bash
git clone https://github.com/skeptre/triage-engine.git
cd triage-engine
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=YOUR_GOOGLE_AI_STUDIO_KEY
```

### 3. Run with Docker Compose

```bash
docker compose up --build
```

---

## Deployment & Containerization Strategy

### Architecture Parity

The project is built to run identically on any environment, from local development machines to production cloud
clusters.

- **Multi-Arch Support:**  
  Using `docker buildx`, the image is cross-compiled for:
    - `linux/amd64` (standard Intel/AMD servers)
    - `linux/arm64` (Apple Silicon / ARM environments)

- **Resource Management:**  
  Built on `python:3.11-slim` to minimize attack surface and image size while maintaining efficiency.

---

## Cloud Registry

The latest stable image is pushed to Docker Hub, allowing instant deployment without requiring local source code:

```bash
docker pull skeptre/triage-engine:latest
```

---

## Architecture Flow

### 1. Ingestion

The system selects a random customer query from `queries.txt`.

### 2. Processing

Gemini 1.5 Flash analyzes the text using a structured system-instruction prompt.

### 3. Serialization

The AI response is parsed into a strictly validated Python dictionary.

### 4. Integration

The final payload is pushed via HTTP `POST` to a simulated CRM endpoint.

---

## Implementation Engineer Notes

During development, the engine evolved from a local Python script into a fully containerized service.

### Key Architectural Pivots

- **SDK Transition:**  
  Shifted to the native Google GenAI SDK for more robust pathing and native `response_mime_type` enforcement.

- **Infrastructure-as-Code:**  
  Implemented Docker Compose to manage:
    - Secrets injection
    - Persistent volume mapping for test data

- **Cross-Platform Delivery:**  
  Resolved Docker manifest mismatches by implementing a multi-platform build pipeline, ensuring the engine remains
  cloud-native and ready for standard Intel-based server deployments.

---

## Summary

The AI Customer Triage Engine demonstrates:

- End-to-end LLM integration into production pipelines
- Strict schema enforcement for structured outputs
- Cloud-native containerization practices
- Multi-architecture deployment readiness
- Secure configuration management

A lightweight, scalable, cloud-ready triage system designed for real-world integration.
