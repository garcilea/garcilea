
from data_pokemon import pokemones


#agregar un elemento a la lista de un diccionario
# Paso 1 : nombre_diccionario["key"]).append("elemento")
# Paso 2 : variable_nueva = list(nombre_diccionario["key"])
# variable_nueva.append("elemento")
# nombre_diccionario["key"] = variable_nueva

# recorrer lista de la key con lista
# concatenar en un string sus valores
# reemplazar valor de la key ataques por el string
# lo mas rapido es variable_str = " | ".join(nombre_diccionario["key"])
# nombre_diccionario["key"] = variable_str



# 1.1
def obtener_nombre_pokemon(dic:dict):
    for pokemon in dic:
        return pokemon['nombre']
obtener_nombre_pokemon(pokemones)
# 1.2
def imprimir_pokemones(lista:list):
    return print(obtener_nombre_pokemon(pokemones))

imprimir_pokemones(pokemones)
#2.1
def tiene_id_par(dic:dict):
    for pokemon in dic:
        if pokemon['id'] %2 == 0:
            return True
        else:
            return False
print(tiene_id_par(pokemones))
# 2.2
def obtener_id_pokemon(dic:dict):
    for pokemon in dic:
        return str(pokemon['id'])
print(type(obtener_id_pokemon(pokemones)))
# 2.3
def pokedex_imprimir_pokemones_id_par(lista:list):
    for pokemon in lista:
        if tiene_id_par(pokemon):
            return obtener_nombre_pokemon(lista)
# print(pokedex_imprimir_pokemones_id_par(pokemones))
# 3.1
def pokedex_imprimir_pokemon_id_mul_25(dic:dict):
    for pokemon in dic:
        if pokemon['id'] % 25 == 0 :
            print(pokemon)
            return True
        else:
            return False
        

print(pokedex_imprimir_pokemon_id_mul_25(pokemones))
# 3.2 MAL
def pokedex_imprimir_pokemon_id_mul_25(lista:list):
    print(obtener_nombre_pokemon(list(pokedex_imprimir_pokemon_id_mul_25(lista))))

#pokedex_imprimir_pokemon_id_mul_25(pokemones)
# 4.1
def nombre_format_pokemon(dic:dict):
    for pokemon in dic:
        id = str(obtener_id_pokemon(pokemon))
        nombre = str(obtener_nombre_pokemon(pokemon))

        return f'#{id} - {nombre}'
#print(nombre_format_pokemon(pokemones))




            
        
