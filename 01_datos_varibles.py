
# Pedir los datos al usuario
nombre = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el producto: ")
precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))

# Calcular el total
total = precio * cantidad

# Mostrar el resumen
print("---Resumen de la compra")
print("Nombre:", nombre)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("precio unidad:", precio)
print("Total compra:", total)
