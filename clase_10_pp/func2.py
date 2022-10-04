import json

import re

def cargar_json(path:str)->list[dict]:
    """
    carga el json y lo abre en modo lectura para utilizarlo, tambien lo cierra.
    Recibe como parametro la ruta del archivo
    retorna los diccionarios dentro de la lista que estaba en el json
    """
    buffer_dict = []
    with open(path,"r") as archivo:
        buffer_dict = json.load(archivo)
        return buffer_dict['heroes']

def imprimir_menu():
    """
    imprime el menu de la app
    No recibe paramentro ni devuelve nada
    """
    print("1- Lista los primeros N heroes que pida el usuario \n"
          "2- Ordenar y listar heroes por altura \n" 
          "3- Ordenar y listar heroes por fuerza \n"
          "4- calular pormedio de una key numerica y filtra por su condicion de menor o mayor \n"
          "5- Busca heroes por inteligencia (average- high- good] y los lista \n"
          "6- Exporta a csv la lista de las opciones anteriores \n"
          "7- Salir \n\n")

def validar_entero(respuesta:str,patron:str)->int: 
    """
    valida que la respuesta recibida este compuesta con numeros unicamente y sea un entero
    recibe un input del usuario y un patron de numeros en regex
    retorna la respuesta castiada a entero
    """   
    if respuesta:
        if re.match(patron,respuesta):
            respuesta = int(respuesta)
            return respuesta
    return -1
   

def mostrar_heroe(lista:list[dict],key:str="fuerza")->str:
    """
    muestr la informacion del heroe : nombre - identidad y una key que el usuario quiera a eleccion
    Recibe una lista y la key a eleccion del usuario
    Retorna un mensaje con la informacion solicitada
    """
    
    for heroe in lista:
        if key in heroe.keys():            
            print(f"Nombre: {heroe['nombre']} || Identidad: {heroe['identidad']} || {key.capitalize()} : {heroe[key]} \n")
            
   

def validar_largo_lista(lista:list,tamaño:int)->int:
    """
    Valida la longitud de la lista para que el usuario no pida mas informacion que la que contiene
    Recibe una lista y un tamaño
    Retorna ul tamaño    
    """
    longitud = len(lista)
   
    
    if tamaño > 0 and tamaño <= longitud:
       
        return tamaño


def buscar_indice_max_min(lista:list,key:str,orden:str)->int:
    """
    Busca un minimo en una lista de elementos dict con clave [key]
    Recibe una lista de elementos dict con clave -key- y la clave y un orden prestablecido
    Retorna el indice del elemnto  segun el orden prestablecido 
    """
    indice_max_min = 0
    
    for i in range(1,len(lista)):
        if (orden == "asc" and lista[i][key] < lista[indice_max_min][key]) or (orden == "des" and lista[i][key] > lista[indice_max_min][key]):
            indice_max_min = i
    return indice_max_min

def buscar_minimo_maximo_por_key(lista:list,key:str,orden:str)->list:
    """
    recibe una lista y la copia, para poder swapear los elementos segun el orden establecido
    recibe una lista con elementos con clave - key - y un orden prestablecido
    Retorna la lista ordenada 
    """
    lista_ordenada = lista[:]
    for i in range(len(lista_ordenada)):
        index_max_min = buscar_indice_max_min(lista_ordenada[i:],key,orden) + i
        lista_ordenada[index_max_min], lista_ordenada[i] = lista_ordenada[i],lista_ordenada[index_max_min]
    return lista_ordenada

def lista_por_inteligencia(lista:list[dict],palabra:str,key:str="inteligencia"):
    """"
    Lista los heroes por tipo inteligencia [average - high - good]
    Recibe una lista y su clave - key.
    Retorna una lista de los heroes que cumplen la condicion    
    """
   
    
    for heroe in lista:
        match = re.match(palabra,heroe[key],re.IGNORECASE)
        if(match):
            var_key = heroe[key]
            print(f'{heroe["nombre"]} || {heroe["identidad"]} || {var_key}\n')
            
           


def heroes_superan_promedio(lista:list[dict],key:str,orden:str)->list:
    
    acumulador_key = 0
    longitud_lista = len(lista)
    for heroe in lista:
        if re.search("peso|altura|fuerza",key):
           acumulador_key += heroe[key]

    promedio = acumulador_key / longitud_lista
    lista_por_orden = []
    for heroe in lista:
        
         if heroe[key] > promedio and orden == "mayor":            
            lista_por_orden.append(heroe['nombre'])  

         elif heroe[key] < promedio and orden == "menor":
            
            lista_por_orden.append(heroe['nombre'])
            
    print(f"el promedio es : {promedio} " )
    return lista_por_orden

def exportar_csv(lista:list,path:str,key:str):
    
    with open(path,"w") as archivo:
        for heroe in lista:
            archivo.write(f'{heroe["nombre"]},{heroe["identidad"]},{heroe[key]}\n')



       



    

