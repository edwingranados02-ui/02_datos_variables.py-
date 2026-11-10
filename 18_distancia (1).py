from machine import Pin, time_pulse_us  # Control de pines y medición de pulsos
from time import sleep, sleep_us         # Pausas en segundos y microsegundos

trig = Pin(18, Pin.OUT)  # Pin de salida que envía el pulso del sensor
echo = Pin(19, Pin.IN)   # Pin de entrada que recibe el pulso de regreso

while True:  # Repite la medición continuamente
    trig.value(0)  # Asegura que el pin TRIG empiece apagado
    sleep_us(2)    # Espera 2 microsegundos

    trig.value(1)  # Envía el pulso de activación
    sleep_us(10)   # Mantiene el pulso durante 10 microsegundos
    trig.value(0)  # Termina el pulso

    # Mide cuánto tarda en llegar el eco; 30000 es el tiempo máximo de espera
    tiempo = time_pulse_us(echo, 1, 30000)

    if tiempo > 0:  # Comprueba que se haya recibido el eco
        distancia = tiempo / 58  # Convierte el tiempo del eco a centímetros
        print(round(distancia, 1))  # Muestra la distancia con un decimal
    else:
        print("Sin medición válida")  # Informa si no se recibió el eco

    sleep(1)  # Espera un segundo antes de medir otra vez