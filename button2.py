import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUTTON=24 #숫자 변경

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#인터럽트(INTERRUPT)
def my_callback(channel):
    print("Pressed the button")

GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=my_callback)


try:
    num = 1
    while True:
        print(num)
        time.sleep(1)
        num = num + 1
        

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")
finally:
    GPIO.cleanup()