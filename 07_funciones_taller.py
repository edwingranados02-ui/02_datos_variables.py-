# def presentar (nombre,edad):
#     print("Nombre",nombre)
#     print("Edad",edad)
#  presentar (lauar,33):

# def sumar (a,b):
#     print(a+b)
#     resultado=sumar(5+2)



# def multiplicar  (a,b):
#     return a*b
# resultado=multiplicar(4,5)+10
# print (resultado)

# def calcular_promedio(notas):
#     suma=0
#     for nota in notas :
#         suma +=nota
#     return suma /len(notas)
# notas_ana =[4.0,3.5,5.0]
# promedio =calcular_promedio(notas_ana)
# print(round(promedio,2))


# def calcular():
#     resultado =20
#     print(resultado)

# calcular()
# print(resultado)


# nombre="lauara "
# def saludar():
#     print(nombre)
#     saludar()

# contador =10
# def aumentar ():
#     contador=contador+1
#     print(contador)

#  aumentar ()

# def aumentar (numero):
#     retur numero +1
#     contador =10
#     contador =aumentar(contador)
#     print(contador)

#    # ejercicio 
# def calcular_total(precio,cantidad ):
#     return precio*cantidad 

# producto={
#     "nombre":"teclado",
#     "precio":80000,
#     "cantidad":3

# }
# producto["total"]=calcular_total(
#     producto["precio"],
#     producto["cantidad"]

# )
# print (producto)


#correccion de codigo 

# taller de clase






def calcular_promedio(notas):
    promedio =sum(notas)/len(notas)
    return promedio
estudiantes=[
    {"nombre":"ana","notas":[4.0,3.5,5.0]},
    {"nombre":"luis","notas":[2.5,3.0,2.8]},
    {"nombre":"carlos","notas":[4.5,4.0,4.8]},
      ]

promedio =calcular_promedio(estudiantes[1]["notas"])
print (promedio)

for estudiante in estudiantes:
    promedio =calcular_promedio(estudiantes["notas"])
    if promedio >3:
        estado  =("aprobado")
    else:
      estado = ("no aprobado" )

    estudiante ["promedio"]=promedio
    estudiante ["estado"] =estado
print (estudiantes)


