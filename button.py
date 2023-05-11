import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUTTON=24 #숫자 변경

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        # 무한 루프 코드
        value=GPIO.input(BUTTON)
        print(value)
        time.sleep(0.1)
        

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")
finally:
    GPIO.cleanup()