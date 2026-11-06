import serial                                         # Permite comunicar Python con el ESP32 por puerto serial
from time import sleep                                    # Permite hacer una pausa
  # El ESP32 debe estar conectado a COM10 y usar la misma velocidad.
puerto = serial.Serial("COM10", 115200)

sleep(3)  

puerto.reset_input_buffer()  # Limpia datos antiguos que hayan quedado en el puerto

while True:
    # Pide escribir ENCENDER o APAGAR
    
    mensaje = input("Digite ENCENDER o APAGAR: ")

    # Agrega un salto de línea, convierte el mensaje a bytes y lo envía al ESP32
    puerto.write((mensaje + "\n").encode())



    