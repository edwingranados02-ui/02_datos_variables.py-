# class Producto:
#     def __init__(self, nombre, cantidad):
#         self.nombre = nombre
       
#         self.cantidad = cantidad

#         def agregar _stock(self, unidades):
#         if unidades <= self.cantidad:
#             self.cantidad -= unidades


#             class Producto:
#     def __init__(self, nombre, cantidad):
#         self.nombre = nombre
#         self.cantidad = cantidad
#         def agregar_stok (self,unidades):

#         # Crear un objeto
# Celular = Producto("Celular", 2)
# Celular.agregar_stok(5)
# print(Celular.cantidad)


#                                                                                   #CREAR 3 OBJETOS

# producto2 = Producto("teclado", 20)
# producto3 = Producto("mause", 15)
# producto4 = Producto("monitor", 8)

# mause.agregar_stok(4)

# print(teclado.nombre, producto2.cantidad)
# print(monitor.nombre, producto3.cantidad)
# print(producto4.nombre, producto4.cantidad)





# class Producto:
#     def __init__(self, nombre, presio):
#         self.nombre = nombre
       
#         self.cantidad =presio


#         def agregar _stock(self, unidades):
#         return self.presio*cantidad

#             class Producto:
#     def __init__(self, nombre, cantidad):
#         self.nombre = nombre
#         self.cantidad = cantidad
#         def agregar_stok (self,unidades):

#         # Crear un objeto
# Celular = Producto("Celular", 2)
# Celular.agregar_stok(5)
# print(Celular.cantidad)


# class Producto:
#     def __init__(self, precio):
#         self.nombre = nombre
#         self.precio = precio
#         self.stock = 0

#     def agregar_stock(self, cantidad):
#         self.stock += cantidad

#     def calcular_total(self, cantidad):
#         return self.precio * cantidad


#                                                               # Crear productos
# celular = Producto("Celular", 20000)
# teclado = Producto("Teclado", 15000)
# mouse = Producto("Mouse", 5000)
# monitor = Producto("Monitor", 25000)



                                                               
# mouse.calcular_total(5) 


# print(mouse.calcular_total(7)


# class Producto:
#     def __init__(self, nombre, precio, cantidad):  #parametros
#         self.nombre = nombre    # tomas la posiciondel objetos   
#         self.precio = precio
#         self.cantidad = cantidad

#     def mostrar_datos(self):
#         return f"{self.nombre} - {self.precio} - {self.cantidad}"                   # metodos

#     def calcular_total(self):
#         return self.precio * self.cantidad







# class Producto:
#     def __init__(self, nombre, precio, cantidad):
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad

#     def mostrar_datos(self):
#         return f"{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad}"

#     def calcular_total(self):
#         return self.precio * self.cantidad

#     def agregar_stock(self, cantidad):
#         self.cantidad += cantidad


#                                                              # 1. Crear tres objetos
# mouse = Producto("Mouse", 50000, 3)
# teclado = Producto("Teclado", 80000, 2)
# monitor = Producto("Monitor", 700000, 1)

#                                                          # 2. Mostrar los datos
# print(mouse.mostrar_datos())
# print(teclado.mostrar_datos())
# print(monitor.mostrar_datos())

#                                                      # 3. Calcular el total de cada producto
# print("Total del mouse:", mouse.calcular_total())
# print("Total del teclado:", teclado.calcular_total())
# print("Total del monitor:", monitor.calcular_total())

#                                                    # 4. Agregar 2 unidades al stock del mouse
# mouse.agregar_stock(2)

#                                                     # Comprobar las cantidades después del cambio
# print("Después de agregar stock:")
# print(mouse.mostrar_datos())
# print(teclado.mostrar_datos())
# print(monitor.mostrar_datos())          





       #RETO FINAL 


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("Depósito realizado.")
        else:
            print("El depósito debe ser positivo.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("El retiro debe ser positivo.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print("Retiro realizado.")

    def consultar_saldo(self):
        return self.saldo

    def mostrar_datos(self):
        return f"Titular: {self.titular} - Saldo actual: {self.saldo}"


# Crear dos cuentas
cuenta1 = CuentaBancaria("Carlos", 100000)
cuenta2 = CuentaBancaria("Ana", 50000)

# Probar operaciones
cuenta1.depositar(50000)
cuenta1.retirar(30000)
cuenta2.retirar(60000)  # Se rechaza: Ana solo tiene $50 000

# Mostrar los saldos finales
print(cuenta1.mostrar_datos())
print(cuenta2.mostrar_datos())
            
            
            

    