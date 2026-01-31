# TechLearn – Question of the Day (QOTD) Backend v2

Production-ready REST API powering TechLearn's "Question of the Day" coding platform.  
Users fetch daily coding challenges, submit solutions, view stats, and compete on a leaderboard.

Live API: [https://techlearn-qotd-backend-v2.onrender.com](https://techlearn-qotd-backend-v2.onrender.com)

---

## Table of contents

- [Quick Overview](#quick-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture & Data Models](#architecture--data-models)
- [API Reference](#api-reference)
- [Examples (curl & Python)](#examples-curl--python)
- [Local Development](#local-development)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [Testing](#testing)
- [Security & Limitations](#security--limitations)
- [🔧 What I Would Improve With More Time](#-what-i-would-improve-with-more-time)
- [Interview Talking Points](#interview-talking-points)
- [Contributing](#contributing)
- [License & Contact](#license--contact)

---

## Quick overview

TechLearn QOTD Backend v2 exposes a simple, versioned REST API (prefix: `/api/v1`) that delivers a daily coding challenge, accepts user-submitted code, computes basic correctness/score, and aggregates stats and leaderboard data. The service is designed to be frontend-agnostic and easy to integrate with web or mobile clients.

---

## Features

- Daily challenge retrieval
- Code submission endpoint (user-provided code)
- Global stats and per-user usage
- Leaderboard aggregation
- User management (basic)
- Health / meta endpoint
- Versioned API: `/api/v1`
- Deployed on Render

---

## Tech stack

- Python 3.x
- Flask (Blueprints)
- Simple file/mock storage (designed for easy replacement with PostgreSQL)
- Deployed on Render

---

## Architecture & data models

High-level components:
- app.py — Flask application entry point
- routes/ — API route blueprints (qotd.py, submission.py, stats.py, leaderboard.py, meta.py, users.py)
- services/ — Business logic and domain services
- data/ — Mock/persisted data storage (file or in-memory for v2)

Core data models (conceptual):
- Challenge
  - id, date, title, description, difficulty, sample_input, sample_output, tests
- Submission
  - id, user_id, challenge_id, code, language, timestamp, status (passed/failed), score
- User
  - id, name, email (optional), submissions_count, score
- Leaderboard
  - Derived: ordered list of users by score / streaks / accuracy

Notes: This repo uses a clear separation between routes and services so the service layer can be swapped to use a real DB or secure execution sandbox later.

---

## API reference

Base URL: [https://techlearn-qotd-backend-v2.onrender.com](https://techlearn-qotd-backend-v2.onrender.com)  
Prefix: `/api/v1`

All responses use JSON and standard HTTP status codes.

### 1) Health / Meta
- Method: GET
- Path: `/api/v1/meta`
- Description: Health check and basic API metadata.
- Response:
```json
{
  "service": "techlearn-qotd-backend-v2",
  "version": "v2",
  "status": "ok"
}
```

### 2) Get Daily Challenge
- Method: GET
- Path: `/api/v1/daily-challenge`
- Description: Returns the challenge of the day.
- Response (example):
```json
{
  "id": "2026-01-31",
  "title": "Sum of Two",
  "description": "Given two numbers, return their sum.",
  "difficulty": "easy",
  "sample_input": "2 3",
  "sample_output": "5"
}
```

### 3) Submit Solution
- Method: POST
- Path: `/api/v1/daily-challenge/submissions`
- Description: Submit user code for evaluation. (Note: current implementation accepts code and returns a basic pass/fail result; secure execution not implemented in this version.)
- Request (JSON):
```json
{
  "user_id": "alice",
  "code": "def solve(): return 42",
  "language": "python"
}
```
- Response (example):
```json
{
  "submission_id": "sub_12345",
  "user_id": "alice",
  "challenge_id": "2026-01-31",
  "status": "passed",
  "score": 100,
  "message": "All tests passed"
}
```

### 4) Stats
- Method: GET
- Path: `/api/v1/stats`
- Description: Aggregate statistics for challenges and submissions (global).
- Response (example):
```json
{
  "total_submissions": 312,
  "pass_rate": 0.48,
  "active_users": 75
}
```

### 5) Leaderboard
- Method: GET
- Path: `/api/v1/leaderboard`
- Description: Ordered list of top users.
- Response (example):
```json
[
  {"user_id":"bob","score":275,"rank":1},
  {"user_id":"alice","score":250,"rank":2}
]
```

### 6) Users
- Method: GET / POST
- Path: `/api/v1/users`
- Description: List users or create a user.
- Create request example:
```json
{
  "user_id": "alice",
  "name": "Alice"
}
```

---

## Examples (curl & Python)

curl - get daily challenge:
```bash
curl -s GET "https://techlearn-qotd-backend-v2.onrender.com/api/v1/daily-challenge"
```

curl - submit (example):
```bash
curl -s -X POST "https://techlearn-qotd-backend-v2.onrender.com/api/v1/daily-challenge/submissions" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"alice","code":"def solve(): return 42","language":"python"}'
```

Python (requests):
```python
import requests

BASE = "https://techlearn-qotd-backend-v2.onrender.com/api/v1"
r = requests.get(f"{BASE}/daily-challenge")
print(r.json())

payload = {"user_id":"alice","code":"def solve(): return 42","language":"python"}
r2 = requests.post(f"{BASE}/daily-challenge/submissions", json=payload)
print(r2.json())
```

---

## Local development

1. Clone
```bash
git clone https://github.com/monarch-001/techlearn-qotd-backend-v2.git
cd techlearn-qotd-backend-v2
```

2. Create venv and activate
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install
```bash
pip install -r requirements.txt
```

4. Set environment variables (see below) and run
```bash
python app.py
# Server default: http://localhost:5000
```

---

## Environment variables

Create a `.env` or export values in your shell. Typical variables that may be used or added:
- FLASK_ENV=development
- FLASK_APP=app.py
- DATABASE_URL=postgres://... (if migrating to Postgres)
- SECRET_KEY=your-secret-key
- EXECUTION_SANDBOX_URL=... (if external code-runner is used)

---

## Deployment

This project is configured for Render. The runtime is controlled by `runtime.txt` and the entry point is `app.py`. Auto-deploys on push to `main` (if configured on the Render service).

Live instance (public): [https://techlearn-qotd-backend-v2.onrender.com](https://techlearn-qotd-backend-v2.onrender.com)

---

## Testing

- Unit / integration tests: Add a `tests/` directory and run with pytest:
```bash
pip install pytest
pytest
```
- Current repository may not include tests; adding tests for services (business logic) and API endpoints is a recommended next step.

---

## Security & limitations

- Current v2 accepts raw code. Do NOT run on production without a secure code-execution sandbox (containerized, time-limited, resource-limited).
- No authentication in v2. Add JWT or OAuth for production and rate limiting to prevent abuse.
- Data storage is mock/file-based; move to PostgreSQL or another durable store before production.
- Validate and sanitize all inputs.

---

## 🔧 What I Would Improve With More Time

- Safer Code Execution  
  Run user-submitted code in an isolated environment so it can be executed safely without affecting the server.

- Support for Multiple Languages  
  Allow users to submit solutions in languages like Python, Java, and C++ instead of limiting to one language.

- Better Performance Measurement  
  Automatically measure execution time and memory usage instead of relying on user-provided complexity values.

- Database-Backed Storage  
  Move from in-memory storage to a real database so submissions, stats, and leaderboards persist across restarts.

- User Accounts & Authentication  
  Add login and authentication so users can track their own submissions and see personal progress.

- Dynamic Leaderboard  
  Update the leaderboard in real time as new submissions are made.

- Stronger Test Case Validation  
  Add hidden test cases to prevent hardcoded solutions and ensure correct logic.

- Logging & Monitoring  
  Improve error handling and logging to make the system easier to debug and maintain.

- API Documentation  
  Add clear API documentation (OpenAPI/Swagger) so developers can easily understand and use the backend.

- Scalability & Automation  
  Add automated tests and CI/CD pipelines to make the system more reliable and easier to scale.

---

## License & contact

MIT License — see LICENSE file.
