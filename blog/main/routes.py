from flask import render_template, request, Blueprint,flash, redirect, url_for
from blog.models import Post
from flask_login import login_required
from blog import db
from blog.models import Subscriber
from blog.posts.forms import CommentForm



main = Blueprint('main',__name__)

@main.route("/")
def front():
    return render_template('front.html')

@main.route("/home")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '', type=str)
    category_filter = request.args.get('category', '', type=str)

    # Fetch posts with optional filters
    query = Post.query
    if search_query:
        query = query.filter(Post.title.ilike(f"%{search_query}%"))
    if category_filter:
        query = query.filter(Post.category == category_filter)

    posts = query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)

    # Fetch distinct categories as a flat list
    categories = [row[0] for row in Post.query.with_entities(Post.category).distinct().all()]

    # Pass the comment form for each post
    form = CommentForm()

    return render_template(
        'home.html',
        posts=posts,
        categories=categories,
        form=form,
        search_query=search_query,
        category_filter=category_filter
    )

    
@main.route('/about')
@login_required
def about():
    return render_template('about.html')


@main.route('/subscribe', methods=['GET','POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            flash('Please provide a valid email address.', 'danger')
            return redirect(url_for('main.about'))

        # Check if the email is already subscribed
        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            flash('This email is already subscribed!', 'warning')
            return redirect(url_for('main.about'))

        # Save the new subscriber
        new_subscriber = Subscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()

        flash('Thank you for subscribing!', 'success')
        return redirect(url_for('main.about'))
    
    return render_template('subscribe.html')
    





