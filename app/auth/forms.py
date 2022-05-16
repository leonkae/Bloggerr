from math import remainder
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length,Email, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name= StringField('last_name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Signup')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('save your login info')
    submit = SubmitField('login')
     