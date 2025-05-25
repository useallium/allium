from flask import Blueprint, render_template
from flask_login import login_required, current_user
from database.internships import Internships
from database.applications import Applications

recruiter = Blueprint('recruiter', __name__, url_prefix='/recruiter')

@recruiter.route('/internships')
@login_required
def internships():
    if current_user.user_type != 'recruiter':
        return "Unauthorized", 403

    internships_db = Internships()
    applications_db = Applications()

    internships_list = internships_db.get_internships_by_recruiter(current_user.id)
    data = []

    for internship in internships_list:
        applications = applications_db.get_applications_by_internship(internship['internship_id'])
        data.append({
            'internship': internship,
            'applications': applications,
            'application_count': len(applications)
        })

    internships_db.close()
    applications_db.close()

    return render_template('recruiter_internships.html', data=data)

@recruiter.route('internships/add')
def add_internship():
    company_id = 4
    recruiter_id = 63
    return render_template('add_internships.html',recruiter_id=recruiter_id, company_id=company_id)
