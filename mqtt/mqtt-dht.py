import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json
import adafruit_dht
import psutil
import adafruit_dht

for proc in psutil.process_iter():
    if proc.name == 'libgpiod_pulsein':
        proc.kill()
        
dht_device = adafruit_dht.DHT22(17)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 23

GPIO.setup(LED,GPIO.OUT)

MQTT_HOST= "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60

MQTT_PUB_TOPIC = "mobile/gusdnr/sensing"
MQTT_SUB_TOPIC = "mobile/gusdnr/led"

def on_publish(client, userdata, mid):
    print("\nMessage Published...")

def on_message(client, useradta, message):
    result = str(message, patload.decode("utf-8"))
    print(f"reeived message = {result}")
    if result.upper() == "ON":
        GPIO.output(LED, GPIO.HIGH)
    if result.upper() == "OFF":
        GPIO.output(LED, GPIO.LOW)
    else:
        print("Illegal Argument")

client = mqtt.Client()
client.on_message = on_message
client.on_publish = on_publish

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.subscribe(MQTT_SUB_TOPIC)
client.loop_start()

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
        
            
            sensing = {
            "temperature":temperature,
            "humidity":humidity
            }
            value = json.dumps(sensing)
            client.publish(MQTT_PUB_TOPIC, value)
            print(value)
        except RuntimeError:
            time.sleep(2)
            continue
        
        time.sleep(20)

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")
finally:
    dht_device.exit()
    client.disconnect()