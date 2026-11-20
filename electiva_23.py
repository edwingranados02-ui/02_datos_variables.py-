import numpy as np  # Importa NumPy y le asigna el nombre abreviado np.

temperaturas = np.array([26, 28, 31, 29, 25, 33, 27])  # Crea un arreglo con las temperaturas.

temp_aumentadas = temperaturas + 2  # Suma 2 grados a cada temperatura.
promedio = np.mean(temperaturas)  # Calcula el promedio de las temperaturas.
temp_max = np.max(temperaturas)  # Busca la temperatura más alta.
temp_min = np.min(temperaturas)  # Busca la temperatura más baja.

print(temp_aumentadas)  # Muestra las temperaturas con 2 grados añadidos.
print(promedio)  # Muestra el promedio.
print(temp_max)  # Muestra la temperatura máxima.
print(temp_min)  # Muestra la temperatura mínima.
print(temperaturas[0])  # Muestra el primer valor del arreglo (índice 0).
print(temperaturas[6])  # Muestra el séptimo valor del arreglo (índice 6).

temp_bajas = temperaturas[temperaturas < 28]  # Selecciona las temperaturas menores que 28.
print(temp_bajas)  # Muestra las temperaturas seleccionadas.




