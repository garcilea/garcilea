import re
import json

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

def validar_respuesta(patron:str,respuesta:str)->str:
    if respuesta:
        match_o = re.match(patron,respuesta,re.IGNORECASE)
        if match_o:               
             return str(respuesta)
        else:
            return False
   

def imprimir_menu():
    print("1- Listar N heroes\n"
          "2- Ordenar y listar por fuerza\n"
          "3- Ordenar y listar por poder\n"
          "4- Promedio segun key\n"
          "5- Buscar palabra\n"
          "6- Exportar csv\n"
          "7- Salir\n")

def cargar_json(path:str)->list[dict]:
    buffer_dict = []
    with open(path,"r",encoding="utf-8") as archivo:
        buffer_dict = json.load(archivo)
        return buffer_dict["heroes"]

def mostrar_heroe(lista:list,key:str):
    if lista:
        for heroe in lista:
            print(f'Nombre: {heroe["nombre"]}, Identidad: {heroe["identidad"]}, {key.capitalize()}: {heroe[key]}')

def exportar_csv(lista:list[dict],path:str,key:str):
    with open(path,"w") as archivo:
        for heroe in lista:
            archivo.writelines(f'Nombre: {heroe["nombre"]}, Identidad: {heroe["identidad"]}, {key.capitalize()}: {heroe[key]}\n')

    
def buscar_indice_max_min(lista:list,key:str,orden:str)->int:
    ind_max_min = 0
    if lista: 
        for i in range(len(lista)):
         if (lista[i][key] > lista[ind_max_min][key] and orden == "up") or (lista[i][key] < lista[ind_max_min][key] and orden == "down"):
            ind_max_min = i
        return ind_max_min

def ordenar_lista_orden(lista:list,key:str,orden:str)->list:
    lista_copia = lista[:]
    
    for i in range(len(lista)):
        ind_max_min = buscar_indice_max_min(lista_copia[i:],key,orden) + i
        lista_copia[i],lista_copia[ind_max_min] = lista_copia[ind_max_min],lista_copia[i]
    return lista_copia

def buscar_heroe_por_inteligencia(lista:list,tipo:str,key:str = 'inteligencia'):
    if lista:
        for heroe in lista:
            match = re.match(tipo,heroe[key],re.IGNORECASE)
            if (match):
                tipo_int = heroe[key]
                print(f'Nombre: {heroe["nombre"]}, Identidad: {heroe["identidad"]}, {key.capitalize()}: {tipo_int}\n')
    
                
def promedio_heroes(lista:list[dict],key:str,orden:str)->list:
    """
    Saca el promedio general de una key para mostrar los heroes que superan o no ese promedio
    recibe una lista con un diccionario dentro con su clave - key - 
    retorna un sting con la informacion del heroe
    """
    
    acumulador_key = 0
    lista_por_condicion = []

    for heroe in lista:
        if  lista and re.findall("altura|peso|fuerza",key):
            acumulador_key += heroe[key]
    
    promedio = acumulador_key / len(lista)

    for heroe in lista:
        if heroe[key] < promedio and orden == "menor":
            lista_por_condicion.append(heroe)
        elif heroe[key] > promedio and orden == "mayor":
            lista_por_condicion.append(heroe)
    print(f"el pormedio es {promedio}")
    return lista_por_condicion

                
