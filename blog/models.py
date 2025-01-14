from blog import db,app, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer




@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    __tablename__ = "user"
    __tableargs__ ={'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8') # Token is now returned as a string

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_images = db.Column(db.String(20),nullable=False, default='default.jpg')
    content = db.Column(db.Text,nullable=False)
    category = db.Column(db.String(50), nullable=False, default='General')
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)
   


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_subscribed = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Subscriber {self.email}>"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)  # Link to a Post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Link to a User

    def __repr__(self):
        return f"Comment('{self.content}', '{self.date_posted}')"

likes = db.Table('likes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
)

with app.app_context():
    db.create_all()        