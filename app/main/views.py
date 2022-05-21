from flask import render_template,redirect,url_for,request,abort
from . import main_blueprint as main
from flask_login import current_user, login_required
from .forms import PostsForm,CommentForm,UpdateAccount
from .models import Post,User,Comments
from app import db,photos
from datetime import datetime as dt


@main.route('/')
def index():
    posts = Post.query.all()
    form = CommentForm()
    
    return render_template('index.html',posts=posts, comment_form=form)

@main.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    form = CommentForm()
    return render_template('posts.html',posts=posts, comment_form=form)


@main.route('/posts/add', methods=['GET', 'POST'])
@login_required
def create_post():
    create_post=PostsForm()
    now = dt.now()
    if create_post.validate_on_submit():
        date_posted=now.strftime('%a %d %b %Y %H:%M:%S')
        user_id=current_user._get_current_object().id
        post = Post(title=create_post.title.data, content=create_post.content.data,date_posted=date_posted,user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main_blueprint.posts'))
    return render_template('createpost.html',create=create_post)

    


@main.route('/comment/<int:post_id>/add', methods=['POST'])
@login_required
def add_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comments(comment=form.comment.data, post_id = post_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main_blueprint.posts',post_id=post_id))
    return render_template('posts.html',comment_form=form)


@main.route('/account/<uname>')
@login_required
def account(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template('account.html',user=user)

@main.route('/account/<uname>/update/',methods= ['GET', 'POST'])
@login_required
def update_account(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    update = UpdateAccount()   
    if update.validate_on_submit():
        user.bio = update.bio.data
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.account',uname=user.username))
    return render_template('update.html',update=update)
        
@main.route('/account/<uname>/update/pic', methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    
    return redirect(url_for('main_blueprint.account', uname = uname))

