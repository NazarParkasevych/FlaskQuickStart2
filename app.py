from flask import render_template, redirect, url_for, session, flash
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('_base.html')


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


user_database = {
    "Nazar": "123456",
    "Vlad": "1234567"
}

app.secret_key = 'secretkey'


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return render_template('show_posts.html', post_id=post_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user_database and user_database[username] == password:
            session['username'] = username
            flash("Nothing")
            return redirect(url_for('hello_user', username=request.form['username']))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect(url_for('home'))


@app.route('/register', methods=['GET',  'POST'])
def register():
    if request.method == "POST":
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route("/user/<username>")
def hello_user(username):
    if 'username' in session and session['username'] == username:
        return render_template('user.html', username=username)


@app.route('/users')
def show_users_profile():
    users = [
        'Nazar',
        'Vlad'
    ]
    return render_template('user_list.html', users=users)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)