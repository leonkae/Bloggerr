from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user, login_required
from app.main.models import User
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import auth_blueprint as auth
from app.main import main_blueprint
from app import db





@auth.route('/about')
def about():
  return render_template('about.html')

@auth.route("/register", methods=['GET','POST'])
def register():
      signup = RegistrationForm()
      if signup.validate_on_submit():
            flash(f'{signup.username.data} Account created successfully.', 'success')
            user=User(first_name=signup.first_name.data, last_name=signup.last_name.data , username=signup.username.data,email=signup.email.data,password=signup.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth_blueprint.login'))
      title = "sigup"  
      return render_template('auth/register.html', title = title , form=signup)
  
  


@auth.route ('/login', methods=['GET','POST'])
def login():
    login=LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(email=login.email.data).first()
        if user is None and user.verify_password(login.password.data):
            flash("Invalid email or password")
            return redirect(url_for('auth_blueprint.login'))
        login_user(user, remember=login.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main_blueprint.posts'))
    return render_template('auth/login.html', login=login)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_blueprint.index'))

