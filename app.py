from flask import Flask
from routes.qotd import qotd_bp
from routes.submission import submission_bp
from routes.stats import stats_bp
from routes.leaderboard import leaderboard_bp
from routes.meta import meta_bp
from routes.users import users_bp


API_PREFIX = "/api/v1"

def create_app():
    app = Flask(__name__)
    

    app.register_blueprint(qotd_bp, url_prefix=API_PREFIX)
    app.register_blueprint(submission_bp, url_prefix=API_PREFIX)
    app.register_blueprint(stats_bp, url_prefix=API_PREFIX)
    app.register_blueprint(leaderboard_bp, url_prefix=API_PREFIX)
    app.register_blueprint(meta_bp, url_prefix=API_PREFIX)
    app.register_blueprint(users_bp, url_prefix=API_PREFIX)



    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
