from flask import Blueprint, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from database.users import Users

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/auth/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message":"Missing email or password"}), 400

    try:
        db = Users()

        user = db.get_user_by_email(email)

        if user and  check_password_hash(user['password_hash'], password):
            session['user_id'] = user['user_id']
            session['user_type'] = user['user_type']

            return redirect(url_for('dashboard.index'))
        else:
            return redirect(url_for('login.index'))

    except Exception as e:
        return jsonify({"message":f'Error during login'})

@api.route('/auth/logout')
def logout():
    session.clear()
    return redirect(url_for('login.index'))

@api.route('/auth/signup', methods=['POST'])
def signup():
    # Extract form data
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    user_type = request.form.get('user_type')

    # Validate input
    if not email or not password or not first_name or not last_name or not user_type:
        return jsonify({"message": "Missing credentials"}), 400

    try:
        db = Users()

        # Check if email already exists
        if db.get_user_by_email(email):
            return jsonify({"message": "Email already registered"}), 400

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Add user to database
        user_info = db.add_user(email, first_name, last_name, hashed_password, user_type)

        if user_info is not None:
            # Store session data
            session['user_id'] = user_info['user_id']
            session['user_type'] = user_info['user_type']

            # Redirect based on user type
            if user_info['user_type'] == 'student':
                return redirect(url_for('auth.index'))
            elif user_info['user_type'] == 'recruiter':
                return redirect(url_for('auth.index'))

        return jsonify({"message": "User could not be created"}), 500


    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"message": f"Error during signup: {str(e)}"}), 500



