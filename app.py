from flask import Flask,render_template,flash,redirect,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '59f407f167538988e3a11cacf723e820'

posts = [
    {
        'author':'neth nduta',
        'title':'blog post 1',
        'content':'this is my blog post',
        'date_posted':'May 16 2022'
    },
      {
        'author':'Joseph nduta',
        'title':'blog post 2',
        'content':'this is my other blog post',
        'date_posted':'May 16 2022'
    },
        {
        'author':'Rachel Wacuka',
        'title':'blog post 3',
        'content':'this is my very new blog post',
        'date_posted':'May 16 2022'
    }
]
@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'successfully created an account for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)