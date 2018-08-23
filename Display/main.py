# Display
# Created at 2018-08-23 05:26:39.118655

import streams
from wolkabout.iot import iot
from wireless import wifi
from espressif.esp8266wifi import esp8266wifi

WIFI_SSID = "wolkabout"
WIFI_SECURITY = wifi.WIFI_WPA2
WIFI_PASSWORD = "Walkm3int0"

KEY = "whvjjf5a0yzyay9b"
PASSWORD = "505a6c04-d4be-401b-8ebe-1a627f4bb042"

pinMode(D0, OUTPUT)
pinMode(D1, OUTPUT)
pinMode(D2, OUTPUT)
pinMode(D3, OUTPUT)
pinMode(D4, OUTPUT)
pinMode(D5, OUTPUT)
pinMode(D6, OUTPUT)
pinMode(D7, OUTPUT)
pinMode(D8, INPUT)

esp8266wifi.auto_init()
wifi.link(WIFI_SSID, WIFI_SECURITY, WIFI_PASSWORD)
device = iot.Device(KEY, PASSWORD)
wolk = iot.Wolk(device)
wolk.connect()

digitalWrite(D0, HIGH)
digitalWrite(D1, HIGH)
digitalWrite(D2, HIGH)
digitalWrite(D3, LOW)
digitalWrite(D4, HIGH)
digitalWrite(D5, HIGH)
digitalWrite(D6, HIGH)

while True:
    digitalWrite(D4, LOW)
    read = digitalRead(D8)
    if read == 1:
        digitalWrite(D7, LOW)
        digitalWrite(D2, LOW)
        digitalWrite(D1, LOW)
        digitalWrite(D6, LOW)
        wolk.add_sensor_reading("N", 1)
    else:
        digitalWrite(D7, HIGH)
        digitalWrite(D2, HIGH)
        digitalWrite(D1, HIGH)
        digitalWrite(D6, HIGH)
        wolk.add_sensor_reading("N", 0)
    wolk.publish()
    sleep(1000)
    digitalWrite(D4, HIGH)
    sleep(1000)