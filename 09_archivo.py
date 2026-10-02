# with open(saludo.txt ,"r") as archivo
#     texto= archivos.read ()
#  print(texto)



 #with open("datos.txt ,"w") as archivo:
#     texto= archivos.write ()
#  print(texto)



# agregar

#with open("registro.txt" ,"w") as archivo:
  #  archivo.write("ana/n")
   # with open("registro.txt" ,"a") as archivo:
       # archivo.write("luis/n")
       # archivo.write("carlos/n")
#with open("registro.txt","r") as archivo:
   # for linia in archivo:
        #print(linia.strip())# elimina saltos de linia y espacios

# with open("edades.txt","r") as archivo:
#     for linia in archivo:
#         edad=int(linia.strip())
#         print(edad +5)
# with open("registro.txt" ,"a") as archivo:
#         archivo.write("20/n")
#        archivo.write("30/n")
# with open("registro.txt","r") as archivo:
#     for linia in archivo:
#         print(linia.strip())

# with

#  open("registro.txt", "r") as archivo:
#     datos = archivo.readlines 
#   print()


# productos = ["Mouse","Teclado","Monitor"]
# with open (productos.txt , "w") as archivo:
#         for producto in productos :
#             archivo.write(producto + "\n")

#nombres = ["ana","luis","carlos"]
#with open (nombres.txt , "w") as archivo:
           # archivo.write(nombres)
            

# productos =[
#     {"nombre:"mouse","presio":50000, "catidad":5},
#     {"nombre:"teclado","presio":80000, "catidad":3}
# ]
# with open (productos.txt , "w") as archivo :
#     for producto in productos :
#     archivos.write(producto["nombres"])+","

linia = "tecldo,8000,3"
datos = linia.strip().split(",")

nombre =datos [0]
precio = int(datos [1])
cantidad =int(datos [2])
total= precio * cantidad
print(total)