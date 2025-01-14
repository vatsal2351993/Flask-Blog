
import os
import secrets
from PIL import Image
from flask import url_for, flash, redirect
from flask_mail import Message
from blog import mail,app
from blog.models import Subscriber



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn 

def save_user_picture(form_picture):
    random_hex = secrets.token_hex(10)  # Generate a unique filename
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)

    # Resize the image
    output_size = (1000, 1000)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='Rblogs@Demo.com' , recipients=[user.email])
    msg.body= f'''To reset your password, visit the following link:
    {url_for('users.reset_token', token= token, _external=True )}
    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)


@app.route('/send_newsletter')
def send_newsletter():
    subscribers = Subscriber.query.all()
    for subscriber in subscribers:
        msg = Message(
            'Latest from R Blogs',
            sender='Rblogs@Demo.com',
            recipients=[subscriber.email]
        )
        msg.body = 'Check out our latest posts at R Blogs!'
        mail.send(msg)

    flash('Newsletter sent successfully!', 'success')
    return redirect(url_for('home'))
