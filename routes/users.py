from flask import Blueprint, jsonify
from data.store import submissions

users_bp = Blueprint("users", __name__)

@users_bp.route("/users/<user_id>/submissions", methods=["GET"])
def user_submissions(user_id):
    user_history = [
        s for s in submissions if s["userId"] == user_id
    ]

    return jsonify({
        "userId": user_id,
        "totalSubmissions": len(user_history),
        "submissions": user_history
    }), 200

