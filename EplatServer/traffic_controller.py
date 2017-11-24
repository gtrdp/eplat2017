import RPi.GPIO as GPIO
import time
import json

def init_kondisi():
    #Kondisi output
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    #Timur
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    #Selatan
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    #Barat
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    #Utara
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

def timur_hijau (detik = 0):
    GPIO.output(24, 1)
    GPIO.output(16, 0)
    GPIO.output(27, 0)
    GPIO.output(6, 0)

    GPIO.output(23, 1)
    GPIO.output(12, 1)
    GPIO.output(17, 1)
    GPIO.output(5, 1)

    GPIO.output(18, 0)
    GPIO.output(25, 1)
    GPIO.output(4, 1)
    GPIO.output(22, 1)

    for i in range(10 - detik):
        time.sleep(1)

def timur_kuning (detik = 0):
    GPIO.output(24, 1)
    GPIO.output(16, 0)
    GPIO.output(27, 0)
    GPIO.output(6, 0)

    GPIO.output(23, 0)
    GPIO.output(12, 1)
    GPIO.output(17, 1)
    GPIO.output(5, 1)

    GPIO.output(18, 1)
    GPIO.output(25, 1)
    GPIO.output(4, 1)
    GPIO.output(22, 1)

    for i in range(2):
        time.sleep(1)

def selatan_hijau (detik = 0):
    GPIO.output(24, 0)
    GPIO.output(16, 1)
    GPIO.output(27, 0)
    GPIO.output(6, 0)

    GPIO.output(23, 1)
    GPIO.output(12, 1)
    GPIO.output(17, 1)
    GPIO.output(5, 1)

    GPIO.output(18, 1)
    GPIO.output(25, 0)
    GPIO.output(4, 1)
    GPIO.output(22, 1)

    for i in range(10 - detik):
        time.sleep(1)

def selatan_kuning (detik = 0):
	GPIO.output(24, 0)
	GPIO.output(16, 1)
	GPIO.output(27, 0)
	GPIO.output(6, 0)

	GPIO.output(23, 1)
	GPIO.output(12, 0)
	GPIO.output(17, 1)
	GPIO.output(5, 1)

	GPIO.output(18, 1)
	GPIO.output(25, 1)
	GPIO.output(4, 1)
	GPIO.output(22, 1)

	for i in range(2):
		time.sleep(1)

def barat_hijau (detik = 0):
    GPIO.output(24, 0)
    GPIO.output(16, 0)
    GPIO.output(27, 1)
    GPIO.output(6, 0)

    GPIO.output(23, 1)
    GPIO.output(12, 1)
    GPIO.output(17, 1)
    GPIO.output(5, 1)

    GPIO.output(18, 1)
    GPIO.output(25, 1)
    GPIO.output(4, 0)
    GPIO.output(22, 1)

    for i in range(10 - detik):
        time.sleep(1)

def barat_kuning (detik = 0):
    GPIO.output(24, 0)
    GPIO.output(16, 0)
    GPIO.output(27, 1)
    GPIO.output(6, 0)

    GPIO.output(23, 1)
    GPIO.output(12, 1)
    GPIO.output(17, 0)
    GPIO.output(5, 1)

    GPIO.output(18, 1)
    GPIO.output(25, 1)
    GPIO.output(4, 1)
    GPIO.output(22, 1)

    for i in range(2):
        time.sleep(1)

def utara_hijau(detik = 0):
    GPIO.output(24, 0)
    GPIO.output(16, 0)
    GPIO.output(27, 0)
    GPIO.output(6, 1)

    GPIO.output(23, 1)
    GPIO.output(12, 1)
    GPIO.output(17, 1)
    GPIO.output(5, 1)

    GPIO.output(18, 1)
    GPIO.output(25, 1)
    GPIO.output(4, 1)
    GPIO.output(22, 0)

    for i in range(10 - detik):
        time.sleep(1)

def utara_kuning(detik = 0):
	GPIO.output(24, 0)
	GPIO.output(16, 0)
	GPIO.output(27, 0)
	GPIO.output(6, 1)

	GPIO.output(23, 1)
	GPIO.output(12, 1)
	GPIO.output(17, 1)
	GPIO.output(5, 0)

	GPIO.output(18, 1)
	GPIO.output(25, 1)
	GPIO.output(4, 1)
	GPIO.output(22, 1)

	for i in range(2):
		time.sleep(1)

def save_state(current_state):
    with open('state.json', 'w') as data_file:
            data_file.write(json.dumps(current_state))

def read_state():
    with open('state.json') as data_file:
        previous_state = json.load(data_file)

    return previous_state

def main_loop():
    # read state
    previous_state = read_state()
    foo = previous_state['light']
    current_state = {}

    if foo == 0:
        current_state['light'] = 0
        save_state(current_state)
        selatan_hijau()
        selatan_kuning()

    if foo == 0 or foo == 1:
        current_state['light'] = 1
        save_state(current_state)
        timur_hijau()
        timur_kuning()

    if foo == 0 or foo == 1 or foo == 2:
        current_state['light'] = 2
        save_state(current_state)
        barat_hijau()
        barat_kuning()

    if foo == 0 or foo == 1 or foo == 2 or foo == 3:
        current_state['light'] = 3
        save_state(current_state)
        utara_hijau()
        utara_kuning()

    # enter main loop
    while True:
        print("main loop...")

        current_state['light'] = 0
        save_state(current_state)
        selatan_hijau()
        selatan_kuning()

        current_state['light'] = 1
        save_state(current_state)
        timur_hijau()
        timur_kuning()

        current_state['light'] = 2
        save_state(current_state)
        barat_hijau()
        barat_kuning()

        current_state['light'] = 3
        save_state(current_state)
        utara_hijau()
        utara_kuning()

if __name__ == "__main__":
	init_kondisi()
	main_loop()
