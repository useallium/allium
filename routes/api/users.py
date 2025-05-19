from flask import Blueprint, jsonify, request, session, redirect, url_for, flash
#from database import Database
from werkzeug.security import generate_password_hash, check_password_hash
from database.users import Users

api = Blueprint('users_api', __name__, url_prefix='/api')


@api.route('users', methods=['GET'])
def get_all_users():
    db = Users()
    try:
        users = db.get_all_users()
        return jsonify(users), 201
    
    except Exception as e:
        return jsonify({"message":"failure"}),500

@api.route('/users/create', methods=['POST'])
def create_user():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    user_type = request.form.get('user_type')

    if not email or not password or not first_name or not last_name or not user_type:
        return jsonify({'message': 'Missing required fields'}), 400
    
    password_hash = generate_password_hash(password)

    try:
        # Insert the user into the database
        db = Users()

        # Commit changes to the database
        retrieve_id = db.add_user(email,first_name,last_name,password_hash,user_type)

        # Get the newly inserted user ID

        # Return success response with the newly created user's details
        return jsonify({
            'message': 'User created successfully',
            'user_id': retrieve_id,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'user_type': user_type
        }), 201

    except Exception as e:
        # Handle any database error
        
        return jsonify({'message': f'Error creating user: {str(e)}'}), 500
