from flask import Blueprint, jsonify
from datetime import datetime

meta_bp = Blueprint("meta", __name__)

@meta_bp.route("/meta", methods=["GET"])
def meta():
    return jsonify({
        "service": "TechLearn QOTD API",
        "version": "v1",
        "status": "healthy",
        "server_time": datetime.utcnow().isoformat() + "Z"
    }), 200
