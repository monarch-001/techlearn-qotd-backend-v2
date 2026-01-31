from flask import Blueprint, jsonify
from data.store import submissions

stats_bp = Blueprint("stats", __name__)

@stats_bp.route("/daily-challenge/stats", methods=["GET"])
def get_stats():
    total = len(submissions)
    correct = sum(1 for s in submissions if s.get("status") == "correct")

    success_rate = (
        f"{(correct / total) * 100:.2f}%" if total > 0 else "0%"
    )

    return jsonify({
        "totalAttempts": total,
        "correctAttempts": correct,
        "successRate": success_rate
    }), 200
