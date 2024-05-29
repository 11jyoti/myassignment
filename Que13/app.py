from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('notification', 'Connected to the server.')

# Function to send notification to all connected clients
def send_notification(message):
    socketio.emit('notification', message)

if __name__ == '__main__':
    socketio.run(app)