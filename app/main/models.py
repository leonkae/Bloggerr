from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app import db
from app import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_pic_path = db.Column(db.String(120), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255))   
    posts = db.relationship('Post', backref='author', lazy=True)
      
    @property
    def password(self):
        raise AttributeError('You cannot Read Attribute Error')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.username}>'
      
    
    
class Post(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      title = db.Column(db.String(255), nullable=False)
      date_posted = db.Column(db.DateTime, nullable=False, default=datetime)
      content = db.Column(db.Text, nullable=False)
      user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
      comments = db.relationship('Comments', backref='comments',lazy = True)

      def __repr__(self):
          return f"User('{self.title}','{self.date_posted}','{self.content}')"    
      


class Comments(db.Model):        
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))    
    
