import RPi.GPIO as GPIO
import time

ada_eplat = False
arah = 0
waktu = 0

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

def timur (detik = 0):
    global waktu
    #hijau
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

    #kuning
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

    waktu = 0


def selatan (detik = 0):
    global waktu
    #hijau
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

    #kuning
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

    waktu = 0

def barat(detik = 0):
    global waktu
    #hijau
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

    #kuning
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

    waktu = 0

def utara(detik = 0):
    global waktu
    #Hijau
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

    #Kuning
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

    waktu = 0

def input_kondisi():
    global arah
    global waktu
    global ada_eplat
    
    try:
        # cek apakah loop sudah berjalan
        if ada_eplat:
            x = arah
        else:
            ada_eplat = True
            waktu = 0
            print("Interrupt!!!")
            x=int(input("Masukkan kondisi: "))
        
        if x==1 :
            arah = 1
            timur(waktu)

        if x==2 :
            arah = 2
            selatan(waktu)
            
        if x==3 :
            arah = 3
            barat(waktu)
            
        if x==4 :
            arah = 4
            utara(waktu)

        arah = 0
        waktu = 0
        ada_eplat = False
        main_loop()
    except KeyboardInterrupt:        
        print("Ngantri boss!!")
        print "Tunggu", 10-waktu, " detik lagi!"
        print("")
        input_kondisi()
        

def main_loop():
    try:
        while True :
            print("main loop...")
            timur()
            selatan()
            barat()
            utara()

    except KeyboardInterrupt:
        input_kondisi()
    
# if __name__ == "__main__":
init_kondisi()
main_loop()
