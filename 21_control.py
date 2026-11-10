import serial
from time import sleep

# Abre la conexión serial con el ESP32
# Usa la misma velocidad configurada en la placa: 115200 baudios
puerto = serial.Serial("COM3", 115200, timeout=1)

# Espera a que el ESP32 se conecte y limpia los datos recibidos
sleep(2)
puerto.reset_input_buffer()

while True:
    # Lee una línea que envía el ESP32 y quita espacios y saltos de línea
    dato = puerto.readline().decode().strip()

    try:
        # Convierte la distancia recibida a número
        distancia = float(dato)
        print(f"Distancia: {distancia} cm")

        # Enciende el LED si algo está a menos de 50 cm
        if distancia < 50:
            puerto.write(b"ENCENDER\n")
        else:
            # Si está a 50 cm o más, apaga el LED
            puerto.write(b"APAGAR\n")

    except ValueError:
        # Ignora líneas vacías o datos que no sean números
        pass   #dd