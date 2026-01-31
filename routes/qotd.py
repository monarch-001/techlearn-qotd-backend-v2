from flask import Blueprint, jsonify
from data.store import qotd

qotd_bp = Blueprint("qotd", __name__)

@qotd_bp.route("/daily-challenge", methods=["GET"])
def get_daily_challenge():
    first_case = qotd["test_cases"][0]

    return jsonify({
        "title": qotd["title"],
        "difficulty": qotd["difficulty"],
        "problem_statement": qotd["problem_statement"],
        "function_signature": qotd["function_signature"],
        "sample_input": first_case["input"],
        "sample_output": first_case["output"]
    }), 200


@qotd_bp.route("/daily-challenge/hints", methods=["GET"])
def get_hints():
    return jsonify({"hints": qotd["hints"]}), 200
