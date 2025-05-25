from flask import Flask, request, jsonify
from flask_login import LoginManager
from routes import init_routes
from dotenv import load_dotenv
import os
from database.users import Users
from routes.web.auth import User

load_dotenv()
AUTH_TOKEN = os.getenv('AUTHTOKEN')


login_manager = LoginManager()
@login_manager.user_loader
def load_users(user_id):
    users = Users()
    user_data = users.get_user_by_id(user_id)
    users.close()
    if user_data:
        return User(
            id=user_data['user_id'],
            email=user_data['email'],
            password_hash=user_data['password_hash'],
            user_type=user_data['user_type'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
    
    return None


def create_app():
    app = Flask(__name__)
    app.secret_key = AUTH_TOKEN

       # 💡 You missed this line:
    login_manager.init_app(app)

    # Optional: redirect unauthenticated users
    login_manager.login_view = 'auth.login'


    
    init_routes(app)
    
    print("\n🚨 Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint:40} -> {rule.rule}")


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
