import pandas as pd  # Importa pandas para trabajar con tablas.

datos = {  # Crea un diccionario con los datos.
    "Medicion": [1, 2, 3, 4, 5],  # Numera las mediciones.
    "Distancia": [15, 18, 22, 12, 30]  # Guarda las distancias medidas.
}  # Termina el diccionario.

tabla_datos = pd.DataFrame(datos)  # Convierte el diccionario en una tabla.
print(tabla_datos)  # Muestra la tabla completa.

print(tabla_datos["Distancia"])  # Muestra la columna de distancias.
promedio = tabla_datos["Distancia"].mean()  # Calcula el promedio de las distancias.
print(promedio)  # Muestra el promedio.

distancia_max = tabla_datos["Distancia"].max()  # Busca la distancia más alta.
print(distancia_max)  # Muestra la distancia más alta.

filas_altas = tabla_datos[tabla_datos["Distancia"] > 20]  # Selecciona distancias mayores que 20.
print(filas_altas)  # Muestra las filas seleccionadas.

tabla_datos["Distancia Doble"] = tabla_datos["Distancia"] * 2  # Agrega una columna con las distancias duplicadas.
print(tabla_datos)  # Muestra la tabla actualizada.