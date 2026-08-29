
# Pedir los datos al usuario
nombre = input("Nombre: ")
edad = int(input("Edad: "))
temperatura = float(input("Temperatura corporal: "))
nota = float(input("Nota de capacitación (0.0 a 5.0): "))
carnet_input = input("¿Tiene carnet? (escriba exactamente si o no): ")

# Calcular variables booleanas 
mayor_edad = edad >= 18
temp_adecuada = temperatura <= 37.5
cap_aprobada = nota >= 3.0
tiene_carnet = carnet_input == "si"

# Condición general del ejercicio
cumple_requisitos = mayor_edad and temp_adecuada and cap_aprobada and tiene_carnet

#  Resultados
print("nombre:", nombre)
print("mayor_edad:", mayor_edad)
print("temp_adecuada:", temp_adecuada)
print("cap_aprobada:", cap_aprobada)
print("tiene_carnet:", tiene_carnet)
print("cumple_requisitos:", cumple_requisitos)