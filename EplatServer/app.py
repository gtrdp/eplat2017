# from flask_socketio import SocketIO, send, emit
from flask import Flask
from flask import request
from flask import Markup
from flask import render_template
import logging

import RPi.GPIO as GPIO
import time
import thread

import json
import math

import light_config

app = Flask(__name__)
# socketio = SocketIO(app)
# set the reporting error only
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
app.debug = True

arah = 0
waktu = 0
antrian_a = []
antrian_b = []
antrian_c = []
antrian_d = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # emit('update', request.data)
        print(request.data)
        return 'Processing the input...'
    else:
        print("someone access the raspberry in GET method!!")
        return render_template("dashboard.html")
        # return "hello"

@app.route('/interrupt', methods=["GET"])
def keyboard_interrupt():
    if request.method == 'GET':
        thread.interrupt_main()
        return 'Interrupt!'

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        print(request.data)

        junction = [-7.762049, 110.369364]

        # read previous data
        with open('data.json') as data_file:
            data_json = json.load(data_file)

        # get the json
        ambulance = json.loads(request.data)
        data = data_json
        if ambulance['lat'] == 0 and ambulance['lon'] == 0:
            # exit signal, emitted when the ambulance leaving the traffic light
            direction = 0
            angle = 0
            distance = -1
        else:
            # convert from angle to direction and set appropriate action
            # for corresponding traffic light
            angle = calculate_angle(junction[0], junction[1],\
                    ambulance['lat'], ambulance['lon'])

            # calculate distance
            distance = calculate_distance(junction[0], junction[1],\
                    ambulance['lat'], ambulance['lon'])

            direction = convert_angle(angle)

            print direction
            print angle
            print distance

        # check the delta_distance to determine whether the ambulance is approaching
        # or leaving the traffic light
        if distance < data['ambulance']['distance'] and distance > 0:
            # approaching;
            if sum(data['traffic_light']) == 0:
                # the lights are still off; set appropriate traffic light to green
                data['traffic_light'][direction] = 1
                print 'turned on!'
        elif distance > data['ambulance']['distance']:
            # leaving set all traffic light to red
            data['traffic_light'] = [0, 0, 0, 0]
            print 'turned off!'

        # write to file
        data['ambulance']['direction'] = direction
        data['ambulance']['angle'] = angle
        data['ambulance']['distance'] = distance
        data['ambulance']['info'] = ambulance
        with open('data.json', 'w') as data_file:
            data_file.write(json.dumps(data))



    return '{"status": "OK", "message": "Processing the input..."}'

@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        # read previous data
        with open('data.json') as data_file:
            return json.dumps(json.load(data_file))

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))
#     emit('update', json)math.

def calculate_distance(lat1, lon1, lat2, lon2):
    earth_radius = 6000 # Radius of earth in KM
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180

    a = math.sin(dLat/2) * math.sin(dLat/2) + \
    math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * \
    math.sin(dLon/2) * math.sin(dLon/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = earth_radius * c

    return d * 1000 # meters

def calculate_angle(lat1, lon1, lat2, lon2):
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180

    y = math.sin(dLon) * math.cos(lat2 * math.pi / 180)
    x = math.cos(lat1 * math.pi / 180) * math.sin(lat2 * math.pi / 180) \
        - math.sin(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.cos(dLon)

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360

    return brng

def convert_angle(degr):
    direction = -1

    if degr > 315 or degr < 45:
        # north
        direction = 0
    elif degr > 45 and degr < 135:
        # east
        direction = 1
    elif degr > 135 and degr < 225:
        # south
        direction = 2
    else:
        # west
        direction = 3

    return direction

def main_loop():
    try:
        while True :
            print("main loop...")
            selatan_hijau()
            selatan_kuning()

            timur_hijau()
            timur_kuning()

            barat_hijau()
            barat_kuning()

            utara_hijau()
            utara_kuning()

    except KeyboardInterrupt:
        #input_kondisi()
        print("Interrupt!")
        main_loop()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # socketio.run(app)

    init_kondisi()
    main_loop()
