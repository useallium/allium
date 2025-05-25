from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from database.students import Students
from database.recruiters import Recruiters

profile = Blueprint('profile', __name__, url_prefix='/profile')

@profile.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if current_user.user_type == 'student':
        db = Students()
        user_data = db.get_student_by_id(current_user.id)

        if request.method == 'POST':
            university = request.form.get('university')
            degree = request.form.get('degree')
            graduation_year = request.form.get('graduation_year')
            resume = request.form.get('resume')

            updated = db.update_student(current_user.id, university, degree, graduation_year, resume)
            db.close()

            if updated:
                flash('Profile updated successfully!', 'success')
                return redirect(url_for('dashboard.index'))
            else:
                flash('Failed to update profile.', 'danger')

        return render_template('edit_profile.html', student=user_data)

    elif current_user.user_type == 'recruiter':
        db = Recruiters()
        user_data = db.get_recruiter_by_id(current_user.id)

        if request.method == 'POST':
            job_title = request.form.get('job_title')
            phone_number = request.form.get('phone_number')

            updated = db.update_recruiter(current_user.id, job_title, phone_number)
            db.close()

            if updated:
                flash('Profile updated successfully!', 'success')
                return redirect(url_for('dashboard.index'))
            else:
                flash('Failed to update profile.', 'danger')

        return render_template('edit_profile.html', recruiter=user_data)

    else:
        flash("Access denied.", "danger")
        return redirect(url_for('dashboard.index'))
