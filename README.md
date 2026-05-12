# GrossphereOne

> AI-powered automation platform for modern businesses.

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![Part of](https://img.shields.io/badge/Voltex%20Network-FCRI-purple.svg)](https://fcri.science)

GrossphereOne is a **no-code AI workflow automation platform** — enabling startups and businesses to automate operations, orchestrate infrastructure, and deploy intelligent agents without becoming AI engineers first.

---

## Architecture

```
User / Business
      │
      ▼
┌─────────────────────────┐
│     GrossphereOne       │
│                         │
│  ┌──────────────────┐   │
│  │  Workflow Engine │   │   Define → Run → Monitor
│  └────────┬─────────┘   │
│           │              │
│  ┌────────▼─────────┐   │
│  │   Agent Layer    │   │   Intelligent task execution
│  └────────┬─────────┘   │
│           │              │
│  ┌────────▼─────────┐   │
│  │  Integrations    │   │   APIs, webhooks, services
│  └──────────────────┘   │
└─────────────────────────┘
           │
           ▼
    AIKA → Ayooni → Automation
    (Voltex Network backbone)
```

---

## Structure

```
grosphereone/
├── agents/
│   └── workflow_agent.py    AI agent for workflow execution
├── api/
│   └── server.py            FastAPI HTTP server
├── dashboard/               Operations monitoring UI
├── integrations/            Third-party service connectors
├── platform/                Core platform infrastructure
├── workflows/               Built-in workflow templates
│   └── customer_signup.py   Example: automated customer onboarding
└── docs/                    Platform documentation
```

---

## Quick Start

```bash
git clone https://github.com/Davidcarmelalex/grosphereone
cd grosphereone
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api.server:app --reload --port 8300
```

API available at `http://localhost:8300`

---

## API

### Run a Workflow
```http
POST /workflows/run
Content-Type: application/json

{
  "name": "customer_signup",
  "data": {
    "email": "user@example.com",
    "plan": "starter"
  }
}
```

### Health Check
```http
GET /
→ {"platform": "GrossphereOne"}
```

---

## Built-in Workflow Templates

| Workflow | Description |
|----------|-------------|
| `customer_signup` | Automated customer onboarding flow |
| `lead_qualification` | AI-powered lead scoring and routing |
| `invoice_processing` | Document extraction and payment workflow |
| `support_triage` | Intelligent ticket routing and prioritization |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Part of the [Voltex Network](https://fcri.science).
