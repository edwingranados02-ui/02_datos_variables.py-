# #CONTINUACION SEGUNDA CLASE 
# with open("productos.txt") ,"r" as archivo:

#     for linia in archivo:
#         datos= linea.strip().split(",")

#         producto = {
#            " nombre":datos [0],
#             " presio":int(datos[1])
#               [0],
           

#         }
#pra crear archivo

# with open ("estudiantes.txt","w") as archivo:
#     for i in range(3):
#     nombre = input("ingrese el nombre: ")
#     edad = int(input("ingrse la edad: "))
#     archivo.write(nombre + "," + str(edad)+ "\n")

# # # 1. Abre o crea un archivo llamado "estudiantes.txt" en modo 'w'
# # archivo = open("estudiantes.txt", "w")

# # # 2. Escribe dentro del archivo
# # archivo.write("estudianes .\n") # \n significa "salto de línea" (Enter)
# # archivo.write("Esta es la segunda línea.")

# # # 3. CIERRA el archivo (obligatorio para que los cambios se guarden)
# # archivo.close()



# # # ORIENTACION ORIENTADA EN objectos 
# # #1. Creamos la clase (El molde)

# #   class Producto:
# #     pass  # Le dice a Python: "Déjalo así, luego escribo el código"

# # # Puedes crear el objeto, pero aún no hace nada ni tiene datos
# # mause  = Producto()
# # teclado  = Producto()



# # ORIENTACION ORIENTADA EN objectos 
# #1. Creamos la clase (El molde)

#   class Producto:
#     pass  # Le dice a Python: "Déjalo así, luego escribo el código"

# # Puedes crear el objeto, pero aún no hace nada ni tiene datos
# mause  = Producto()
# teclado  = Producto()


# class Producto:
    
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio

#     # Sabes que el producto tendrá un descuento, pero no sabes la fórmula aún
#     def aplicar_descuento(self):
#         pass  # Evita que el programa falle por estar vacío

#     # Otro método que harás después
#     def actualizar_precio(self):
#         pass

# # Tu objeto sigue funcionando perfectamente
# mouse = Producto("mause", 50000)
# print(producto.nombre)


# # 1. Creamos la clase con los 3 datos requeridos
# class Producto:
    
#     def __init__(self, nombre, precio, cantidad):
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad

# # 2. Creamos un par de objetos (productos de tu tienda)
# producto_1 = Producto("mause", 50000, 15)   # Tenemos 15 mouses
# producto_2 = Producto("teclado", 85000, 5)  # Tenemos 5 teclados

# # 3. Vemos la información en pantalla
# print("Producto 1:", producto_1.nombre)
# print("Precio: , producto_1.precio)
# print("Cantidad en bodega:", producto_1.cantidad)


#metodos

















