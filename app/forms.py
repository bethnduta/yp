from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length,Email,EqualTo,ValidationError
from app.models import User

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')
    
    def validate_username(self, username):
        
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username exists')
        
    def validate_email(self, email):
            
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email exists') 
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')    
    
    
    
class updateAccountForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('update')
    picture = FileField('update Profile picture', validators=[FileAllowed(['jpg','png'])])
    def validate_username(self, username):
                if username.data != current_user.username:
                    user = User.query.filter_by(username=username.data).first()
                    if user:
                        raise ValidationError('Username exists')
        
    def validate_email(self, email):
         if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email exists')   
    
        
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])  
    content = TextAreaField('Content', validators=[DataRequired()]) 
    submit = SubmitField('Post')
         
        