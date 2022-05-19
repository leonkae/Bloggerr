from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField



class PostsForm(FlaskForm):
    title = StringField('enter title')
    content = TextAreaField('hi Bloggerr lets hear you')
    date_posted = StringField()
    submit=SubmitField('Blog')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('comment')    
    submit=SubmitField('submit comment')   
    

class UpdateAccount(FlaskForm):
    bio = TextAreaField('bio')    
    submit=SubmitField('update bio')  