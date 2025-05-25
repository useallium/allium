from flask import Blueprint,render_template,redirect,url_for,jsonify,session,request,flash
from flask_login import UserMixin, login_user, logout_user
auth = Blueprint('auth', __name__)
from database.users import Users
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, email, password_hash, user_type, first_name, last_name):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.user_type = user_type
        self.first_name = first_name
        self.last_name = last_name

    def get_id(self):
        return str(self.id)  # Flask-Login expects this to be a string

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message":"Missing email or password"}), 400
    
    db = Users()

    user = db.get_user_by_email(email)
    db.close()
    print(user)

    if user and check_password_hash(user['password_hash'], password):
        user = User(id=user['user_id'],
            email=user['email'],
            password_hash=user['password_hash'],
            user_type=user['user_type'],
            first_name=user['first_name'],
            last_name=user['last_name'])
        
        login_user(user)  # 🔥 The critical line
        return redirect(url_for('dashboard.index'))
    else:
        print("login")
        return redirect(url_for('auth.login'))
        



@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    user_type = request.form.get('user_type')

    if not email or not password or not first_name or not last_name or not user_type:
        flash('Please fill out all fields','error')
        return redirect(url_for('auth.signup'))
    
    password_hash = generate_password_hash(password)

    try:
        db = Users()

        existing = db.get_user_by_email(email)
        if existing:
            flash('User already exists', 'error')
            return redirect(url_for('auth.signup'))
        
        password_hash = generate_password_hash(password)

        new_user = db.add_user(email, first_name, last_name, password_hash, user_type)
        db.close()

        # No need to check password again on signup!
        user = User(
            id=new_user['user_id'],
            email=new_user['email'],
            password_hash=new_user['password_hash'],
            user_type=new_user['user_type'],
            first_name=new_user['first_name'],
            last_name=new_user['last_name']
        )
        
        login_user(user)  # Log user in immediately
        
        print(user)  # optional debugging
        
        login_user(user)

        # Redirect to profile completion based on user_type
        if user.user_type == 'student':
            return redirect(url_for('dashboard.complete_student_profile'))
        elif user.user_type == 'recruiter':
            return redirect(url_for('dashboard.complete_recruiter_profile'))
        else:
            return redirect(url_for('dashboard.index'))  # fallback


    except Exception as e:
        print(f"Signup error: {e}")  # helpful for debugging
        flash('An error occurred during signup. Please try again.', 'error')
        return redirect(url_for('auth.signup'))




@auth.route('/logout')
def logout():
    print("Before clear:", session)
    logout_user()
    print("After clear:", session)
    return redirect(url_for('web.index'))