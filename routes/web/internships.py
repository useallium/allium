from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from database.internships import Internships
from database.applications import Applications
from database.students import Students
from database.users import Users
from database.recruiters import Recruiters
from database.base import Database


internships = Blueprint('internship', __name__, url_prefix='/internships')

@internships.route('/')
@login_required
def show_internships():
    db = Internships()
    internships_list = db.get_all_internships()

    for internship in internships_list:
        company = db.get_company_by_internship(internship['internship_id'])
        if company and 'company_name' in company:
            internship['company_name'] = company['company_name']
        else:
            internship['company_name'] = 'Unknown'

    print("internships:", internships_list)
    return render_template('internships_list.html', internships=internships_list)

@internships.route('/manage', methods=['GET'])
@login_required
def manage_internships():
    if current_user.user_type != 'recruiter':
        flash("Access denied.", "danger")
        return redirect(url_for('dashboard.index'))

    db_internships = Internships()
    db_applications = Applications()
    db_users = Users()
    db_students = Students()  # Behövs

    try:
        internships = db_internships.get_internships_by_recruiter(current_user.id)

        for internship in internships:
            applicants = db_applications.get_applications_by_internship(internship['internship_id'])

            for applicant in applicants:
                user_info = db_users.get_user_by_id(applicant['applicant_id'])
                student_info = db_students.get_student_info_by_user_id(applicant['applicant_id'])

                if user_info:
                    applicant['first_name'] = user_info.get('first_name', 'Unknown')
                    applicant['last_name'] = user_info.get('last_name', '')
                    applicant['email'] = user_info.get('email', 'Unknown')

                if student_info:
                    applicant['resume'] = student_info.get('resume', None)
                else:
                    applicant['resume'] = None

            internship['applicants'] = applicants

        return render_template("manage_internships.html", internships=internships)

    except Exception as e:
        flash(f"Something went wrong: {e}", "danger")
        return redirect(url_for('dashboard.index'))


@internships.route('/apply/<int:internship_id>', methods=['POST'])
@login_required
def apply_to_internship(internship_id):
    db = Applications()
    sdb = Students()
    try:
        
        student_info = sdb.get_student_info_by_user_id(current_user.id)
        resume = student_info['resume']

        print(resume)
        
        success = db.apply(current_user.id, internship_id, resume)
        if success:
            flash('You have successfully applied!', 'success')
        else:
            flash('Application failed or you have already applied.', 'danger')
    except Exception as e:
        print(f"Error in application route: {e}")
        flash('An unexpected error occurred. Please try again.', 'danger')
    
    return redirect(url_for('dashboard.index'))        


@internships.route('/add', methods=['GET', 'POST'])
def add_internship():
    rdb = Recruiters()
    idb = Internships()
    info = rdb.get_recruiter_by_id(current_user.id)
    company_id = info['company_id']

    if request.method == 'POST':
        # Process form data
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        is_remote = bool(request.form.get('is_remote'))
        department = request.form.get('department')
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        is_paid = bool(request.form.get('is_paid'))
        salary = int(request.form['salary'])

        # Example: save to DB
        idb.add_internship(
            company_id=company_id,
            recruiter_id=current_user.id,
            title=title,
            description=description,
            location=location,
            is_remote=is_remote,
            department=department,
            start_date=start_date,
            end_date=end_date,
            is_paid=is_paid,
            salary=salary,
            is_filled=False
        )

        flash('Internship created successfully!', 'success')
        return redirect(url_for('internship.manage_internships'))

    # GET request
    return render_template('add_internships.html', recruiter_id=current_user.id, company_id=company_id)
