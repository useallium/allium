from flask import Blueprint, render_template, redirect, url_for, request,jsonify
from flask_login import login_required,current_user
from database.recruiters import Recruiters
from database.students import Students
from database.companies import Companies
from database.applications import Applications
dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def index():
    profile_complete = False
    applications = []

    if current_user.user_type == 'student':
        db = Students()  # Your class to access student info
        student_info = db.get_student_info_by_user_id(current_user.id)
        
        adb = Applications()
        applications = adb.get_applications_by_student(current_user.id)

        print("APPLICATIONS:",(applications))

        if student_info:
            profile_complete = True

    elif current_user.user_type == 'recruiter':
        db = Recruiters()
        recruiter_info = db.get_recruiter_info_by_user_id(current_user.id)
        

        if recruiter_info:
            profile_complete = True

    else:
        # For other user types, you could default to True or do other checks
        profile_complete = True

    return render_template('dashboard.html', profile_complete=profile_complete, applications=applications)


@dashboard.route('/complete-profile/student', methods=['GET', 'POST'])
@login_required
def complete_student_profile():
    db = Students()

    # If already completed, skip
    if db.get_student_info_by_user_id(current_user.id):
        
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        university = request.form.get('university')
        degree = request.form.get('degree')
        graduation_year = request.form.get('graduation_year')
        resume = request.form.get('resume')

        print(f"Received POST: user_id={current_user.id}, uni={university}, grad={graduation_year}, degree={degree}")


        db.add_student(current_user.id, university, degree, graduation_year, resume)
        
        return redirect(url_for('dashboard.index'))

    
    return render_template('complete_student_profile.html')

@dashboard.route('/complete-profile/recruiter', methods=['GET', 'POST'])
@login_required
def complete_recruiter_profile():
    db = Recruiters()

    cdb = Companies()
    companies = cdb.get_company_info_signup()
    
    print(companies)

    if db.get_recruiter_info_by_user_id(current_user.id):
        db.close()
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        job_title = request.form.get('job_title')
        phone_number = request.form.get('phone_number')
        company_id = request.form.get('company_id')
        print(f"Received POST: company_id={company_id}, job_title={job_title}, phone_number={phone_number}")
        
        db.add_recruiter(company_id, current_user.id, job_title, phone_number)
        
        return redirect(url_for('dashboard.index'))


    return render_template('complete_recruiter_profile.html', companies=companies)

@dashboard.route('/dashboard/withdraw', methods=['POST'])
@login_required
def withdraw_application():
    application_id = request.form.get('application_id')

    # Optional: Verify the application belongs to current_user
    db = Applications()
    
    result = db.remove_application(application_id)
    

    if result:
        print("Application withdrawn successfully.", "success")
    else:
        print("Unauthorized or application not found.", "danger")

    
    return redirect(url_for('dashboard.index'))

