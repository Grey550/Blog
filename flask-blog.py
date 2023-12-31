from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'cafcbebed98c409a66f69fb30ba60efd'

posts = [
    {
        'author': 'Angel Eyes',
        'title' : 'Blog Post One',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2022'
    },
    {
        'author': 'Chris Boys',
        'title' : 'Blog Post Two',
        'content' : 'Second post content',
        'date_posted' : 'April 21, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)