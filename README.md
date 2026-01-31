# TechLearn – Question of the Day (QOTD) Backend v2

A production-ready REST API that powers a **Question of the Day (QOTD)** coding platform.  
Users can fetch daily coding challenges, submit solutions, view stats, and compete on a leaderboard.

🔗 **Live API Base URL**  
https://techlearn-qotd-backend-v2.onrender.com

---

## 🚀 Features

- 📅 Daily coding challenge API
- 🧠 Code submission endpoint (user-provided code)
- 📊 Global statistics (submissions, correctness, usage)
- 🏆 Dynamic leaderboard
- 👤 User management
- 🩺 Health / meta endpoint
- 🔁 API versioning (`/api/v1`)
- ☁️ Deployed on **Render**

---

## 🏗️ Project Structure

techlearn-qotd-backend-v2/
│
├── app.py # Flask app entry point
├── routes/ # API route blueprints
│ ├── qotd.py
│ ├── submission.py
│ ├── stats.py
│ ├── leaderboard.py
│ ├── meta.py
│ └── users.py
│
├── services/ # Business logic layer
├── data/ # Data / mock storage
│
├── requirements.txt # Python dependencies
├── runtime.txt # Python runtime version (Render)
├── README.md # Project documentation
├── LICENSE # MIT License
└── init.py


---

## 🔗 API Overview

All endpoints are prefixed with:

/api/v1


### 📌 Available Endpoints

| Feature | Method | Endpoint |
|------|------|------|
| API Info / Health | GET | `/api/v1/meta` |
| Daily Challenge | GET | `/api/v1/daily-challenge` |
| Submit Solution | POST | `/api/v1/daily-challenge/submissions` |
| Stats | GET | `/api/v1/stats` |
| Leaderboard | GET | `/api/v1/leaderboard` |
| Users | GET / POST | `/api/v1/users` |

---

## 🧪 Example Requests

### 🔹 Get Daily Challenge
```http
GET /api/v1/daily-challenge
🔹 Submit a Solution
POST /api/v1/daily-challenge/submissions
Content-Type: application/json
{
  "user_id": "alice",
  "code": "def solve(): return 42"
}
🔹 View Leaderboard
GET /api/v1/leaderboard
🛠️ Local Development
1️⃣ Clone the repository
git clone https://github.com/monarch-001/techlearn-qotd-backend-v2.git
cd techlearn-qotd-backend-v2
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the server
python app.py
Server runs at:

http://localhost:5000
☁️ Deployment
Platform: Render

Runtime: Python (defined in runtime.txt)

Entry point: app.py

Auto-deploys on push to main

🧠 Design Notes
Uses Flask Blueprints for modular routing

Clear separation of routes and services

Versioned API to support future changes

Designed to be frontend-agnostic (web / mobile)

📌 Future Enhancements
Persistent database (PostgreSQL)

Secure code execution & test-case validation

Per-user submission history

Time & space complexity analysis

Swagger / OpenAPI documentation

Authentication & rate limiting
