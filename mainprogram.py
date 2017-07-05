import RPi.GPIO as GPIO
import time

gak_ada_ambulan = True

def init_condition():
    # set kondisi awal 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)

    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

def timur():
    #hijau
    GPIO.output(4, 0)
    GPIO.output(12, 1)
    GPIO.output(18, 1)
    GPIO.output(24, 1)
    GPIO.output(5, 0)
    GPIO.output(13, 0)
    GPIO.output(22, 0)
    GPIO.output(25, 0)
    GPIO.output(6, 1)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    GPIO.output(26, 0)
    for i in range(10):
        time.sleep(1)

    #kuning
    GPIO.output(4, 0)
    GPIO.output(12, 1)
    GPIO.output(18, 1)
    GPIO.output(24, 1)
    GPIO.output(5, 1)
    GPIO.output(13, 0)
    GPIO.output(22, 0)
    GPIO.output(25, 0)
    GPIO.output(6, 0)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    GPIO.output(26, 0)
    for i in range(2):
        time.sleep(1)

def barat():
    #hijau
    GPIO.output(4, 1)
    GPIO.output(12, 0)
    GPIO.output(18, 1)
    GPIO.output(24, 1)
    GPIO.output(5, 0)
    GPIO.output(13, 0)
    GPIO.output(22, 0)
    GPIO.output(25, 0)
    GPIO.output(6, 0)
    GPIO.output(17, 1)
    GPIO.output(23, 0)
    GPIO.output(26, 0)
    time.sleep(10)
    
    #kuning
    GPIO.output(4, 1)
    GPIO.output(12, 0)
    GPIO.output(18, 1)
    GPIO.output(24, 1)
    GPIO.output(5, 0)
    GPIO.output(13, 1)
    GPIO.output(22, 0)
    GPIO.output(25, 0)
    GPIO.output(6, 0)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    GPIO.output(26, 0)
    time.sleep(2)

def utara():
    #hijau
    GPIO.output(4, 1)
    GPIO.output(12, 1)
    GPIO.output(18, 0)
    GPIO.output(24, 1)
    GPIO.output(5, 0)
    GPIO.output(13, 0)
    GPIO.output(22, 0)
    GPIO.output(25, 0)
    GPIO.output(6, 0)
    GPIO.output(17, 0)
    GPIO.output(23, 1)
    GPIO.output(26, 0)
    time.sleep(10)

    #kuning
    GPIO.output(4, 1)
    GPIO.output(12, 1)
    GPIO.output(18, 0)
    GPIO.output(24, 1)
    GPIO.output(5, 0)
    GPIO.output(13, 0)
    GPIO.output(22, 1)
    GPIO.output(25, 0)
    GPIO.output(6, 0)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    GPIO.output(26, 0)
    time.sleep(2)

def selatan():
    #hijau
    GPIO.output(4, 1)
    GPIO.output(12, 1)
    GPIO.output(18, 1)
    GPIO.output(24, 0)
    GPIO.output(5, 0)
    GPIO.output(13, 0)
    GPIO.output(22, 0)
    GPIO.output(25, 0)
    GPIO.output(6, 0)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    GPIO.output(26, 1)
    time.sleep(10)

    #kuning
    GPIO.output(4, 1)
    GPIO.output(12, 1)
    GPIO.output(18, 1)
    GPIO.output(24, 0)
    GPIO.output(5, 0)
    GPIO.output(13, 0)
    GPIO.output(22, 0)
    GPIO.output(25, 1)
    GPIO.output(6, 0)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    GPIO.output(26, 0)
    time.sleep(2)

    
def input_kondisi():
    x=int(input("kondisi..."))
    if x==1 :
        #timur
        print ('timur on')
        GPIO.output(4, 0)
        GPIO.output(12, 1)
        GPIO.output(18, 1)
        GPIO.output(24, 1)
        GPIO.output(5, 0)
        GPIO.output(13, 0)
        GPIO.output(22, 0)
        GPIO.output(25, 0)
        GPIO.output(6, 1)
        GPIO.output(17, 0)
        GPIO.output(23, 0)
        GPIO.output(26, 0)
        time.sleep(10)

        GPIO.output(4, 0)
        GPIO.output(12, 1)
        GPIO.output(18, 1)
        GPIO.output(24, 1)
        GPIO.output(5, 1)
        GPIO.output(13, 0)
        GPIO.output(22, 0)
        GPIO.output(25, 0)
        GPIO.output(6, 0)
        GPIO.output(17, 0)
        GPIO.output(23, 0)
        GPIO.output(26, 0)
        for i in range(2):
            time.sleep(1)
        
    if x==2 :
        #barat
        print ('barat on')
        GPIO.output(4, 1)
        GPIO.output(12, 0)
        GPIO.output(18, 1)
        GPIO.output(24, 1)
        GPIO.output(5, 0)
        GPIO.output(13, 0)
        GPIO.output(22, 0)
        GPIO.output(25, 0)
        GPIO.output(6, 0)
        GPIO.output(17, 1)
        GPIO.output(23, 0)
        GPIO.output(26, 0)
        time.sleep(10)

        GPIO.output(4, 1)
        GPIO.output(12, 0)
        GPIO.output(18, 1)
        GPIO.output(24, 1)
        GPIO.output(5, 0)
        GPIO.output(13, 1)
        GPIO.output(22, 0)
        GPIO.output(25, 0)
        GPIO.output(6, 0)
        GPIO.output(17, 0)
        GPIO.output(23, 0)
        GPIO.output(26, 0)
        time.sleep(2)
        
    if x==3 :
        #utara
        print('utara on')
        GPIO.output(4, 1)
        GPIO.output(12, 1)
        GPIO.output(18, 0)
        GPIO.output(24, 1)
        GPIO.output(5, 0)
        GPIO.output(13, 0)
        GPIO.output(22, 0)
        GPIO.output(25, 0)
        GPIO.output(6, 0)
        GPIO.output(17, 0)
        GPIO.output(23, 1)
        GPIO.output(26, 0)
        time.sleep(10)

        GPIO.output(4, 1)
        GPIO.output(12, 1)
        GPIO.output(18, 0)
        GPIO.output(24, 1)
        GPIO.output(5, 0)
        GPIO.output(13, 0)
        GPIO.output(22, 1)
        GPIO.output(25, 0)
        GPIO.output(6, 0)
        GPIO.output(17, 0)
        GPIO.output(23, 0)
        GPIO.output(26, 0)
        time.sleep(2)

    if x==4 :
        #selatan
        print ('selatan on')
        GPIO.output(4, 1)
        GPIO.output(12, 1)
        GPIO.output(18, 1)
        GPIO.output(24, 0)
        GPIO.output(5, 0)
        GPIO.output(13, 0)
        GPIO.output(22, 0)
        GPIO.output(25, 0)
        GPIO.output(6, 0)
        GPIO.output(17, 0)
        GPIO.output(23, 0)
        GPIO.output(26, 1)
        time.sleep(10)

        GPIO.output(4, 1)
        GPIO.output(12, 1)
        GPIO.output(18, 1)
        GPIO.output(24, 0)
        GPIO.output(5, 0)
        GPIO.output(13, 0)
        GPIO.output(22, 0)
        GPIO.output(25, 1)
        GPIO.output(6, 0)
        GPIO.output(17, 0)
        GPIO.output(23, 0)
        GPIO.output(26, 0)
        time.sleep(2)


    main_loop()

def main_loop():
    try:
        while True :
            print("main loop...")
            timur()
            barat()
            utara()
            selatan()
            
    except :
        input_kondisi()
        

if __name__ == "__main__":
    init_condition()

    main_loop()
