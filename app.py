from flask import Flask, request, jsonify
from routes import init_routes
from dotenv import load_dotenv
import os

load_dotenv()
AUTH_TOKEN = os.getenv('AUTHTOKEN')


def create_app():
    app = Flask(__name__)

    @app.before_request
    def check_auth_token():
        if not request.path.startswith('/api/'):
            return

        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {AUTH_TOKEN}":
            return jsonify({"error": "Unauthorized"}), 401



    init_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
