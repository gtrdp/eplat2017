# from flask_socketio import SocketIO, send, emit
from flask import Flask
from flask import request
from flask import Markup
from flask import render_template
import logging

app = Flask(__name__)
# socketio = SocketIO(app)
# set the reporting error only
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
app.debug = True

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # emit('update', request.data)
        print(request.data)
        return 'Processing the input...'
    else:
        print("someone access the raspberry in GET method!!")
        return render_template("map.html")
        # return "hello"

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        # emit('update', request.data)
        print(request.data)
        return 'Processing the input...'

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))
#     emit('update', json)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # socketio.run(app)
