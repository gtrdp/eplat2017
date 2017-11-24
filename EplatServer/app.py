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

antrian = {0: {}, 1: {}, 2: {}, 3: {}}
vehicles = {}
light = False

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
        # thread.interrupt_main()

        # define if the vehicle is approaching or leaving ======================
        # which side does the vehicle come from ================================
        print(request.data)

        junction = [-7.762049, 110.369364]
        # approaching =

        # get the json
        # json example:
        # {"device_id":"12345","direction":"north","lat":-7.759257028937096,"lon":110.36958307027817,"vehicle_type":0}
        vehicle = json.loads(request.data)
        if vehicle['lat'] == 0 and vehicle['lon'] == 0:
            # exit signal, emitted when the ambulance leaving the traffic light
            direction = -1
            angle = -1
            distance = -1
        else:
            # convert from angle to direction and set appropriate action
            # for corresponding traffic light
            angle = calculate_angle(junction[0], junction[1],\
                    vehicle['lat'], vehicle['lon'])
            # calculate distance
            distance = calculate_distance(junction[0], junction[1],\
                    vehicle['lat'], vehicle['lon'])

            direction = convert_angle(angle)

            print direction
            print angle
            print distance

        # check the delta_distance to determine whether the ambulance is approaching
        # or leaving the traffic light

        # give default value for new vehicle
        if vehicle['device_id'] not in vehicles:
            # remark: [direction, angle, distance, type]
            vehicles[vehicle['device_id']] = [0, 0, 0, 0]

        # if distance < vehicles[vehicle['device_id']][2] and distance > 0:
        #     # approaching;
        # elif distance > vehicles[vehicle['device_id']][2] :
        #     # leaving set all traffic light to red

        # update values
        vehicles[vehicle['device_id']][0] = direction
        vehicles[vehicle['device_id']][1] = angle
        vehicles[vehicle['device_id']][2] = distance
        vehicles[vehicle['device_id']][3] = vehicle['vehicle_type']

        # input kondisi ========================================================
        # queue checking, check if it is a new vehicle or not
        if vehicle['device_id'] not in antrian[vehicle['vehicle_type']]:
            print("New vehicle!\n")
            antrian[vehicle['vehicle_type']][vehicle['device_id']] = direction

        # check vehicle priority if it is higher or not
        # check antrian priority, turn on appropriate lights
        for vehicle_type, kendaraan in antrian.iteritems():
            if len(kendaraan) > 0:
                # there is still vehicle
                print("antrian is not empty\n")
                turn_on_lights(kendaraan.values()[0])
                break

        # sending exit message, handle it
        # check if it is an exit message, remove from queue, turn off the lights,
        # go to next queue, otherwise return to main loop
        if distance == -1:
            # remove from queue
            print("exit message, remove from queue...\n")
            del antrian[vehicle['vehicle_type']][vehicle['device_id']]
            del vehicles[vehicle['device_id']]

            # check antrian again
            antrian_counter = 0
            for vehicle_type, kendaraan in antrian.iteritems():
                if len(kendaraan) > 0:
                    # there is still vehicle
                    turn_on_lights(kendaraan.values()[0])
                    antrian_counter += 1
                    break

            # go to main loop if antrian is empty
            if antrian_counter == 0:
                print('return to main loop...\n\n')
                main_loop()

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

def input_kondisi():
    global arah
    global waktu
    global antrian_a
    global antrian_b
    global antrian_c
    global antrian_d

    try:

	# baca input interrupt
        print("Interrupt!!!")
        x=int(input("Arah Datang Kendaraan: "))
        y=raw_input("Id Kendaraan: ")

        # masukkan ke antrian
        if (y == 'a'):
            antrian_a.append(x)
        if (y == 'b'):
            antrian_b.append(x)
        if (y == 'c'):
            antrian_c.append(x)
        if (y == 'd'):
            antrian_d.append(x)
        waktu = 0

        # baca antrian
        while (len(antrian_a) > 0):
            m = antrian_a[0]

            if m ==1 :
                selatan_hijau(waktu)
            if m ==2 :
                timur_hijau(waktu)
            if m ==3 :
                barat_hijau(waktu)
            if m ==4 :
                utara_hijau(waktu)

            m = antrian_a.pop(0) # ambil antrian paling depan

            if m ==1 :
                selatan_kuning(waktu)
            if m ==2 :
                timur_kuning(waktu)
            if m ==3 :
                barat_kuning(waktu)
            if m ==4 :
                utara_kuning(waktu)


        while (len(antrian_b) > 0):
            m = antrian_b[0]

            if m ==1 :
                selatan_hijau(waktu)
            if m ==2 :
                timur_hijau(waktu)
            if m ==3 :
                barat_hijau(waktu)
            if m ==4 :
                utara_hijau(waktu)

            m = antrian_b.pop(0) # ambil antrian paling depan

            if m ==1 :
                selatan_kuning(waktu)
            if m ==2 :
                timur_kuning(waktu)
            if m ==3 :
                barat_kuning(waktu)
            if m ==4 :
                utara_kuning(waktu)

        while (len(antrian_c) > 0):
            m = antrian_c[0]

            if m ==1 :
                selatan_hijau(waktu)
            if m ==2 :
                timur_hijau(waktu)
            if m ==3 :
                barat_hijau(waktu)
            if m ==4 :
                utara_hijau(waktu)

            m = antrian_c.pop(0) # ambil antrian paling depan

            if m ==1 :
                selatan_kuning(waktu)
            if m ==2 :
                timur_kuning(waktu)
            if m ==3 :
                barat_kuning(waktu)
            if m ==4 :
                utara_kuning(waktu)

        while (len(antrian_d) > 0):
            m = antrian_d[0]

            if m ==1 :
                selatan_hijau(waktu)
            if m ==2 :
                timur_hijau(waktu)
            if m ==3 :
                barat_hijau(waktu)
            if m ==4 :
                utara_hijau(waktu)

            m = antrian_d.pop(0) # ambil antrian paling depan

            if m ==1 :
                selatan_kuning(waktu)
            if m ==2 :
                timur_kuning(waktu)
            if m ==3 :
                barat_kuning(waktu)
            if m ==4 :
                utara_kuning(waktu)


        # kembali ke state awal
        main_loop()

    except KeyboardInterrupt:
        input_kondisi()

def turn_on_lights(jalur = 0):
    if jalur == 0:
        # north
        light_config.utara_hijau()
    elif jalur == 1:
        # east
        light_config.timur_hijau()
    elif jalur == 2:
        # south
        light_config.selatan_hijau()
    elif jalur == 3:
        # west
        light_config.barat_hijau()

def main_loop(light = 0):
    try:
        while True :
            print("main loop...")
            light_config.selatan_hijau()
            light_config.selatan_kuning()

            light_config.timur_hijau()
            light_config.timur_kuning()

            light_config.barat_hijau()
            light_config.barat_kuning()

            light_config.utara_hijau()
            light_config.utara_kuning()

    except KeyboardInterrupt:
        #input_kondisi()
        print("Main loop Interrupt!\n\n")
        # main_loop()

if __name__ == '__main__':
    light_config.init_kondisi()
    app.run(host='0.0.0.0')
    # socketio.run(app)
    main_loop()
