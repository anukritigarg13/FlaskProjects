from flask import Flask,render_template,url_for
from form import Registration, loginForm
app=Flask(__name__)
app.config['SECRET_KEY']='8c3e73913edf142b844bbd77188c5318'

posts=[{'author':'Anukriti',
'title':'Blog Post 1',
'content':'First post content',
'date_posted':'April 20,2001'},
{'author':'Anu',
'title':'Blog Post 2',
'content':'Second post content',
'date_posted':'April 19,2001'}





]


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',p=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='all is well')

@app.route("/register")
def register():
	form=Registration()
	return render_template('register.html',title='Register',form=form)
@app.route("/login")
def login():
	form=loginForm()
	return render_template('login.html',title='Login',form=form)
if __name__=='__main__':
	app.run(debug=True)