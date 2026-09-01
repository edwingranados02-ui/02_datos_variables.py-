# ("contraseña incorrecta")

# edad = 25
# matricula ="si "
# contraseña ="azul" 

# if edad<18:
#     print("acceso restingido " )
# else:
#     if  matricula==("si"):
#         if contraseña== "azul":
#             print("BIENVENIDO")
#         else :
#             print("contraseña incorrecta")
#     else:
#         print("marticula  ")("contraseña incorrecta")

# edad = 25
# matricula ="si "
# contraseña ="azul" 

# if edad<18:
#     print("acceso restingido " )
# else:
#     if  matricula==("si"):
#         if contraseña== "azul":
#             print("BIENVENIDO")
#         else :
#             print("contraseña incorrecta")
#     else:
#         print("marticula  ")



# Nombre = input("Nombre: ")
# Edad = int(input("Edad: "))
# tiene_invitacion = input("¿Tiene invitación? (si/no): ")
# invitacion= tiene_invitacion.lower() 
# if Edad >= 18 and tiene_invitacion == "si":
#       print("Autorizado ", Nombre)
# elif Edad <= 18:
#      print("acceso denegado, ", Nombre)
# else:
#          print("Necesita invitación, ", Nombre)


# numero =1
# while  numero <=3:

#     print(numero )

# contraseña = ""
# intentos = 0
# "while contraseña! = "python" and intentos < 3:
# contraseña = input("Contraseña: ")
# intentos = intentos + 1

# if contraseña == "python":
#     print("Acceso autorizado")
# else:
#     print("Acceso bloqueado")





pin_correcto = "2580"
max_intentos = 3
intentos = 0
while intentos < max_intentos:
    pin_ingresado = input("Ingrese el PIN: ")
    if pin_ingresado == pin_correcto:
        print("Acceso autorizado")
        intentos +=1
    else:
        print("PIN incorrecto")
        intentos += 1