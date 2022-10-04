import re
import json

def cargar_json(path:str)->list[dict]:
    buffer_dict = []
    with open(path,"r",encoding = "utf-8") as archivo:
        buffer_dict = json.load(archivo)
        return buffer_dict['heroes']


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

def validar_largo_lista(lista:list,tamaño:int)->int:
    """
    Valida la longitud de la lista para que el usuario no pida mas informacion que la que contiene
    Recibe una lista y un tamaño
    Retorna ul tamaño    
    """
    longitud = len(lista)
   
    
    if tamaño > 0 and tamaño <= longitud:
       
        return tamaño

def mostrar_menu():
    print("1- Listar los primeros N héroes \n"
          "2- Ordenar y Listar héroes por altura \n"
          "3- Ordenar y Listar héroes por fuerza  \n"
          "4- heroes que superan el promedio de una key ordenados en forma ascendente  \n"
          "5- lista heroes por inteligencia que cumplan la condicion de good average y high\n"
          "6- Exporta csv la lista de heroe ordenada segun requiera usuario \n"
          "7- Salir" )

def mostrar_heroe(lista:list[dict],key:str = "fuerza"):
    for heroe in lista:
        if key in heroe.keys():
            print(f'Nombre = {heroe["nombre"]} || Identidad: {heroe["identidad"]} || {key.capitalize()}: {heroe[key]}')


def exportar_csv(lista:list,path:str,key:str):
    with open(path,"w") as archivo:
        for heroe in lista:
          archivo.write(f'{heroe["nombre"]} || Identidad: {heroe["identidad"]} || {key.capitalize()} : {heroe[key]}\n')



def buscar_indice_max_min(lista:list,key:str,orden:str)->int:
    ind_max_min = 0
    for i in range(len(lista)):
        if (orden == "up" and lista[i][key] < lista[ind_max_min][key]) or (orden == "down" and lista[i][key] > lista[ind_max_min][key]):
            ind_max_min = i
    return ind_max_min

def ordenar_lista(lista:list,key:str,orden:str)->list:
    lista_copia = lista[:]
    for i in range(len(lista)):
        ind_max_min = buscar_indice_max_min(lista_copia[i:],key,orden) + i
        lista_copia[ind_max_min],lista_copia[i] = lista_copia[i],lista_copia[ind_max_min]
    return lista_copia


def promedio_key(lista:list[dict],key:str,orden:str):
    acumulador_key = 0
    longitud_lista = len(lista)
    if longitud_lista > 0 :
        for heroe in lista:
            if key in heroe.keys() and re.search("fuerza|peso|altura",key):
                acumulador_key += heroe[key]

    promedio = acumulador_key / longitud_lista
    lista_por_condicion = []
    for heroe in lista:     
        if heroe[key] < promedio and orden == "menor":
            lista_por_condicion.append(heroe)
        elif heroe[key] > promedio and orden == "mayor":
            lista_por_condicion.append(heroe)
    
    print(f"el promedio es {promedio} " )
    return lista_por_condicion

def buscar_por_palabra(lista:list[dict],palabra:str,key:str = 'inteligencia'):
   
   if len(lista) > 0:
    for heroe in lista:
        match = re.match(palabra,heroe[key],re.IGNORECASE)
        if (match):
            coincidencia = heroe[key]
            print(f"{heroe['nombre']} || {heroe['identidad']} || {coincidencia} ")


def validar_respuesta(patron:str,respuesta:str)->None:
    if respuesta:
        match_o = re.match(patron,respuesta,re.IGNORECASE)
        if match_o:               
             return respuesta
        respuesta = ""
        return respuesta

        



