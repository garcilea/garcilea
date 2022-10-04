import re
import json



def imprimir_menu():
       print("1- Listar los ultimos N pokemons\n"
             "2- Ordena y listar poke por poder\n"
             "3- Odenar y listar poke por ID\n"
             "4- Calcular la cantidad promedio de las key tipo lista\n"
             "5- Buscar pokemones por tipo y printiar en consola\n"
             "6- exportar csv de la opcion 1 al 4\n"
             "7- Salir\n")


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
    return print("Error")

def validar_largo_lista(lista:list,tamaño:int)->int:
    """
    Valida la longitud de la lista para que el usuario no pida mas informacion que la que contiene
    Recibe una lista y un tamaño
    Retorna ul tamaño    
    """
    longitud = len(lista)
   
    
    if tamaño > 0 and tamaño <= longitud:
       
        return tamaño

def cargar_json(path:str)->list[dict]:
    buffer_dict = []
    with open(path,"r",encoding = "utf-8") as archivo:
        buffer_dict = json.load(archivo)
        return buffer_dict["pokemones"]

def mostrar_poke(lista:list[dict],key:str = "poder")->str:
    
    if lista:
        for poke in lista:
            if key in poke.keys():
                print(f'Nomnre : {poke["nombre"]}, Evoludciones: {poke["evoluciones"]}, {key.capitalize()}: {poke[key]})')

def validar_respuesta(patron:str,respuesta:str)->None:
    if respuesta:
        match_o = re.match(patron,respuesta,re.IGNORECASE)
        if match_o:               
             return respuesta
    

def buscar_indice_max_min(lista:list[dict],key:str,orden:str)-> int:
    indice_max_min = 0
   
    for i in range(len(lista)):
        if (lista[i][key] < lista[indice_max_min][key] and orden == "up") or (lista[i][key] > lista[indice_max_min][key] and orden == "down"):
            indice_max_min = i            
    return indice_max_min

def ordena_lista_poke_segun_key(lista:list[dict],key:str,orden:str)-> list:
    lista_copia = lista[:]

    for i in range(len(lista_copia)):
        indice_max_min = buscar_indice_max_min(lista_copia[i:],key,orden) + i
        lista_copia[i], lista_copia[indice_max_min] =  lista_copia[indice_max_min],lista_copia[i]
    
    return lista_copia

def determina_promedio(lista:list[dict],key:str,orden:str)->list:

    pass
    acumulador_key = 0 
    
    if lista:
        for heroe in lista:            
            if re.match("evoluciones|fortaleza|debilidad|tipo",heroe.keys()):                             
                acumulador_key += len(heroe[key])   

    promedio =    acumulador_key
    lista = []
    for poke in lista:
        if (orden == "menor" and promedio > poke[key]) (orden == "mayor" and promedio < poke[key]):
            lista.append(poke["nombre"])
        elif (orden == "mayor" and promedio < poke[key]):
            lista.append(poke["nombre"])
    print(f"El promedio es : {promedio}")
    
    return lista



def exportar_csv(lista:list,path:str,key:str):
    with open(path,"w") as archivo:
        for poke in lista:
            archivo.writelines(f"Nombre : {poke['nombre']}, Identidad: {poke['id']}, {key.capitalize()} : {poke[key]}\n")

def buscar_por_tipo(lista:list[dict],tipo:str,key:str):    
    
    if lista:
        for poke in lista:
            str_tipo = "-".join(poke[key])
            str_fortaleza = "-".join(poke["fortaleza"])
            str_evol = "-".join(poke["evoluciones"])

            match = re.match(tipo,str_tipo,re.IGNORECASE)
            if (match):         
                
                print(f'Id: {poke["id"]} | Nombre: {poke["nombre"]} | {key.capitalize()}: {str_tipo} | Evoluciones: {str_evol} | Porder: {poke["poder"]} | Fortaleza: {str_fortaleza}')



    
   






