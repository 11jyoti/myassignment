from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('submit.html', name=name)
    return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(debug=True)