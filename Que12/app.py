from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initial data
data = {'value': 0}

@app.route('/')
def index():
    return render_template('index.html', data=data)

@socketio.on('update')
def update(value):
    data['value'] = value
    socketio.emit('update', value, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)