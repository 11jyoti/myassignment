#.Explain how to set up a Flask application to handle form submissions using POST requests.
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f'Name: {name}, Email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
