from flask import Flask, render_template, redirect, url_for, flash, request, session
from config import Config
from models import mongo, bcrypt, init_app
from wtforms import Form, StringField, PasswordField, validators

app = Flask(_name_)
app.config.from_object(Config)

init_app(app)

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        users = mongo.db.users
        existing_user = users.find_one({'username': form.username.data})

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            users.insert_one({'username': form.username.data, 'password': hashpass})
            flash('You have successfully registered! You can now login.', 'success')
            return redirect(url_for('signin'))
        else:
            flash('That username already exists!', 'danger')

    return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        users = mongo.db.users
        login_user = users.find_one({'username': form.username.data})

        if login_user:
            if bcrypt.check_password_hash(login_user['password'], form.password.data):
                session['username'] = form.username.data
                flash('You have successfully logged in.', 'success')
                return redirect(url_for('hello'))
            else:
                flash('Invalid username/password combination', 'danger')
        else:
            flash('Invalid username/password combination', 'danger')

    return render_template('signin.html', form=form)

@app.route('/hello')
def hello():
    if 'username' in session:
        return f"Hello, {session['username']}! Welcome to Geeks!"
    return redirect(url_for('signin'))

@app.route('/signout')
def signout():
    session.pop('username', None)
    flash('You have successfully logged out.', 'success')
    return redirect(url_for('signin'))

if _name_ == '_main_':
    app.run(debug=True)