import time
import adafruit_dht
import psutil
import board

for proc in psutil.process_iter():
    if proc.name == 'libgpiod_pulsein':
        proc.kill()

dht_device = adafruit_dht.DHT22(board.D27, use_pulseio=False)

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
        
            print(temperature)
            print(humidity)
        except RuntimeError:
            time.sleep(2)
            continue
        time.sleep(2)

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")
finally:
    dht_device.exit()