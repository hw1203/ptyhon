import paho.mqtt.client as mqtt
import time
import json

MQTT_HOST= "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60

MQTT_PUB_TOPIC = "mobile/gusdnr/sensing"

client = mqtt.Client()

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start()

try:
    while True:
        time.sleep(10)
        #dht sensor
        humidity, temperature = 80, 30
        sensing = {
            "temperature":temperature,
            "humidity":humidity
            }
        value = json.dumps(sensing)
        client.publish(MQTT_PUB_TOPIC, value)
        print(value)
    
except KeyboardInterrupt:
    print("I'm done!!")
finally:
    client.disconnect