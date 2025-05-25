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
