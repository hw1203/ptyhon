import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED=23 #숫자 변경

GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        # 무한 루프 코드
        print("On")
        GPIO.output(23, GPIO.HIGH)
        time.sleep(1)
        print("Off")
        GPIO.output(23, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")
finally:
    GPIO.output(23, GPIO.LOW)
    GPIO.cleanup()