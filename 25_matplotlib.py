import pandas as pd  # Importa pandas para leer los datos del archivo CSV.
import matplotlib.pyplot as plt  # Importa las herramientas para crear gráficos.

tabla = pd.read_csv("distancias.csv")  # Carga los datos del archivo en una tabla.

plt.plot(tabla["Medicion"], tabla["Distancia"])  # Grafica la distancia de cada medición.
plt.xlabel("Medicion")  # Nombra el eje horizontal.
plt.ylabel("Distancia")  # Nombra el eje vertical.
plt.title("Distancias medidas por el KC-SRM")  # Agrega un título al gráfico.
plt.show()  # Muestra el gráfico.