


from data_pokemon import pokemones
import re

def obtener_nombre_pokemon(pokemon:list[dict]):
    
    return pokemon["nombre"]
    
def pokedex_imprimir_pokemones(pokemon:list):
    print(obtener_nombre_pokemon(pokemon))


# 2.1
def tiene_id_par(pokemon:dict):
    if pokemon['id'] % 2 == 0:
        return True
    else:
        return False
# 2.2 
def obtener_id_pokemon(pokemon:dict):
    
       return f'{pokemon["id"]}'
    

# 2.3
def pokedex_imprimir_pokemones_id_par(lista:list,indice:int):
    if tiene_id_par(lista[indice]):
        print(obtener_nombre_pokemon(lista[indice]))


# 3.1
def id_multiplo_25(pokemon:dict):
    if pokemon['id'] % 25 == 0:
        return True
    else:
        return False

  
# 3.2
def pokedex_imprimir_pokemon_id_mul_25(lista:list):
    
    
        if id_multiplo_25(lista) == True:
            pokedex_imprimir_pokemones(lista)

# 4.1
def nombre_format_pokemon(pokemon:list[dict]):
    nombre = obtener_nombre_pokemon(pokemon)
    id = obtener_id_pokemon(pokemon)
    return f'#{id.zfill(3)} - {nombre}'




#4.2
def pokedex_imprimir_nombres_poke_fmt(pokemon:list):
    print(nombre_format_pokemon(pokemon))


#5.1 VER
def calcular_max_dato(pokemon:list[dict],tipo:str,key:str) -> int:
    retorno = 0
    if tipo == "maximo" and type(tipo) == type(str()) and len(pokemon) > 0 and (key == "id" or key == "poder"):
        max = pokemon[0]
        for poke in pokemon:
            if poke[key] > max[key]:
                max = poke
            retorno = max[key]
    return retorno

#print(calcular_max_dato(pokemones,"maximo","id"))

# 5.2
def obtener_lista_pokemones(lista:list[dict],key:str,valor:int):
    lista_vacia = []
    for poke in lista:
        if  poke[key] == valor:
            lista_vacia.append(poke['nombre'])
    return lista_vacia

            
       
# 5.3
def string_max_dato(pokemones:list,maximo:str,key:str):
    max_dato = calcular_max_dato(pokemones,maximo,key)
    lista_pokemones = obtener_lista_pokemones(pokemones,key,max_dato)
    lista_pokemones = " - ".join(lista_pokemones)

    return f'poder maximo: {max_dato} | pokemones: {lista_pokemones}'

# print(string_max_dato(pokemones,"maximo","poder"))

# 5.4 

def imprimir_pokemones_fuertes(pokemones:list):
    return print(string_max_dato(pokemones,"maximo","poder"))

# imprimir_pokemones_fuertes(pokemones)

# 5.5 no lo entendi

def pokedex_imprimir_pokemones_fuertes(lista:list):
    print(obtener_nombre_pokemon(string_max_dato(lista,"maximo","poder")))

# 6.1
def calcular_min_dato(lista:list,tipo:str, key:str):
    

    if re.findall("[minimo]",tipo) and len(lista) > 0 and type(tipo) == type(str()) and re.findall("poder|id",key):
        min_dato = lista[0]
        for poke in lista:
            if poke[key] < min_dato[key]:
                min_dato = poke
    return min_dato[key]

# print(calcular_min_dato(pokemones,"minimo","poder"))

# 6.2

def string_min_dato(lista:list,string:str,key:str):
    
    dato_min = calcular_min_dato(lista, string, key)
    lista_poke = obtener_lista_pokemones(lista,key,dato_min)
    lista_poke = "".join(lista_poke)
    return f'poder minimo : {dato_min} | pokemones: {lista_poke}'

 # print(string_min_dato(pokemones,"minimo","poder"))

# 6.3

