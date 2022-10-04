import json

import re

def escribir_cadena(string:str):
    if type(string) == type(str()):
        print(string)


def abrir_json(path:str) -> list:
    """
    recibe el nombre del archivo que desea abrir en modo lectura en tipo string
    lo carga para poder consultarlo
    retorna la lista con los diccionarios que se encuentre dentro de la lista  
    """
    with open(path,"r") as archivo:
        buffer_dict = json.load(archivo)

    return buffer_dict["paulina"]

def mostrar_videos(lista:list):
    
    for elemento in lista:
        mensaje = f'{elemento["title"]} - {elemento["length"]} - {elemento["views"]}'
        return mensaje

def ordena_indice_max_min(lista:list,key:str,order,str) -> int:
    """
    busca el indice que encuentra del minimo o maximo segun la key a consultar dentro del diccionario
    recibe una lista junto a la key y al ordenamiento que el cliente desee
    retorna el indice donde se encuentre ese minimo o maximo si no lo encuentra retorna -1
    """
    retorno =  -1
    index_max_min = 0 
    if len(lista) > 0:
        for i in range(1,len(lista)):
            if (order == "down" and lista[i][key] < lista[index_max_min][key]) or (order == "up" and lista[i][key] > lista[index_max_min][key]):
                index_max_min = i
            retorno = index_max_min
    return retorno

def buscar_min_max(lista:list,key:str,order:str):
    """
    En base a una lista copiada
    encuentra el indice del minimo y maximo, y lo swapea en la primer posicion de la lista
    luego vuelve a encontrar el nuevo indice del minimo y maximo y lo swapea con el de la posicion siguiente al que comparaba anteriormente
    y asi sucesivamente
    recibe una lista, una key y un ordenamiento
    retorna una lista ordenada
    """
    lista_copia = lista[:] # puedo usar lista.copy() como otra opcion
   
    for i in range(len(lista_copia)):
       indice = ordena_indice_max_min(lista_copia[i:],key,order) + i
       lista_copia[i],lista_copia[indice] = lista_copia[indice],lista_copia[i]
    return lista_copia


def buscar_por_titulo(lista:list,key:str,palabra:str):
    """"
    busca que titulos de los videos coinciden con su busqueda
    recibe una lista de diccionarios, y busca por su key "title"
    retorna las coincidencias segun la o las palabras buscadas
    """
    print("\n")
    for elemento in lista:
      
       match = re.search(palabra,elemento[key],re.IGNORECASE)
     
       if (match):
        titulo = elemento[key]
        palabra = "\033[0;31m" + match.group() + "\033[0;m"
        titulo = titulo.replace(match.group(),palabra)
        print("{0} - {1} - {2}".format(elemento["views"],elemento["length"], titulo))
    print("\n")

def exportar_csv(lista:list,path:str):
    with open(lista,"w") as archivo:
        for elemento in lista:
         archivo.write("{0},{1},{2}\n".format(elemento["views"],elemento["length"], elemento["title"]))
    





    

        

    

   












