from flask import Blueprint, jsonify, request
from db import get_connection
from werkzeug.security import generate_password_hash

api = Blueprint('api', __name__, url_prefix='/api')

# Get all users
@api.route('/users', methods=['GET'])
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)

@api.route('/users/create', methods=['POST'])
def create_user():
    # Get data from the request
    data = request.get_json()

    # Extract the necessary fields
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    user_type = data.get('user_type')

    # Validate the required fields
    if not email or not password or not first_name or not last_name or not user_type:
        return jsonify({'message': 'Missing required fields'}), 400

    # Hash the password
    password_hash = generate_password_hash(password)

    # Establish database connection
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Insert the user into the database
        cursor.execute("""
            INSERT INTO users (email, password_hash, first_name, last_name, user_type)
            VALUES (%s, %s, %s, %s, %s)
        """, (email, password_hash, first_name, last_name, user_type))

        # Commit changes to the database
        conn.commit()

        # Get the newly inserted user ID
        user_id = cursor.lastrowid

        # Return success response with the newly created user's details
        return jsonify({
            'message': 'User created successfully',
            'user_id': user_id,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'user_type': user_type
        }), 201

    except Exception as e:
        # Handle any database error
        conn.rollback()
        return jsonify({'message': f'Error creating user: {str(e)}'}), 500

    finally:
        # Clean up
        cursor.close()
        conn.close()

# Get a specific user by ID
@api.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404
