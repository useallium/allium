from flask import Blueprint, jsonify, request
from database.recruiters import Recruiters

api = Blueprint('recruiters_api', __name__, url_prefix='/api')

@api.route('/recruiters', methods=['GET'])
def get_all_recruiters():
    db = Recruiters()
    try:
        recruiters = db.get_all_recruiters()
        return jsonify(recruiters), 200
    except Exception as e:
        return jsonify({'message': f'Error fetching recruiters: {str(e)}'}), 500

@api.route('/recruiters/get_by_id', methods=['POST'])
def get_recruiter_by_id():
    db = Recruiters()
    try:
        data = request.get_json()
        recruiter_id = data.get('recruiter_id')

        if recruiter_id is None:
            return jsonify({'message': 'Missing recruiter_id'}), 400

        recruiter = db.get_recruiter_by_id(recruiter_id)
        if recruiter:
            return jsonify(recruiter), 200
        else:
            return jsonify({'message': f'No recruiter found with ID: {recruiter_id}'}), 404

    except Exception as e:
        return jsonify({'message': f'Error retrieving recruiter: {str(e)}'}), 500

@api.route('/recruiters/update', methods=['POST'])
def update_recruiter():
    db = Recruiters()
    try:
        data = request.get_json()

        recruiter_id = data.get('recruiter_id')
        company_id = data.get('company_id')
        job_title = data.get('job_title')
        phone_number = data.get('phone_number')

        if None in [recruiter_id, company_id, job_title, phone_number]:
            return jsonify({'message': 'Missing one or more required fields'}), 400

        rows_updated = db.update_recruiter(recruiter_id, company_id, job_title, phone_number)

        if rows_updated:
            return jsonify({'message': f'Recruiter {recruiter_id} updated successfully'}), 200
        else:
            return jsonify({'message': f'No recruiter found with ID: {recruiter_id}'}), 404

    except Exception as e:
        return jsonify({'message': f'Error updating recruiter: {str(e)}'}), 500