def imprimir_pokemones_debiles(lista:list):
    print(string_min_dato(lista,"minimo","poder"))

# 6.4 no lo entendi, que diferencia hay con el 6.3 ?

# 6.4.1 opcional ---> no me imprime nada !!
def calcular_min_max_dato(lista:list, tipo:str,key:str):
    if len(lista) > 0 and re.findall("maximo|minimo",tipo) and re.findall("poder|id",key) and type(lista) == type(list()):
       max_min = lista[0]
       for poke in lista:
           if (tipo == "maximo" and poke[key] > max_min[key]):             
              max_min = poke
           elif (tipo == "minimo" and poke[key] < max_min[key]):
              max_min = poke
    
    dato = obtener_lista_pokemones(lista,key,max_min[key])
    dato = " - ".join(dato) 
    print(dato)
    return dato
# calcular_min_max_dato(pokemones,"maximo","poder")
# 07 a 09

def calcular_promedio_dato(lista:list[dict],key:str,tipo:str) -> float:
    if len(lista) > 0 and re.findall("poder|id",key):
        acumulador_keys = 0
        contador_poke = 0
        
        for poke in lista:
            if tipo in poke["tipo"]:
                if type(poke[key]) == type(int()):
                   acumulador_keys = acumulador_keys + poke[key]
                   contador_poke += 1
                    
    promedio = float(acumulador_keys/contador_poke)
    
    return promedio                

#print(calcular_promedio_dato(pokemones,"poder","fuego"))

def pokedex_imprimir_promedio_dato_tipo(lista:list[dict],key:str,tipo:str):
    calculo = calcular_promedio_dato(lista,key,tipo)
    mensaje = f'El promedio de fuerza de pokemones de fuego es : {calculo}'
    mensaje = print(mensaje)
    return mensaje

#pokedex_imprimir_promedio_dato_tipo(pokemones,"poder","fuego")

# 10.01
def tiene_varios_tipos(pokemon:dict):
    
    if len(pokemon["tipo"]) > 1:
        return True
    else:
        return False

#print(tiene_varios_tipos(pokemones))

# 10.2
def obtener_pokemones_varios_tipos(lista:list[dict]):

    lista_varios = []
    for poke in lista:
        if tiene_varios_tipos(poke) == True:
            lista_varios.append(poke["nombre"])
    
    return lista_varios
    
    

#print(obtener_pokemones_varios_tipos(pokemones))

def pokedex_imprimir_pokemones_varios_tipos(lista:list[dict]):
    lista_varios  = obtener_pokemones_varios_tipos(lista)
    
       
    nombre = ""
    for poke in lista:
        if poke['nombre'] in lista_varios:
            nombre = pokedex_imprimir_nombres_poke_fmt(poke)
    nombre = str(nombre)
    
        
   


#pokedex_imprimir_pokemones_varios_tipos(pokemones)
        
   



# 12.01

def tiene_varias_evos(pokemon:dict):

    if len(pokemon["evoluciones"])> 1:
        return True
    else:
        return False
# 12.02
def obtener_pokemones_varias_evos(lista:list):
    lista_vacia = []
    for poke in lista:
        if tiene_varias_evos(poke) == True:
            lista_vacia.append(poke)
    
    return lista_vacia

#print(obtener_pokemones_varias_evos(pokemones))

# 12.03
def pokedex_imprimir_pokemones_varias_evos(lista:list) -> str:
    lista_aux = obtener_pokemones_varias_evos(lista)
    
    mensaje = ""
    for poke in lista_aux:
        mensaje += f'{poke["nombre"]} \n'
    return mensaje
    
    

print(pokedex_imprimir_pokemones_varias_evos(pokemones))


# 13.01
lista_vacia = obtener_pokemones_varias_evos(pokemones)
def obtener_pokemones_cantidad_evos(lista:list[dict]) ->dict:
    dic = {}
    
    for poke in lista:
        dic[poke['nombre']] = len(poke['evoluciones'])
    return dic

