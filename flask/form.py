from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
	username=StringField('Username', 
		validator=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',
		validator=[DataRequired(),Email()])
	password=PasswordField('Password',
		validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password',
		validators=[DataRequired(),
		EqualTo('password')])
	submit=SubmitField('Sign Up')

class loginForm(FlaskForm):
	email=StringField('Email',
		validator=[DataRequired(),Email()])
	password=PasswordField('Password',
		validators=[DataRequired()])
	remeber=BooleanField('Remeber Me')
	submit=SubmitField('Login')

