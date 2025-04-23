from flask import Blueprint, jsonify, request
from db import get_connection

api = Blueprint('companies_api',__name__, url_prefix='/api')

@api.route('/companies', methods=['GET'])
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM companies")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)