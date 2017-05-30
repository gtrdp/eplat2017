from flask import Flask
from flask import request
import logging

app = Flask(__name__)
# set the reporting error only
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        print(request.data)
        return 'Processing the input...'
    else:
        print("someone access the raspberry in GET method!!")
        return 'Hello world! Eplat 2017!'



if __name__ == '__main__':
    app.run(host='0.0.0.0')
