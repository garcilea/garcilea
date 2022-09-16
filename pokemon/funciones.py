
from data_pokemon import pokemones

def obtener_nombre_pokemon(pokemon:dict):
    
    return pokemon["nombre"]
    
def pokedex_imprimir_pokemones(pokemon:list):
    print(obtener_nombre_pokemon(pokemon))



def tiene_id_par(pokemon:dict):
    if pokemon['id'] % 2 == 0:
        return True
    else:
        return False
# 2.2 
def obtener_id_pokemon(pokemon:dict):
    if pokemon['id'] != type(str()):
       return str(pokemon['id'])

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
def nombre_format_pokemon(pokemon:dict):
    nombre = obtener_nombre_pokemon(pokemon)
    id = obtener_id_pokemon(pokemon)
    return f'#{id} - {nombre}'


#4.2
def pokedex_imprimir_nombres_poke_fmt(pokemon:list):
    print(nombre_format_pokemon(pokemon))

#5.1 VER
def calcular_max_dato(pokemon:list,tipo:str,key:str) -> int:
    retorno = 0
    if tipo == "maximo" and type(tipo) == type(str()) and len(pokemon) > 0 and (key == "id" or key == "poder"):
        max = pokemon[0]
        for poke in pokemon:
            if poke[key] > max[key]:
                max = poke[key]
            retorno = max
    return retorno

print(calcular_max_dato(pokemones,"maximo","poder"))

# 5.2
def obtener_lista_pokemones(lista:list, key:str,valor:int):
    lista_vacia = []
    for poke in lista:
        if  poke[key] == valor:
            
            lista_vacia.append(poke['nombre'])
            
       
# 5.3
def string_max_dato(pokemones:list,maximo:str,key:str):
    max_dato = calcular_max_dato(pokemones,maximo,key)
    for pokemon in pokemones:

        lista_pokemones = obtener_lista_pokemones(pokemones,key,)
    pass

        

        

        



        
        
        
        

        
















