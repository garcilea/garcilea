import re
import json

def cargar_json(path:str)->list[dict]:
    """
    carga el json y lo abre en modo lectura para utilizarlo, tambien lo cierra.
    Recibe como parametro la ruta del archivo
    retorna los diccionarios dentro de la lista que estaba en el json
    """
    buffer_dict = []
    with open(path,"r",encoding="utf8") as archivo:
        buffer_dict = json.load(archivo)
        return buffer_dict['heroes']


def imprimir_menu():
    """
    imprime en la termina el menu para que el usuario elija las opciones
    """
    print("1- Listar los primeros N héroes \n"
          "2- Ordenar y Listar héroes por altura \n"
          "3- Ordenar y Listar héroes por fuerza  \n"
          "4- heroes que superan el promedio de una key ordenados en forma ascendente  \n"
          "5- lista heroes por inteligencia que cumplan la condicion de good average y high\n"
          "6- Exporta csv la lista de heroe ordenada segun requiera usuario \n"
          "7- Salir" )

def validar_entero(respuesta:str,patron:str)->int: 
    """
    valida que la respuesta recibida este compuesta con numeros unicamente y sea un entero
    recibe un input del usuario y un patron de numeros en regex
    retorna la respuesta castiada a entero - en c
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
    Retorna un tamaño    
    """
    longitud = len(lista)
   
    
    if tamaño > 0 and tamaño <= longitud:
       
        return tamaño

def mostrar_heroe(lista:list[dict],key:str)->str:
    """
    muetra la informacion de cada heroe contenido en la lista
    recibe un dic proveniente de una lista y la itera con su clave - key -
    retorna la la informacion del heroe formateada    
    """
    
    for heroe in lista:
        if key in heroe.keys():            
            print(f"Nombre: {heroe['nombre']} || Identidad: {heroe['identidad']} || {key.capitalize()} : {heroe[key]} \n")
        
    

def buscar_indice_max_min(lista:list,key:str,orden:str)->int:
    """
    en base a una lista recibidad y una clave-key- permite obtener la posicion del minimo o maximo a buscar
    Recibe una lista , la key - clave - del diccionario que se encunetra dentro  y un ordenamient "up" o "down"
    retorna un entero que indica la posicion del mismo
    """
    
    indice_max_min = 0
    for i in range(1,len(lista)):
        if (orden == "up" and lista[i][key] < lista[indice_max_min][key]) or (orden == "down" and lista[i][key] > lista[indice_max_min][key]):
            indice_max_min = i
    return indice_max_min

      
    

def ordenar_lista(lista:list[dict],key:str,orden:str):
    """
    recibe una lista y la copia, para poder swapear los elementos segun el orden establecido
    recibe una lista con elementos con clave - key - y un orden prestablecido
    Retorna la lista ordenada 
    """
    lista_copiada = lista[:]
    for i in range(len(lista_copiada)):
        indice_max_min = buscar_indice_max_min(lista_copiada[i:],key,orden) + i
        lista_copiada[i],lista_copiada[indice_max_min] = lista_copiada[indice_max_min],lista_copiada[i]
    return lista_copiada

  



def promedio_heroes(lista:list[dict],key:str,orden:str)->list:
    """
    Saca el promedio general de una key para mostrar los heroes que superan o no ese promedio
    recibe una lista con un diccionario dentro con su clave - key - 
    retorna un sting con la informacion del heroe
    """
    longitud  = len(lista)
    acumulador_key = 0
    lista_por_condicion = []

    for heroe in lista:
        if  longitud > 0 and re.findall("altura|peso|fuerza",key):
            acumulador_key += heroe[key]
    
    promedio = acumulador_key / longitud

    for heroe in lista:
        if heroe[key] < promedio and orden == "menor":
            lista_por_condicion.append(heroe)
        elif heroe[key] > promedio and orden == "mayor":
            lista_por_condicion.append(heroe)

    print(f"el promedio {orden} al promedio general que es : {promedio} slo listan los siguientes heroes : " )
    return lista_por_condicion
        
def lista_heroes_por_inteligencia(lista:list[dict],palabra:str,key:str="inteligencia")->str:
    """
    En base a una palabra recibida busca dentro la key - inteligencia - si esta o no 
    En caso de que si, muestra al heroe que coincidan
    recibe una lista, una palabra a buscar y una key - prestablecida ( inteligencia)
    retorna un string formateado
    """
    
    for heroe in lista:
        match = re.match(palabra,heroe[key],re.IGNORECASE)    
        if (match):
            tipo_inteligencia = heroe[key]
            print(f'heroe: {heroe["nombre"]} || {heroe["identidad"]} || {key} - {tipo_inteligencia}\n')
            
    

def exportar_csv(lista:list,path:str,key:str="fuerza"):
    with open(path,"w") as archivo:
        for heroe in lista:
            archivo.write(f'{heroe["nombre"]},{heroe["identidad"]},{heroe[key]}\n')





    

