# print(lista[0]) ----> imprime el primer elem de la lista ( que es un dicc )
# print(lista[0]['title']) ----> accedo al 1er eelem del dicc por su nombre
# a la lista accedemos por los sub indice
# al dicc siempre accedemos por el nombre del key
# puedo guardar en una variable la lista, entonces accedo a la lista mas facil
# tema mas visto ----> estrategia : creo una variable donde el maximo o minimo  es el primer elemento
# cantidad ---> len(lista) para saber cuantos son

from data_stark import lista_personajes
"""
minimo_altura = float(lista_personajes[0]["altura"])
acumulador_altura = 0
altura_promedio = 0
len_altura = len(lista_personajes)
nombre_bajo = ""
nombre_mas_pesado = ""
nombre_menos_pesado = ""
maximo_peso = float(lista_personajes[0]["peso"])
min_peso = float(lista_personajes[0]["peso"])


for superheroe in lista_personajes:
    superheroe["altura"] = float(superheroe["altura"])
    superheroe["peso"] = float(superheroe["peso"])
    # punto b
    #print(superheroe["nombre"])
    # punto c
    nombre_altura = "el nombre del superheroe es {0} y su altura es {1:.2f}".format(superheroe["nombre"],superheroe["altura"])
    print(nombre_altura)
    
    # punto d
    if (superheroe["altura"]) > (maximo_altura):
        maximo_altura = superheroe["altura"]
        nombre_alto = superheroe["nombre"]
    # punto e
    if (superheroe["altura"] < minimo_altura):
        minimo_altura = superheroe["altura"]
        nombre_bajo = superheroe["nombre"]
      
    # punto f altura promedio
    acumulador_altura += superheroe["altura"]
    altura_promedio = "La altura promedio es {0:.2f} ".format((acumulador_altura/len_altura))

    # Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    # -----> esta dentro del maximo y minimo

    # Calcular e informar cual es el superhéroe más y menos pesado
    if ( superheroe["peso"] > maximo_peso):
        maximo_peso = superheroe["peso"]
        nombre_mas_pesado = superheroe["nombre"]
    if ( superheroe["peso"] < min_peso):
        min_peso = superheroe["peso"]
        nombre_menos_pesado = superheroe["nombre"]
        
maximo_altura = "la altura maxima es {0} mts".format(maximo_altura) 
minimo_altura = "la altura minima es {0:.2f} mts".format(minimo_altura) 
nombre_alto = "El nombre del superheroe mas alto es {0} ".format(nombre_alto)
nombre_bajo = "El nombre del superheroe mas bajo es {0} ".format(nombre_bajo)
nombre_mas_pesado = "El nombre mas pesado es {0}".format(nombre_mas_pesado)
nombre_menos_pesado = "El nombre menos pesado es {0}".format(nombre_menos_pesado)

print(maximo_altura)
print(minimo_altura)
print(altura_promedio)
print(nombre_alto)
print(nombre_bajo)
print(nombre_mas_pesado)
print(nombre_menos_pesado)
"""


def imprime_nombre_superheore():
    for superheroe in lista_personajes:
        print(superheroe['nombre'])


def imprime_nombre_y_altura_heroe():
    for superheroe in lista_personajes:
        print("el nombre del superheroe es {0} y su altura es {1:.2f}".format(superheroe["nombre"],float(superheroe["altura"])))

def determina_nombre_superheroe_mas_alto():
    maximo_altura = float(lista_personajes[0])
    nombre_alto = ""
    for superheroe in lista_personajes:
        
        if(float(superheroe["altura"]) > maximo_altura['altura']):
            maximo_altura = superheroe
            nombre_alto = superheroe

    print("El nombre del superheroe mas alto es {1} y su altura es {0} mts".format(maximo_altura["altura"], nombre_alto['nombre']))

def determina_nombre_superheroe_mas_bajo():
    minimo_altura = float(lista_personajes[0])
    nombre_bajo = ""
    for superheroe in lista_personajes:
        if(float(superheroe["altura"]) < minimo_altura["altura"]):
            minimo_altura = superheroe
            nombre_bajo = superheroe

    print("El nombre del superheroe mas bajo es {1} y su altura  es {0:.2f} mts".format(minimo_altura["altura"], nombre_bajo["nombre"]))

def determina_altura_promedio():
    len_altura = len(lista_personajes)
    acumulador_altura = 0
    for superheroe in lista_personajes:
        acumulador_altura += float(superheroe["altura"])
    print("La altura promedio es {0:.2f} ".format((acumulador_altura/len_altura)))

def determina_peso_y_nombre_heroe_mas_pesado():
    nombre_mas_pesado = ""
    maximo_peso = float(lista_personajes[0])
    for superheroe in lista_personajes:
        
        if(float(superheroe["peso"]) > maximo_peso["peso"]):
            maximo_peso = superheroe
            nombre_mas_pesado = superheroe
    print("El nombre del superheoroe mas pesado es {0} y su peso es {1}".format(nombre_mas_pesado["nombre"], maximo_peso["peso"]))

def determina_peso_y_nombre_heroe_menos_pesado():
    nombre_menos_pesado = ""
    minimo_peso = float(lista_personajes[0])
    for superheroe in lista_personajes:
        
        if(float(superheroe["peso"]) < minimo_peso["peso"]):
            minimo_peso = superheroe
            nombre_menos_pesado = superheroe
    print("El nombre del superheoroe menos pesado es {0} y su peso es {1}".format(nombre_menos_pesado["nombre"], minimo_peso["peso"]))

while True:
    respuesta = input("\n1 - nombre de todos los superheroes\n2 - muestra el nombre y altura de cada superheroe\n3 - Nombre y altura superheroe mas alto\n4 - Nombre y altura superheroe mas alto\n5 - altura promedio\n6 - Nombre heroe mas pesado\n7 - Nomre heroe menos pesado\n8 - Salir\n\n> ")
    if(respuesta == "1"):
        imprime_nombre_superheore()   
    elif(respuesta == "2"):
        imprime_nombre_y_altura_heroe()
    elif(respuesta == "3"):
        determina_nombre_superheroe_mas_alto()
    elif(respuesta == "4"):
        determina_nombre_superheroe_mas_bajo()
    elif(respuesta == "5"):
        determina_altura_promedio()
    elif(respuesta == "6"):
        determina_peso_y_nombre_heroe_mas_pesado()
    elif(respuesta == "7"):
        determina_peso_y_nombre_heroe_menos_pesado()  
    elif(respuesta == "8"):
        break

    




        








    





