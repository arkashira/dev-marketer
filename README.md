<h3 align="center">🛠️ dev‑marketer</h3>

<div align="center">
  <a href="https://github.com/yourusername/dev-marketer/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://github.com/yourusername/dev-marketer"><img src="https://img.shields.io/badge/python-3.11%2B-blue.svg" alt="Python 3.11+"></a>
  <a href="https://github.com/yourusername/dev-marketer/actions"><img src="https://img.shields.io/github/actions/workflow/status/yourusername/dev-marketer/ci.yml?branch=main&label=build" alt="Build Status"></a>
  <a href="https://github.com/yourusername/dev-marketer/stargazers"><img src="https://img.shields.io/github/stars/yourusername/dev-marketer.svg?style=social" alt="Stars"></a>
</div>

---

# 🚀 dev‑marketer
**Power indie developers with automated growth‑hacking tools.**  
A lightweight growth‑automation platform that lets solo creators launch, promote, and iterate on their products without leaving the command line.

## Why dev‑marketer?
- **Zero‑code campaigns** – Build email, social, and referral funnels with a single YAML file.  
- **Real‑time analytics** – Dashboard shows acquisition, conversion, and churn metrics updated every minute.  
- **Built for indie devs** – Designed for teams of 1‑3 who need fast ROI on marketing spend.  
- **Open‑source & extensible** – Plug‑in architecture lets you add custom channels or data sources.  
- **Privacy‑first** – All data stays in‑process or in your own cloud storage; no hidden trackers.  

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Campaign Builder** | Define multi‑channel campaigns (email, Twitter, Reddit) via declarative YAML. |
| **A/B Testing Engine** | Split‑test subject lines, ad copy, and landing pages with statistical confidence reporting. |
| **Analytics Dashboard** | Live charts for clicks, sign‑ups, LTV, and funnel drop‑off. |
| **Automation Scheduler** | Cron‑style triggers for drip emails, retargeting posts, and webhook callbacks. |
| **Integrations** | Native adapters for SendGrid, Mailgun, Twitter API, Discord webhooks, and custom webhooks. |
| **Export / Reporting** | CSV/JSON export of campaign results; one‑click PDF summary generation. |

## Tech Stack
> **Note:** The tech‑stack is defined in `decisions/tech-stack.md`. At present the project is a pure Python package.

- **Python 3.11+**
- **Poetry** (or `pip`) for dependency management
- **FastAPI** for the HTTP API layer
- **SQLModel / SQLite** for lightweight persistence
- **Jinja2** for templated email generation
- **Docker** (optional) for containerised deployment
- **GitHub Actions** for CI/CD

## Project Structure
```
dev-marketer/
├─ business/          # Domain‑specific logic (campaign orchestration)
├─ src/               # Core library (FastAPI app, models, services)
├─ tests/             # Unit & integration test suite
├─ pyproject.toml     # Build system, entry points, dependencies
├─ requirements.txt   # Pin‑exact versions for CI
└─ README.md          # ← you are here
```

## Getting Started

```bash
# 1️⃣ Clone the repo
git clone https://github.com/yourusername/dev-marketer.git
cd dev-marketer

# 2️⃣ Install dependencies (using pip)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3️⃣ Run the development server
uvicorn src.main:app --reload --port 8000
```

The entry point defined in `pyproject.toml` also allows:

```bash
# If you prefer Poetry
poetry install
poetry run dev-marketer  # launches the FastAPI server
```

### Running the Test Suite

```bash
# Using pytest (installed via requirements.txt)
pytest -vv
```

## Deploy

The application can be deployed to any environment that runs a standard Python service.

### Docker (recommended)

```bash
# Build the image
docker build -t dev-marketer:latest .

# Run the container
docker run -p 8000:8000 dev-marketer:latest
```

### Platform‑as‑a‑Service

- **Railway / Fly.io** – point to the repository and set the start command to `uvicorn src.main:app --host 0.0.0.0 --port $PORT`.
- **Heroku** – add a `Procfile` with `web: uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000}`.

## Status
🟢 **Active development** – latest build `b619b6b` (code‑build cycle 20260609‑025311‑dev‑mark).

## Contributing
Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose fixes, add features, or improve documentation.

## License
Released under the **MIT License**.