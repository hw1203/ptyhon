import RPi.GPIO as GPIO
import time
import adafruit_dht
import psutil
import board

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein':
        proc.kill()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 23  # 숫자 변경
buzzer_pin = 12
dht_device = adafruit_dht.DHT22(board.D27, use_pulseio=False)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

scale = [523]  # 음계입력
note_list = [0]  # 음계조합
term = [0.5]  # 음길이 조합

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            
            print(temperature)
            print(humidity)
        except RuntimeError:
            time.sleep(2)
        
        if temperature >= 25:
            print("On")
            for _ in range(3):
                GPIO.output(LED, GPIO.HIGH)
                p = GPIO.PWM(buzzer_pin, 100)
                p.start(100)
                p.ChangeDutyCycle(90)
                for i in range(len(note_list)):
                    p.ChangeFrequency(scale[note_list[i]])
                    time.sleep(term[i])
                p.stop()
                GPIO.output(LED, GPIO.LOW)
                time.sleep(0.5)
            print("Temperature:", temperature)
            print("Humidity:", humidity)
        else:
            print("Off")
            GPIO.output(LED, GPIO.LOW)
        
        time.sleep(1)
            
except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")
finally:
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()