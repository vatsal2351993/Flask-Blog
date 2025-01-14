from flask import render_template, url_for, flash,redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from blog import db
from blog.models import Post, Comment
from blog.posts.forms import PostForm, CommentForm
from blog.users.utils import save_user_picture




posts = Blueprint('posts',__name__)




@posts.route('/post/new', methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        # Handle image upload
        picture_file = 'default.jpg'  # Default image
        if form.picture.data:
            picture_file = save_user_picture(form.picture.data)

        # Create a new post
        post = Post(
            title=form.title.data,
            content=form.content.data,
            user_images=picture_file,  # Save the uploaded image filename
            author=current_user,  # Assuming `author` relationship exists
            category=form.category.data
        )
        db.session.add(post)
        db.session.commit()

        flash("Your post has been created!", 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', form=form, legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    # Generate the image URL if an image exists for the post
    user_images = None
    if post.user_images:
        user_images = url_for('static', filename='img/' + post.user_images)
    return render_template('post.html', post=post, user_images=user_images)





@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit() 
    flash("Your post has been deleted!", 'success')
    return redirect(url_for('main.home'))

@posts.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post_id=post.id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    return redirect(url_for('main.home'))










