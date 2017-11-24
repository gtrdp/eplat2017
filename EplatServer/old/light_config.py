import RPi.GPIO as GPIO
import time
import thread

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
    waktu = 0

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
        waktu += 1
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
    waktu = 0

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
        waktu += 1
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
    waktu = 0

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
        waktu += 1
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
    waktu = 0

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
        waktu += 1
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
