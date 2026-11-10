from machine import Pin, time_pulse_us
from time import sleep, sleep_us
import sys
import select

trig = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
led = Pin(2, Pin.OUT)

led.value(0)

while True:
    trig.value(0)
    sleep_us(2)

    trig.value(1)
    sleep_us(10)
    trig.value(0)

    tiempo = time_pulse_us(echo, 1, 30000)

    if tiempo > 0:
        distancia = tiempo / 58
        print(round(distancia, 1))

    if select.select([sys.stdin], [], [], 0)[0]:
        comando = sys.stdin.readline().strip()

        if comando == "ENCENDER":
            led.value(1)
        elif comando == "APAGAR":
            led.value(0)

    sleep(0.5)