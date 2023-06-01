import RPi.GPIO as GPIO
import time
<<<<<<< HEAD
GPIO.setmode(GPIO.BCM)
TRIG = 13
ECHO = 19
print("start")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
=======

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 13
ECHO = 19

print("start")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

>>>>>>> 0089260c9e1463d2f6d15c216311143754c0e29e
try :
    while True :
        GPIO.output(TRIG, False)
        time.sleep(0.5)
<<<<<<< HEAD
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == 0 :
            pulse_start = time.time()
            
        while GPIO.input(ECHO) == 1 :
            pulse_end = time.time()
                
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)
            
        print("Distance : ", distance, "cm")
            
except :
    GPIO.cleanup()
=======

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0 :
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1 :
            pulse_end = time.time()

        print("Distance : ", distance, "cm")

except :
    print("I'm done!")
    GPIO.cleanup()
>>>>>>> 0089260c9e1463d2f6d15c216311143754c0e29e
