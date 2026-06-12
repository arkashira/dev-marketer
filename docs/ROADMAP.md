# ROADMAP.md – dev‑marketer

## Vision
Create a lightweight, self‑hosted marketing automation engine that lets SMBs and growth teams control outbound email volume, enforce compliance limits, and gain simple analytics—all without vendor lock‑in or complex SaaS contracts.

---

## Milestones Overview

| Milestone | Target Release | Core Theme | MVP‑Critical Items* |
|-----------|----------------|------------|---------------------|
| **MVP**   | **2026‑07‑15** | **Foundational Engine** | ✅ Core `MarketingAutomation` class<br>✅ Monthly email quota enforcement<br>✅ `send_email`, `display_limit_usage`, `increase_limit` APIs<br>✅ Unit test suite (pytest) |
| **v1.0**  | 2026‑09‑30 | **Usability & Extensibility** | ✅ CLI & basic web UI<br>✅ Template‑based email composition<br>✅ Scheduler (cron‑style) |
| **v1.5**  | 2026‑11‑15 | **Integrations & Analytics** | ✅ SMTP provider plug‑ins (SendGrid, Mailgun)<br>✅ Simple dashboard (sent / blocked / quota)<br>✅ Export CSV reports |
| **v2.0**  | 2027‑02‑28 | **Automation & Growth** | ✅ Trigger rules (event‑driven, list‑based)<br>✅ A/B testing engine<br>✅ Multi‑tenant SaaS mode (optional) |
| **v2.5**  | 2027‑05‑31 | **Enterprise‑grade** | ✅ Role‑based access control (RBAC)<br>✅ GDPR / CAN‑SPAM compliance audit logs<br>✅ High‑throughput async worker pool (via `vLLM`‑style task queue) |

\* **MVP‑Critical** items are the absolute minimum needed for a launchable, revenue‑validated product.

---

## Detailed Roadmap

### 📌 MVP – Foundational Engine (Due 2026‑07‑15)

| Item | Description | Owner | Status |
|------|-------------|-------|--------|
| Core class implementation | `MarketingAutomation` with internal quota tracker, `send_email`, `display_limit_usage`, `increase_limit` | Lead Engineer | ✅ Completed |
| Monthly quota persistence | Simple JSON/YAML file + in‑memory cache | Engineer | ✅ Completed |
| Email sending stub | Abstract `EmailProvider` interface; default no‑op implementation for tests | Engineer | ✅ Completed |
| Unit test coverage | ≥ 90 % branch coverage using `pytest` | QA Lead | ✅ Completed |
| CI pipeline | GitHub Actions: lint → test → build wheel | DevOps | ✅ Completed |
| Documentation | README usage guide, API reference, contribution guide | Tech Writer | ✅ Completed |
| Packaging & distribution | Publish to internal PyPI registry | Release Engineer | ✅ Completed |

**MVP Success Metric** – 5 paying pilot customers adopt the engine and stay within quota for 30 days.

---

### 🚀 v1.0 – Usability & Extensibility (Due 2026‑09‑30)

| Feature | Rationale | Implementation Notes |
|---------|-----------|----------------------|
| **CLI tool** (`dev-marketer-cli`) | Quick local usage, scripting | Click‑based commands: `send`, `status`, `increase` |
| **Web UI (Flask)** | Non‑technical users can manage limits | Minimal dashboard, auth via API key |
| **Email templates** | Reduce copy‑paste, support variables | Jinja2 rendering, stored in `templates/` |
| **Scheduler** | Batch send at specific dates/times | `APScheduler` integration, cron‑syntax |
| **Docker image** | One‑click deployment | Multi‑stage build, config via env vars |

---

### 📈 v1.5 – Integrations & Analytics (Due 2026‑11‑15)

| Integration | Details |
|-------------|---------|
| **SMTP providers** | Plug‑in architecture; adapters for SendGrid, Mailgun, Amazon SES. |
| **Dashboard** | React front‑end (create‑react‑app) served by Flask; charts via Chart.js (sent vs blocked, daily usage). |
| **Reporting** | CSV export endpoint; optional webhook for external BI tools. |
| **Rate‑limit alerts** | Email/SMS (Twilio) when 80 % of quota reached. |

---

### 🌱 v2.0 – Automation & Growth (Due 2027‑02‑28)

| Automation | Description |
|------------|-------------|
| **Trigger rules engine** | Event sources: webhook, CSV import, database query. Conditions → actions (`send_email`). |
| **A/B testing** | Split traffic by rule, collect open/click metrics (via tracking pixel). |
| **Multi‑tenant mode** | Namespaced quotas, per‑tenant API keys; optional SaaS deployment on Kubernetes. |
| **Async worker pool** | Use `celery` + Redis; scale to >10k emails/hour. |

---

### 🏢 v2.5 – Enterprise‑grade (Due 2027‑05‑31)

| Enterprise Feature | Implementation |
|--------------------|----------------|
| **RBAC** | `flask‑login` + `flask‑principal`; roles: admin, marketer, auditor. |
| **Compliance logs** | Immutable audit trail stored in append‑only log (e.g., SQLite WAL or external log service). |
| **GDPR / CAN‑SPAM tools** | Data‑subject request API, automatic unsubscribe handling. |
| **High‑throughput engine** | Replace synchronous send with `vLLM`‑style request queue; auto‑scale workers. |
| **SLA monitoring** | Prometheus metrics + Grafana dashboards. |

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Email deliverability issues | High (customer churn) | Start with well‑known SMTP providers; expose detailed bounce logs. |
| Quota enforcement bugs | Medium | Extensive unit + integration tests; property‑based testing for edge cases. |
| Scaling async workers | Medium | Prototype with Celery + Redis early (v1.5) to validate architecture. |
| Compliance liability | High | Build audit logs and unsubscribe handling from v2.0 onward; legal review before v2.5. |

---

## Success Metrics (Post‑Launch)

| Metric | Target (6 mo) |
|--------|---------------|
| Paying customers | ≥ 20 |
| Monthly active users (MAU) | ≥ 150 |
| Email volume processed | ≥ 500 k |
| Churn rate | ≤ 5 % |
| Net Promoter Score (NPS) | ≥ 45 |

---

## How to Contribute

1. Fork the `dev-marketer` repo.  
2. Create a feature branch named `feat/<short‑name>`.  
3. Follow the **contribution guide** in `CONTRIBUTING.md`.  
4. Submit a PR; CI will run lint, tests, and security scans.  
5. Tag the appropriate milestone (`MVP`, `v1.0`, etc.) in the PR.

---

*Prepared by the Senior Product/Engineering Lead – Axentx*
