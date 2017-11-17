import RPi.GPIO as GPIO
import time

arah = 0
waktu = 0
antrian_a = []
antrian_b = []
antrian_c = []
antrian_d = []

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
    global waktu
    global arah
    
    arah = 2
    
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

        waktu = 0

def timur_kuning (detik = 0):
    global waktu
    global arah
    
    arah = 2
    
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

def selatan_hijau (detik = 0):
    global waktu
    global arah
    
    arah = 1
    
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

        waktu = 0

def selatan_kuning (detik = 0):
	global waktu
	global arah
	
	arah = 1
	
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

def barat_hijau (detik = 0):
    global waktu
    global arah
    
    arah = 3
    
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

        waktu = 0

def barat_kuning (detik = 0):
    global waktu
    global arah
    
    arah = 3
    
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

def utara_hijau(detik = 0):
    global waktu
    global arah
    
    arah = 4
    
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

        waktu = 0

def utara_kuning(detik = 0):
	global waktu
	global arah
	
	arah = 4
	
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
        input_kondisi()
    
if __name__ == "__main__":
	# keterangan arah
	# 1: selatan
	# 2: timur
	# 3: Barat
	# 4: utara
	
	init_kondisi()
	main_loop()
