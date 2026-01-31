from flask import Blueprint, request, jsonify
from backend.services.evaluator import evaluate_code, CodeExecutionError
from backend.data.store import qotd, submissions
from datetime import datetime

submission_bp = Blueprint("submission", __name__)

@submission_bp.route("/daily-challenge/submissions", methods=["POST"])
def submit_code():
    data = request.get_json()

    required_fields = ["userId", "language", "code"]
    if not data or not all(f in data for f in required_fields):
        return jsonify({"error": "Invalid submission payload"}), 400

    if data["language"] != "python":
        return jsonify({"error": "Only Python is supported"}), 400

    try:
        result = evaluate_code(
            code=data["code"],
            function_name="two_sum",
            test_cases=qotd["test_cases"]
        )
    except CodeExecutionError as e:
        return jsonify({"status": "error", "message": str(e)}), 400

    # ✅ STORE SUBMISSION
    submission_record = {
        "userId": data["userId"],
        "questionId": qotd["id"],
        "status": result["status"],
        "passed": result["passed"],
        "total": result["total"],
        "submittedAt": datetime.utcnow().isoformat() + "Z"
    }

    submissions.append(submission_record)

    return jsonify(result), 200
