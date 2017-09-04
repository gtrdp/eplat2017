# from flask_socketio import SocketIO, send, emit
from flask import Flask
from flask import request
from flask import Markup
from flask import render_template
import logging

import json
import math

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

        junction = [-7.762049, 110.369364]
        request = json.loads(request.data)
        
        # read previous data
        with open('data.json') as data_file:
            data_json = json.load(data_file)

        # get the json
        ambulance = json.loads(request)
        data = data_json
        if ambulance['lat'] == 0 and ambulance['lon'] == 0:
            # exit signal, emitted when the ambulance leaving the traffic light
            direction = 0
            data['ambulance']['direction'] = 0
            data['ambulance']['angle'] = 0
            data['ambulance']['distance'] = -1
        else:    
            # convert from angle to direction and set appropriate action
            # for corresponding traffic light
            angle = calculate_angle(junction[0], junction[1],\
                    ambulance['lat'], ambulance['lon'])

            # calculate distance
            distance = calculate_distance(junction[0], junction[1],\
                    ambulance['lat'], ambulance['lon'])
            
            direction = convert_angle(angle)
            data['ambulance']['direction'] = direction
            data['ambulance']['angle'] = angle
            data['ambulance']['distance'] = distance

            print direction
            print angle

        # check the delta_distance to determine whether the ambulance is approaching
        # or leaving the traffic light
        if data['ambulance']['distance'] != -1 and distance >= data['ambulance']['distance']:
            # approaching; set appropriate traffic light to green
            data['traffic_light'][direction] = 1
            
        elif data['ambulance']['distance'] != -1 and distance < data['ambulance']['distance']:
            print 'here2'
            # leaving set all traffic light to red
            data['traffic_light'] = [0, 0, 0, 0]
        else:
            print 'here'
            # exit signal, turn all lights to red
            # leaving set all traffic light to red
            data['traffic_light'] = [0, 0, 0, 0]

        # write to file
        data['ambulance']['info'] = ambulance
        with open('data.json', 'w') as data_file:
            data_file.write(json.dumps(data))



        return '{"status": "OK", "message": "Processing the input..."}'

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))
#     emit('update', json)math.

def calculate_distance(lat1, lon1, lat2, lon2):
    earth_radius = 6378.137 # Radius of earth in KM
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

    if degr > 315 and degr < 45:
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # socketio.run(app)
