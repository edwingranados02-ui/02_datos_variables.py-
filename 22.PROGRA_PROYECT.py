from machine import Pin, time_pulse_us
from time import sleep, sleep_us

# SENSOR HC-SR04
TRIG = Pin(23, Pin.OUT)
ECHO = Pin(22, Pin.IN)

# LEDS
LED_VERDE = Pin(18, Pin.OUT)
LED_ROJO = Pin(19, Pin.OUT)

# ESTADO INICIAL
TRIG.value(0)
LED_VERDE.value(0)
LED_ROJO.value(0)

# PROGRAMA PRINCIPAL
while True:

    TRIG.value(0)
    sleep_us(2)

    TRIG.value(1)
    sleep_us(10)
    TRIG.value(0)

    duracion = time_pulse_us(ECHO, 1, 30000)

    if duracion >= 0:

        distancia = (duracion * 0.0343) / 2

        if distancia >= 10:
            LED_VERDE.on()
            LED_ROJO.off()
            estado = "ZONA SEGURA"

        else:
            LED_VERDE.off()
            LED_ROJO.on()
            estado = "OBJETO CERCANO"

        print("Distancia: {:.1f} cm - {}".format(distancia, estado))

    else:
        LED_VERDE.off()
        LED_ROJO.off()
        print("Sin lectura")

    sleep(0.2)