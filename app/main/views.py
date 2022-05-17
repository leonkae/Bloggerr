from flask import render_template,redirect,url_for,request
from . import main_blueprint as main



@main.route('/')
def index():
    return render_template('index.html')