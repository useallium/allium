from flask import Blueprint, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash
from database.users import Users
import traceback

api = Blueprint('login_api', __name__, url_prefix='/api')

@api.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message":"Missing email or password"}), 400
    
    try:
        db = Users()

        user = db.get_user_by_email(email)

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['user_id']
            session['user_type'] = user['user_type']

            return redirect(url_for('dashboard.index'))
        else:
            return redirect(url_for('login.index'))
        
        

    except Exception as e:
        traceback.print_exc()
        return jsonify({'message': f'Error during login: {str(e)}'}), 500


@api.route('/logout')
def logout():
    session.clear()  # Clear the session to log the user out
    return redirect(url_for('login.index'))  # Redirect to login page