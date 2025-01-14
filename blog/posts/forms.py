from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Upload Image or Snippet', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    category = SelectField('Category', choices=[
        ('General', 'General'),
        ('Technology', 'Technology'),
        ('Food', 'Food'),
        ('Lifestyle', 'Lifestyle'),
        ('Education', 'Education'),
        ('Travel','Travel')
    ], validators=[DataRequired()])
    submit = SubmitField('Post')
    
class CommentForm(FlaskForm):
    content = TextAreaField('Add a Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')    
    
    