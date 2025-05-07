from flask import Blueprint, jsonify, request, session, redirect, url_for, flash
#from database import Database
from werkzeug.security import generate_password_hash, check_password_hash
from database.users import Users

api = Blueprint('users_api', __name__, url_prefix='/api')


@api.route('users', methods=['POST'])
def get_all_users():
    try:
        data = request.get_json()
        print(data)
        return jsonify(data)
    
    except Exception as e:
        pass



# Get all users
# @api.route('/users', methods=['GET'])
# def get_users():
#     # conn = connect()
#     cursor = conn.cursor(dictionary=True)

#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()

#     cursor.close()
#     conn.close()

#     return jsonify(users)

# @api.route('/users/create', methods=['POST'])
# def create_user():
#     # Get data from the request

#     # Extract the necessary fields
#     email = request.form.get('email')
#     password = request.form.get('password')
#     first_name = request.form.get('first_name')
#     last_name = request.form.get('last_name')
#     user_type = request.form.get('user_type')

#     # Validate the required fields
#     if not email or not password or not first_name or not last_name or not user_type:
#         return jsonify({'message': 'Missing required fields'}), 400
#     # Hash the password
#      password_hash = generate_password_hash(password)

#     # Establish database connection
#     conn = connect()
#     cursor = conn.cursor()

#     try:
#         # Insert the user into the database
#         cursor.execute("""
#             INSERT INTO users (email, password_hash, first_name, last_name, user_type)
#             VALUES (%s, %s, %s, %s, %s)
#         """, (email, password_hash, first_name, last_name, user_type))

#         # Commit changes to the database
#         conn.commit()

#         # Get the newly inserted user ID
#         user_id = cursor.lastrowid

#         # Return success response with the newly created user's details
#         return jsonify({
#             'message': 'User created successfully',
#             'user_id': user_id,
#             'email': email,
#             'first_name': first_name,
#             'last_name': last_name,
#             'user_type': user_type
#         }), 201

#     except Exception as e:
#         # Handle any database error
#         conn.rollback()
#         return jsonify({'message': f'Error creating user: {str(e)}'}), 500

#     finally:
#         # Clean up
#         cursor.close()
#         conn.close()


# # Get a specific user by ID
# @api.route('/users/<int:user_id>', methods=['GET'])
# def get_user_by_id(user_id):
#     conn = connect()
#     cursor = conn.cursor(dictionary=True)

#     cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
#     user = cursor.fetchone()

#     cursor.close()
#     conn.close()

#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({'error': 'User not found'}), 404

# @api.route('/login', methods=["POST"])
# def login():
#     email = request.form.get('email')
#     password = request.form.get('password')

#     print(email, password)

#     conn = connect()
#     cursor = conn.cursor(dictionary=True)

#     try:
#         cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#         user = cursor.fetchone()

#         if not user or not check_password_hash(user['password_hash'], password):
#             flash('Invalid credentials')
#             return redirect(url_for('login.index'))

#         session['id'] = user['user_id']
#         session['email'] = user['email']
#         return redirect(url_for('dashboard.index'))  # Redirect to dashboard

#     except Exception as e:
#         # If connection is still valid, do a rollback
#         if conn.is_connected():
#             try:
#                 conn.rollback()
#             except:
#                 pass  # You might want to log that rollback failed.

#         return jsonify({'message': f'Error logging in user: {str(e)}'}), 401

#     finally:
#         # Ensure the cursor and connection are closed properly
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()
