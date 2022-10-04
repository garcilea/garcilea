
import re 
import json

def abrir_json(path:str)->list:
    """
    recibe el nombre del archivo que desea abrir en modo lectura en tipo string
    lo carga para poder consultarlo
    retorna la lista con los diccionarios que se encuentre dentro de la lista  
    """
    with open(path,"r",encoding="utf8") as archivo:
        buffer_json = json.load(archivo)
    return buffer_json["paulina"]

def imprimir_menu():
    print("\n")
    print(" Bienvenido a la app de Paulina!\n"
          "1 - Listar TOP N videos\n"
          "2 - Ordenar videos por duracion (UP/DOWN)\n"
          "3 - Ordenar videos por cantidad de views (UP/DOWN)\n"
          "4 - Buscar videos por título\n"
          "5 - Exportar lista de videos a CSV\n"
          "6 - Salir\n\n")

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
    elif tamaño == 0:
        print("error: tamaño inequivoco, vuelva a elegir")
    else:
        return -1

def mostrar_video(lista:list[dict],key:str="date")->str:
    """
    muestra informacion del video y una key a eleccion ( por default muestra la fecha)
    recibe una lista y una clave-key-
    devuelve una cadena (string)
    """
    for video in lista:
        print(f'Titulo: {video["title"]} - Views: {video["views"]} - {key.capitalize()} : {video[key]}')


def buscar_posicion_lista(lista:list[dict],key:str,orden:str="up")->int:
    """
    busca la posicion del maximo o minimo que contenga la lista
    recibe una lista que adentro tiene un dic por el cual recibe la clave y un ordenamient ( up o down)
    retorn un entero que indica la posicion del min-max buscado
    """
    indice_max_min = 0
    for i in range(len(lista)):
        if (re.match("up",orden) and lista[i][key] < lista[indice_max_min][key]) or  (re.match("down",orden) and lista[i][key] > lista[indice_max_min][key]):
            indice_max_min = i
    return indice_max_min

def ordenar_videos_por_key(lista:list[dict],key:str,orden:str)->list:
    """
    ordena los videos de una lista segun el orden proporcionado respecto a la key
    recibe una lista que adentro tiene un diccionario con su clave-key y un orden que se va a establecer
    retorna una lista ordenada        
    """
    lista_copiada = lista[:]

    for i in range(len(lista_copiada)):
        indice_max_min = buscar_posicion_lista(lista_copiada[i:],key,orden) + i
        lista_copiada[i],lista_copiada[indice_max_min] = lista_copiada[indice_max_min],lista_copiada[i]
    return lista_copiada    

def buscar_videos_por_titulo(lista:list[dict],key:str,palabra:str):
    """"
    busca que titulos de los videos coinciden con su busqueda
    recibe una lista de diccionarios, y busca por su key "title"
    retorna el titulo segun la coincidencia de la palabra encontrada
    """
    for video in lista:
        match = re.match(palabra,video[key],re.IGNORECASE)
        if (match):
            titulo = video[key]
            print(titulo)
        
def exportar_csv(lista:list,path:str,key:str)->list:
    contenido_archivo = ""
    with open(path,"w") as archivo:
        for video in lista:
            contenido_archivo += f'{video["views"]},{video[key]}\n'            
        return archivo.write(contenido_archivo)
