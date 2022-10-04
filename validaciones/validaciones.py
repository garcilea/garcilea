
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


def validar_respuesta(patron:str,respuesta:str)->None:
    if respuesta:
        match_o = re.match(patron,respuesta,re.IGNORECASE)
        if match_o:               
             return respuesta
    return print("Error")