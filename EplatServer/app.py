from flask import Flask
from flask import request
from flask import Markup
from flask import render_template
import logging

app = Flask(__name__)
# set the reporting error only
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
# app.debug = True

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        print(request.data)
        return 'Processing the input...'
    else:
        print("someone access the raspberry in GET method!!")
        return render_template("map.html")
        # return "hello"



if __name__ == '__main__':
    app.run(host='0.0.0.0')
