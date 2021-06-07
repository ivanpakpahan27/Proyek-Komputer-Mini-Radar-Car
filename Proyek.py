# Libraries
import RPi.GPIO as GPIO
import time

# Setting mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setting variabel & Input/Output
GPIO.setup(17,GPIO.OUT)
servo1 = GPIO.PWM(17,50) #17 adalah pin GPIO, 50 = 50Hz pulsa
TRIG = 25 
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

Ena,In1,In2,Enb,In3,In4 = 2,3,4,21,16,20
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)
pwmA = GPIO.PWM(Ena,100)
pwmA.start(0)
pwmB = GPIO.PWM(Enb,100)
pwmB.start(0)

print ("Waiting for 2 seconds")
time.sleep(2)

# Pembaca Jarak
while True:

    def Mundur():
        GPIO.output(In1, GPIO.HIGH)
        GPIO.output(In2, GPIO.LOW)
        pwmA.ChangeDutyCycle(50)
        
        GPIO.output(In3, GPIO.LOW)
        GPIO.output(In4, GPIO.HIGH)
        pwmB.ChangeDutyCycle(50)

    def ManuverKiri():
        GPIO.output(In1, GPIO.LOW)
        GPIO.output(In2, GPIO.HIGH)
        pwmA.ChangeDutyCycle(100)

        GPIO.output(In3, GPIO.LOW)
        GPIO.output(In4, GPIO.HIGH)
        pwmB.ChangeDutyCycle(25)
        print('Manuver Kiri')

    def ManuverKanan():
        GPIO.output(In1, GPIO.HIGH)
        GPIO.output(In2, GPIO.LOW)
        pwmA.ChangeDutyCycle(25)

        GPIO.output(In3, GPIO.HIGH)
        GPIO.output(In4, GPIO.LOW)
        pwmB.ChangeDutyCycle(100)
        print('Manuver Kanan')

    # Variabel duty
    duty = 2
    # Konfigurasi PWM servo
    servo1.start(0)
    
    GPIO.setmode(GPIO.BCM)
    TRIG = 25 
    ECHO = 24
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    #-------------------Maju----------------------------
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwmA.ChangeDutyCycle(100)

    GPIO.output(In3, GPIO.HIGH)
    GPIO.output(In4, GPIO.LOW)
    pwmB.ChangeDutyCycle(100)
    #---------------------------------------------------

    print("Jarak: ",distance,"cm")
    if distance <=15 :
        #-------------------Mundur--------------------------
        Mundur()
        time.sleep(0.5)
        #---------------------------------------------------
        
        #-------------------Stop----------------------------
        GPIO.output(In1, GPIO.LOW)
        GPIO.output(In2, GPIO.HIGH)
        pwmA.ChangeDutyCycle(0)

        GPIO.output(In3, GPIO.HIGH)
        GPIO.output(In4, GPIO.LOW)
        pwmB.ChangeDutyCycle(0)
        #---------------------------------------------------

        # Netral
        print ("Netral")
        servo1.ChangeDutyCycle(7)
        time.sleep(2)
        GPIO.output(TRIG, False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
              
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        Jarak_Depan = distance
        print("Jarak Depan : ",Jarak_Depan)
        time.sleep(1)

        # Kanan
        print ("90 derajat Kanan")
        servo1.ChangeDutyCycle(2)
        time.sleep(2)
        GPIO.output(TRIG, False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
            
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
              
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        Jarak_Kanan = distance
        print("Jarak Kanan : ",Jarak_Kanan)
        time.sleep(1)

        # Netral
        print ("Netral")
        servo1.ChangeDutyCycle(7)
        time.sleep(2)
        GPIO.output(TRIG, False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
              
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        Jarak_Depan = distance
        print("Jarak Depan : ",Jarak_Depan)
        time.sleep(1)

        # Kiri
        print ("90 derajat Kiri")
        servo1.ChangeDutyCycle(12)
        time.sleep(2)
        GPIO.output(TRIG, False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
            
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
              
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        Jarak_Kiri = distance
        print("Jarak Kiri : ",Jarak_Kiri)
        time.sleep(1)

        # Netral
        print ("Netral")
        servo1.ChangeDutyCycle(7)
        time.sleep(2)
        GPIO.output(TRIG, False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
              
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        Jarak_Depan = distance
        print("Jarak Depan : ",Jarak_Depan)
        time.sleep(1)

        if Jarak_Kiri > Jarak_Kanan:
            # Manuver Kiri
            #--------------------------------------------------
            ManuverKiri()
            time.sleep(0.5)
            #---------------------------------------------------
        else:
            # Manuver Kanan
            #--------------------------------------------------
            ManuverKanan()
            time.sleep(0.5)
            #---------------------------------------------------
