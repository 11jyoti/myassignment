from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Set the secret key to use sessions
app.secret_key = 'your_secret_key_here'

# Configure the app to use Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        # Store the user's name in the session
        session['name'] = name
        return render_template('submit.html', name=name)
    return 'Method Not Allowed', 405

@app.route('/profile')
def profile():
    # Retrieve the user's name from the session
    name = session.get('name')
    if name:
        return render_template('profile.html', name=name)
    else:
        return 'Unauthorized', 401

if __name__ == '__main__':
    app.run(debug=True)