from werkzeug.security import generate_password_hash,check_password_hash
from app import db
from app import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.querry.get(int(user_id))