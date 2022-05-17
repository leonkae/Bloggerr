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
  
  
@auth.route("/login")
def login():
      form = LoginForm()
      if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                  return redirect(url_for('about'))
            else:
                flash('login unsuccessful.Check credentials', 'danger')
      return render_template('auth/login.html', title = 'Login', form=form)