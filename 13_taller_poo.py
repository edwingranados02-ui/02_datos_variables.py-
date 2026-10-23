
lista = []

# Registrar los cuatro equipos y guardarlos en el archivo
with open("equipos.txt", "w") as archivo:
    for i in range(4):
        print("\nEquipo", i + 1)

        nombre = input("Nombre del equipo: ")
        cantidad = int(input("Cantidad disponible: "))
        valor_unitario = float(input("Valor unitario: "))

        equipo = {
            "nombre": nombre,
            "cantidad": cantidad,
            "valor_unitario": valor_unitario
        }

        lista.append(equipo)

        archivo.write(
            equipo["nombre"] + ","
            + str(equipo["cantidad"]) + ","
            + str(equipo["valor_unitario"]) + "\n"
        )

# Leer el archivo y calcular los valores

total_general = 0

print("\nEquipos con valor total superior a $2.000.000:")

with open("equipos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")

        nombre = datos[0]
        cantidad = int(datos[1])
        valor_unitario = float(datos[2])

        valor_total = cantidad * valor_unitario
        total_general = total_general + valor_total

        if valor_total > 2000000:
            print("Equipo:", nombre)
            print("Valor total: ", valor_total)

print("\nValor total de todos los equipos: ", total_general)

  
