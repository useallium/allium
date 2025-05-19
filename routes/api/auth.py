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
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    user_type = request.form.get('user_type')
    if not email or not password or not first_name or not last_name or not user_type:
        return jsonify({"message":"Missing credentials"}), 400

    try:
        db = Users()

        hashed_password = generate_password_hash(password)

        users = db.get_all_users()
        for user in users:
            if user['email'] == email:
                return jsonify({"message":"Email already registered"}), 400
            else:
                added_user = db.add_user(email, first_name, last_name, hashed_password, user_type)
                if added_user != None:
                    session['user_id'] = added_user['user_id']
                    session['user_type'] = added_user['user_type']

                    if added_user['user_type'] == 'student':
                        return redirect(url_for('URL_FOR_STUDENT_SIGNUP.index'))
                    elif added_user['user_type'] == 'recruiter':
                        return redirect(url_for('URL_FOR_RECRUITER_SIGNUP.index'))

    except Exception as e:
        return jsonify({"message":f'Error during signup: {str(e)}'}),500



