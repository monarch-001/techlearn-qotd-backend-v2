from flask import Blueprint, jsonify
from data.store import submissions

leaderboard_bp = Blueprint("leaderboard", __name__)

@leaderboard_bp.route("/leaderboard", methods=["GET"])
def leaderboard():
    user_stats = {}

    for s in submissions:
        uid = s["userId"]

        if uid not in user_stats:
            user_stats[uid] = {
                "userId": uid,
                "correct": 0,
                "firstCorrectTime": None
            }

        if s["status"] == "correct":
            user_stats[uid]["correct"] += 1
            if not user_stats[uid]["firstCorrectTime"]:
                user_stats[uid]["firstCorrectTime"] = s["submittedAt"]

    leaderboard = sorted(
        user_stats.values(),
        key=lambda x: (-x["correct"], x["firstCorrectTime"] or "")
    )

    return jsonify(leaderboard), 200
