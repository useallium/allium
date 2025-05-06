from flask import Blueprint, jsonify, request
from database.internships import Internships
from datetime import datetime

api = Blueprint('internships_api', __name__, url_prefix='/api')

@api.route('/internships/add', methods=["POST"])
def add_internship():
    db = Internships()
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['company_id', 'recruiter_id', 'title', 'description',
                           'location', 'is_remote', 'department', 'start_date',
                           'end_date', 'is_paid', 'salary', 'is_filled']
        missing = [field for field in required_fields if data.get(field) is None]
        if missing:
            return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

        internship = {
            "company_id": int(data.get('company_id')),
            "recruiter_id": int(data.get('recruiter_id')),
            "title": data.get('title'),
            "description": data.get('description'),
            "location": data.get('location'),
            "is_remote": bool(data.get('is_remote')),
            "department": data.get('department'),
            "start_date": datetime.strptime(data.get('start_date'), "%Y-%m-%d").date(),
            "end_date": datetime.strptime(data.get('end_date'), "%Y-%m-%d").date(),
            "is_paid": bool(data.get('is_paid')),
            "salary": int(data.get('salary')),
            "is_filled": bool(data.get('is_filled')),
        }

    
        retrieve_id = db.add_internship(internship["company_id"],internship["recruiter_id"],internship["title"],internship["description"],internship["location"],internship["is_remote"],internship["department"],internship["start_date"],internship["end_date"],internship["is_paid"],internship["salary"],internship["is_filled"],)
        if retrieve_id is not None:
            return jsonify({
                "message": "success",
                "internship_id": retrieve_id,
                "internship_info": internship
            }), 201
        else:
            return jsonify({"error": "Failed to insert internship into database"}), 500

    except ValueError as ve:
        return jsonify({"error": f"Invalid data format: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500
    
@api.route('/internships', methods=['GET'])
def get_internships():
    db = Internships()
    
    try:
        internships = db.get_all_internships()
        return jsonify(internships)
    
    except Exception as e:
        return jsonify({"error":f"Server error: {str(e)}"}),500


@api.route('/internships/remove', methods=["POST"])
def remove_internship():
    db = Internships()

    try:
        data = request.get_json()
        internship_id = int(data["internship_id"])

        is_removed = db.remove_internship(internship_id)
        if is_removed:
            return jsonify({"status":"success", "message":"successfully removed internship with id: {}".format(internship_id)}), 201
        else:
            return jsonify({"status":"failed", "message":"could not remove internship with id: {}".format(internship_id)}), 400

    except Exception as e:
        return jsonify({"error":f"Server error: {str(e)}"}),500



    