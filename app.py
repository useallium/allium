from flask import Flask, request, jsonify
from routes import init_routes
from dotenv import load_dotenv
import os

load_dotenv()
AUTH_TOKEN = os.getenv('AUTHTOKEN')


def create_app():
    app = Flask(__name__)


    app.secret_key = AUTH_TOKEN


    init_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
