# 1) validar que la lista no venga vacia y que sea del tipo lista


from data_stark import lista_personajes



def stark_normalizar_datos(lista:list,clave:str):
    modificado = 0 
    vacio = 0
    
    if (len(lista) > 0)  and (type(lista) == type([])):
        vacio = 1
        for heroe in lista:
        
            if (clave == "altura" or clave == "peso") and heroe[clave] != type(float) :
                heroe[clave] = float(heroe[clave])
                modificado = 1
            elif clave == "fuerza" and heroe[clave] != type(int):
                heroe[clave] = int(heroe[clave])
                modificado = 1
           
    if modificado == 1:
        print("Datos normalizados")
    
    if vacio == 0:
        print("lista de errores vacia")

def obtener_nombre(heroe:dict):
    
    return f'Nombre : {heroe["nombre"]}'
        
print(obtener_nombre(lista_personajes[4]))     

def imprimir_dato(cadena:str):
    if type(cadena) == type(str()):
        print(cadena)
        
    



def tark_imprimir_nombres_heroes(lista:list):
    
    for heroes in lista:
               
        return imprimir_dato(obtener_nombre(heroes))

tark_imprimir_nombres_heroes(lista_personajes)
 


def obtener_nombre_y_dato(heroe:dict,dato:str):
    for h in heroe:
        return print(f'{obtener_nombre(h)} | {dato} : {h[dato]}')
    
print(obtener_nombre_y_dato(lista_personajes,"fuerza"))

def stark_imprimir_nombres_alturas(lista:list):
    if lista == []:
        return -1

    for h in lista:
        
        return obtener_nombre_y_dato(lista,"altura")  

#print(stark_imprimir_nombres_alturas(lista_personajes))

#def calcular_max():






            

"""
        "nombre": "Rocket Raccoon",
        "identidad": "Rocket Raccoon",
        "empresa": "Marvel Comics",
        "altura": "122.77",
        "peso": "25.73",
        "genero": "M",
        "color_ojos": "Brown",
        "color_pelo": "Brown",
        "fuerza": "5",
        "inteligencia": "average" 
"""