
  #PARTE B

lista_equipos = []

# Pedir los datos y guardarlos en el archivo
with open("equipos.txt", "w") as archivo:
    for numero_equipo in range(4):
        print("\nEquipo", numero_equipo + 1)

        nombre = input("Nombre del equipo: ")
        cantidad = int(input("Cantidad disponible: "))
        valor_unitario = float(input("Valor unitario: "))

        equipo = Equipo(nombre, cantidad, valor_unitario)
        lista_equipos.append(equipo)
        

        archivo.write(
            equipo.nombre + ","
            + str(equipo.cantidad) + ","
            + str(equipo.valor_unitario) + "\n"
        )

# Leer el archivo y calcular los valores
valor_total_general = 0

with open("equipos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")

        nombre = datos[0]
        cantidad = int(datos[1])
        valor_unitario = float(datos[2])

        equipo = Equipo(nombre, cantidad, valor_unitario)
        valor_total = equipo.calcular_valor_total()

        valor_total_general = valor_total_general + valor_total

        if valor_total > 200000:
            print("\nEquipo:", equipo.nombre)
            print("Valor total: $", valor_total)

print("\nValor total de todos los equipos: $", valor_total_general)






# #PARTE C. POO 
# class dispósitivos:
#     def __init__(self, nombre, marca, precio):
#         self.nombre = nombre
#         self.marca = marca
#         self.precio = precio

#     def calcular_descuento(self):
#        return self.presio * 0.3
#     print()
    


    
# CLASE SENSOR
# class sensor:
#     def __init__(self, nombre, marca, precio):
#         self.nombre = nombre
#         self.marca = marca
#         self.precio = precio

#     def calcular_descuento(self):
#        return self.presio * 0.3
#     print()
    