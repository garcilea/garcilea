"""
Ejercicio Integrador 01

carga de 5 productos

La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
  
 Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ítem con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.
"""


tipo_producto = " "
precio = 0
cantidad_unidades = 0
marcfabricante = " "

marca_barbijo_caro = ""
precio_barbijo_caro = -1
cantidad_barbijo_caro = ""
fabricante_barbijo_caro = ""

item_masunidades = " "
fabricante_mas_unidades = ""

cantidad_jabones = 0



for iteracion in range(5):

 

    tipo_producto = input("Ingrese el tipo de  producto (jabon, barbijo, alcohol): ")

    while tipo_producto != "jabon" and tipo_producto != "barbijo" and tipo_producto != "alcohol":
        tipo_producto = input("Ingrese el tipo de  producto (jabon, barbijo, alcohol): ")
    
    
  # version do while
    while (True):

        precio = int(input("Por favor ingrese el precio : "))

        if precio >= 100 and precio <= 300:
            break
    
    while (True):

        cantidad = int(input("Por favor ingrese la cantidad : "))

        if cantidad >0 and cantidad < 1000:
            break
    
    

    marca = input("Por favor ingrese la marca : ")

    fabricante = input("Por favor ingrese fabricante : ")

    if tipo_producto == "barbijo":

        if precio > precio_barbijo_caro:
            precio_barbijo_caro = precio
            cantidad = cantidad_barbijo_caro
            fabricante = fabricante_barbijo_caro
    elif tipo_producto == "jabon":
        cantidad_jabones += cantidad
        
    if cantidad > item_masunidades:
        item_masunidades = cantidad
        fabricante_mas_unidades = fabricante

print("barbijos mas caro hay : ", cantidad_barbijo_caro, " y lo fabrican : ", fabricante_barbijo_caro)
print("el item con mas unidades lo fabrica : ", fabricante_mas_unidades)
print("jabones hay un total de :", cantidad_jabones)

print("Fin del programa")
        



        
    

             

   
    

