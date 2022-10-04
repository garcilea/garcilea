import json
import re

from jmespath import search


def cargar_json(path:str):
    """
    Abre el archivo desde un set de datos json
    Recibe una direccion
    retorna un diccionario dentro de una lista
    """
    dic_data = []
    with open(path,"r",encoding = "utf-8") as archivo:
        dic_data = json.load(archivo)
        return dic_data["results"]

def buscar_ind_max_min(lista:list,key:str,orden:str)-> int:
    """
    busca el indice del menor o mayor en la lista segun lo requiera el usuario ( up de menor a mayor) y down visceversa
    Recibe una lista dentro un diccionario y una orden que seria para buscar el mayor o menor
    retorna el indice segun corresponda que es un entero    
    """
    ind_max_min = 0
    for i in range(len(lista)):
        if (lista[i][key] < lista[ind_max_min][key] and orden == "up") or (lista[i][key] > lista[ind_max_min][key] and orden == "down"):
            ind_max_min = i
        return ind_max_min

def ordenar_por_key(lista:list,orden:str,key:str)->list:
    """
    Permite ordenar la lista segun la orden que le pasemos en base al indice mayor o menor de lista
    Recibe una lista que tiene un dic con su clave - key - y una orden segun lo que requiera el usuario
    retorna la lista ordenada    
    """
    lista_copia = lista[:]

    if lista_copia:
        for i in range(len(lista_copia)):
            ind_max_min = buscar_ind_max_min(lista_copia[i:],key,orden) + i
            lista_copia[i],lista_copia[ind_max_min] = lista_copia[ind_max_min],lista_copia[i]

    return lista_copia

def convertir_keys_a_entero(lista:list[dict],key:str)->int:
    """
    Convierte las key que posean numeros al tipo entero
    REcibe una lista que contiene un dict con su clave
    """

    if lista:
        for personajes in lista:
            if re.match(["[0-9]+$"],personajes[key]):
                cambio = int(personajes[key])
    return lista



def validar_entero(patron:str,input:str)->int:

    match = re.match(patron,input,re.IGNORECASE)
    if(match):
        input = int(input)
        return input

def exportar_csv(lista:list[dict],path:str,key:str):
    """
    Permite exportar en un archivo csv la lista generada en el punto que consulto el cliente
    Recibe una lista con su clave - key que desea informar y la direccion donde se exporta
    escribe el archivo que exporta
    """
    for personajes in lista:
        with open(path,"w") as archivo:        
            archivo.write(f'Nombre: {personajes["name"]}, {key.capitalize()}: {personajes[key]}')



def mostrar_personaje(lista:list[dict],key:str):
    """
    muestra la informacion del personaje segun lo establecido
    Recibe una lista que posee un diccionario con su key
    No retorna nada, solo imprime la info
    """
    if lista:
        for personajes in lista:
            print(f'Nombre: {personajes["name"]}, {key.capitalize()}: {personajes[key]}')

def buscar_personaje(lista:list[dict],palabra:str,key:str = "name"):
    """
    Busca segun alguna palabra encontrada en alguna key del personaje la info del mismo, por defecto buscara el nombre
    Recibe una lista que adentro tiene un diccionario con su key y la palabra que desea buscar
    Muestra el personaje
    """

    for personajes in lista:

        match_o = re.match(palabra,personajes[key],re.IGNORECASE)

        if (match_o):
            palabra = personajes[key]
            print(f'Nombre: {personajes["name"]}, {key.capitalize()}: {palabra}')


def muestra_personaje_mas_alto_por_genero_masc(lista:list,key:str = "altura"):
    if lista:
        lista_masc = ordenar_por_key(lista,"down",key)
        for personajes in lista_masc:
            if personajes["gender"] == "male":
                personje_masc =  f'Nombre: {personajes["name"]}'
                return  personje_masc
               

def muestra_personaje_mas_alto_por_genero_fem(lista:list,key:str = "altura"):
        if lista:
            lista_fem= ordenar_por_key(lista,"down",key)
            for personajes in lista_fem:
                if personajes["gender"] == "female":
                     personje_fem =  f'Nombre: {personajes["name"]}'
                     return personje_fem 
            
            


