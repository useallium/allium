from flask import Blueprint, jsonify, request,url_for,redirect
from database.applications import Applications
from database.base import Database

#test

api = Blueprint('applications_api', __name__, url_prefix='/api')

@api.route('/applications', methods=["GET"])
def get_applications():
    
    try:
        db = Applications()
        applications = db.get_applications()
        return jsonify(applications)
    
    except Exception as e:
        return jsonify({"status":"fail"}), 500
    
@api.route('/applications/application/<int:application_id>', methods=['GET'])
def get_application_by_application_id(application_id):
    try:
        db = Applications()
        application = db.get_application_by_application_id(application_id)
        return jsonify({
            'status':'success',
            'data': application
            })
    except Exception as e:
        return jsonify({
                'status': 'failure',
                'message': f'Could not find application with id {application_id}'
            }), 400



@api.route('/applications/status', methods=['POST'])
def update_application():
    db = Applications()
    application_id = None

    try:
        data = request.get_json()

        application_id = data['application_id']
        status = data['status']

        if db.update_application_status(status, application_id):
            return jsonify({
                'status': 'success',
                'message': f'Changed application with id {application_id} to status {status}'
            }), 200
        else:
            return jsonify({
                'status': 'failure',
                'message': f'Could not update application with id {application_id}'
            }), 400

    except Exception as e:
        return jsonify({
            'status': 'failed',
            'message': f'Failed to change status of application',
            'error': str(e),
            'application_id': application_id
        }), 400
    
@api.route('/update_status', methods=['POST'])
def update_application_status():
    application_id = request.form.get('application_id')
    new_status = request.form.get('status')

    db = Applications()  # Create instance of your DB class
    success = db.update_application_status(new_status,application_id)

    if success:
        print("Status updated successfully.", "success")
    else:
        print("Failed to update status.", "danger")

    # Optionally, close connection here if you want after update
    

    return redirect(url_for('internship.manage_internships'))

@api.route('applications/num_applicants/<int:internship_id>', methods=['GET'])
def get_num_applicants(internship_id):
    db = Database()
    db.cursor.callproc('GetTotalApplications', [internship_id])

    count = 0 
    for result in db.cursor.stored_results():
        row = result.fetchone()
        if row:
            count = row['total_applications']

    return jsonify({'total_applications': count})