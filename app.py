from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/users")
def user_list():
    users_list = [
        'Parkasevych Nazar'
    ]

    return render_template(
        'user_list.html',
        users_list=users_list
    )


@app.route("/users/string:username>")
def user(username):
    return render_template(
        'user.html',
        username=username,
    )

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/about')
def about():
    return render_template('about.html')