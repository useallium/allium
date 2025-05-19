from flask import Blueprint, render_template, session, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/auth')
def index():
    if 'user_id' not in session:
        # Not logged in — show login page
        return render_template('login.html')

    user_type = session.get('user_type')
    if user_type == 'student':
        return render_template('student_signup.html')
    elif user_type == 'recruiter':
        return render_template('recruiter_signup.html')
    else:
        # Unknown user type, fallback or logout maybe
        return redirect(url_for('auth.logout'))

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.auth_index'))
