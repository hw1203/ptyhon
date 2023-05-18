import paho.mqtt.client as mqtt
import time
import json

MQTT_HOST= "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60

MQTT_SUB_TOPIC = "mobile/gusdnr/sensing"

def on_message(client, userdata, message):
    result = str(message.payload.decode("utf-8"))
    sensing = json.loads(result)
    print(f"temperature = {sensing['temperature']}")
    print(f"humidity = {sensing['humidity']}")

client = mqtt.Client()
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.subscribe(MQTT_SUB_TOPIC)
client.loop_start()

try:
    while True:
        time.sleep(5)
        print("Waiting")
        
except KeyboardInterrupt:
    print("I'm done!!")
finally:
    client.disconnect
