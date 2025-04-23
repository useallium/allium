from flask import Flask
from routes import init_routes
import secrets


def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(32)
    app.config['SESSION_TYPE'] = 'filesystem'  # You can use 'redis', 'memcached', etc. too.
    app.config['SESSION_PERMANENT'] = False    # Session should not be permanent by default
    app.config.from_pyfile('config.py')

    init_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