#obtener_pokemones_cantidad_evos(lista_vacia)

# 13.02

def pokedex_imprimir_pokemones_cantidad_evos(lista:list) -> str:
    dic = obtener_pokemones_cantidad_evos(lista_vacia)
    mensaje = ""
    for clave, valor in dic.items():
        mensaje += f'Pokemon: {clave} | Cantidad de evoluciones: {valor} \n'

    return mensaje

# print(pokedex_imprimir_pokemones_cantidad_evos(pokemones))

#14.01

def tiene_varias_fortalezas(dic:dict)->bool:

    if len(dic['fortaleza']) > 1:
        return True
    else:
        return False
# 14.02
def obtener_pokemones_varias_fortalezas(lista:list) -> list:
    lista_auxiliar = []
    for poke in lista:
        if tiene_varias_fortalezas(poke) == True:
            lista_auxiliar.append(poke)
    return lista_auxiliar

# 14.03

def pokedex_imprimir_pokemones_varias_fortalezas(lista:list)->str:
    lista_fortalezas = obtener_pokemones_varias_fortalezas(lista)
    mensaje = ""
    for poke in lista_fortalezas:
        mensaje += f'{poke["nombre"]} \n'
    return mensaje
        

#print(pokedex_imprimir_pokemones_varias_fortalezas(pokemones))

# 15.01
lista_fortalezas = obtener_pokemones_varias_fortalezas(pokemones)

def obtener_pokemones_cantidad_fortalezas(lista:list) ->dict :
    dic = {}
    
    for poke in lista:
        dic[poke['nombre']] = len(poke['fortaleza'])
    return dic

#print(obtener_pokemones_cantidad_fortalezas(lista_fortalezas))
# 15.02

def pokedex_imprimir_pokemones_cantidad_fortalezas(lista:list[dict]) -> str:
    dic = obtener_pokemones_cantidad_fortalezas(lista_fortalezas)
   
    mensaje = ""
    for clave, concepto in dic.items():
        mensaje += f'Pokemon: {clave} | cantidad de fortalezas : {concepto} \n'
    return mensaje

#print(pokedex_imprimir_pokemones_cantidad_fortalezas(pokemones))

# 16.01

def tiene_varias_debilidades(dic:dict) -> bool:

    if len(dic['debilidad']) > 1:
        return True
    else:
        return False

# 16.02
def obtener_pokemones_varias_debilidades(lista:list) -> list:
    lista_auxiliar = []

    for poke in lista:
        if tiene_varias_debilidades(poke) == True:
            lista_auxiliar.append(poke)
    return lista_auxiliar

#16.03


def pokedex_imprimir_pokemones_varias_debilidades(lista:list) -> str:
    lista_auxiliar = obtener_pokemones_varias_debilidades(lista)
    mensaje = ""
    for poke in lista_auxiliar:
        mensaje += f'{poke["nombre"]} \n'  

    return mensaje    
 
# print(pokedex_imprimir_pokemones_varias_debilidades(pokemones))

lista_debilidades = obtener_pokemones_varias_debilidades(pokemones)

def obtener_pokemones_cantidad_debilidades(lista:list) -> dict:
    dic = {}

    for poke in lista:
        dic[poke['nombre']] = len(poke['debilidad'])
    return dic

#print(obtener_pokemones_cantidad_debilidades(lista_debilidades))
# 17.02
def pokedex_imprimir_pokemones_cantidad_debilidades(lista:list) -> str:

    dic = obtener_pokemones_cantidad_debilidades(lista)
    mensaje = ""
    for clave, concepto in dic.items():
        mensaje += f'Pokemon : {clave} | cantidad debilidades: {concepto} \n'
    return mensaje

# print(pokedex_imprimir_pokemones_cantidad_debilidades(pokemones))




        





    
    
        






        












    

    



















        

        

        



        
        
        
        

        
















