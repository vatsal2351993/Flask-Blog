from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from blog.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2 , max=20)])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_field(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is already taken. Please choose a different credentials")
        
    def validate_field(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("That email is already taken. Please choose a different credentials")

class LoginForm(FlaskForm):
    username= username = StringField('Username', validators=[DataRequired(),Length(min=2 , max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2 , max=20)])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Pitcure', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_field(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is already taken. Please choose a different credentials")
        
    def validate_field(self,email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
             raise ValidationError("That email is already taken. Please choose a different credentials")
            
class RequestResetForm(FlaskForm):
     email = EmailField('Email',validators=[DataRequired(),Email()])
     submit = SubmitField('Request Password Reset')

     def validate_field(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that account. You must register first")
        
class ResetPasswordForm(FlaskForm):
        password = PasswordField('Password', validators=[DataRequired()])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
        submit = SubmitField('Reset Password')
             