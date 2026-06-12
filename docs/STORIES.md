# 📖 Stories.md – dev‑marketer  

## Overview  
The **dev‑marketer** repository provides a lightweight Marketing Automation Engine (MAE) that enforces a monthly email‑send limit. The following backlog defines the product roadmap from the Minimum Viable Product (MVP) through a first‑generation feature set. Stories are grouped into Epics, ordered by delivery priority, and each includes clear Acceptance Criteria (AC) to enable test‑driven development.

---  

## 🗂️ Epics & Story Map  

| Epic | Description | MVP Order |
|------|-------------|-----------|
| **Epic 1 – Core Email Sending & Limit Management** | Fundamental engine: send emails, track usage, enforce monthly caps, and allow limit adjustments. | 1 |
| **Epic 2 – User Management & Authentication** | Secure multi‑tenant access; each user gets an isolated quota. | 2 |
| **Epic 3 – Email Templates & Personalisation** | Re‑usable templates with placeholder substitution. | 3 |
| **Epic 4 – Scheduling & Campaign Management** | Queue‑based sending, recurring campaigns, and pause/resume controls. | 4 |
| **Epic 5 – Reporting & Analytics** | Visibility into usage, delivery stats, and limit forecasts. | 5 |
| **Epic 6 – Admin Controls & Billing Integration** | Admin dashboard, quota overrides, and optional paid‑plan upgrades. | 6 |

---  

## 🚀 Epic 1 – Core Email Sending & Limit Management  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **1.1** | **As a developer, I want to instantiate a `MarketingAutomation` object with a configurable monthly email limit, so that the engine knows how many emails I may send.** | - Constructor accepts `monthly_limit` (int).<br>- Default limit = 1 000 if omitted.<br>- Internal state stores `sent_count` = 0.<br>- `monthly_limit` and `sent_count` are persisted in a JSON file (`mae_state.json`) on each change. |
| **1.2** | **As a developer, I want a `send_email(to, subject, body)` method that respects the monthly limit, so that no more than the allowed emails are dispatched.** | - Method returns `True` on successful send, `False` if limit reached.<br>- When limit is reached, method raises a `LimitReachedError` with a clear message.<br>- Successful send increments `sent_count` and persists state.<br>- Uses Python’s `smtplib` with configurable SMTP settings (host, port, credentials). |
| **1.3** | **As a developer, I want a `display_limit_usage()` method that shows current usage, so that I can monitor remaining quota.** | - Returns a string: `"Sent X / Y emails this month (Z % used)"`.<br>- Handles edge cases (e.g., limit = 0) gracefully.<br>- Output is also logged at INFO level. |
| **1.4** | **As a developer, I want an `increase_limit(delta)` method to raise the monthly quota, so that I can accommodate growth without redeploying.** | - `delta` must be a positive integer; otherwise raises `ValueError`.<br>- New limit = old limit + delta; persisted immediately.<br>- Returns the new limit. |
| **1.5** | **As a system, I want the monthly quota to reset automatically on the first day of each month at 00:00 UTC, so that users start each month fresh.** | - A background job (e.g., `APScheduler` or cron) runs daily, checks if the month changed.<br>- On month rollover, `sent_count` resets to 0 while preserving `monthly_limit`.<br>- Reset event is logged with timestamp. |

---  

## 🔐 Epic 2 – User Management & Authentication  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **2.1** | **As a marketer, I want to create an account with email + password, so that I can access my own quota.** | - `POST /api/users/register` accepts `email`, `password` (hashed with bcrypt).<br>- Returns 201 with user ID and JWT token.<br>- Duplicate email returns 409. |
| **2.2** | **As a marketer, I want to log in and receive a JWT, so that subsequent API calls are authenticated.** | - `POST /api/users/login` validates credentials.<br>- Returns 200 with JWT (exp = 24 h).<br>- Invalid credentials return 401. |
| **2.3** | **As a developer, I want each user to have an isolated `MarketingAutomation` instance with its own limit, so that usage does not bleed across accounts.** | - On registration, a default `monthly_limit` (1 000) is created and stored in a `users` table.<br>- All email‑send actions are scoped to the authenticated user ID. |
| **2.4** | **As a marketer, I want to reset my password via a secure token, so that I can regain access if I forget it.** | - `POST /api/users/forgot-password` sends a time‑limited (15 min) token to the registered email.<br>- `POST /api/users/reset-password` with token and new password updates the hash
