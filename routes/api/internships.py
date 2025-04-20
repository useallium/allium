from flask import Blueprint, jsonify, request
from db import get_connection

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/internships', methods=['GET'])
def get_internships():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM internships")
    internships = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(internships)