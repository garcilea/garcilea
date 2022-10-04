



"""
En la base de datos de la división de armamento de industrias Wayne se tiene una información 
la cual están con la necesidad de cambiar el formato la lista de habilidades con sus respectivos
puntos de combate, actualmente cada una de ellas está presente como un diccionario pero para su
nuevo sistema requieren que el tipo de dato sea una tupla la cual albergue solamente el nombre 
de la habilidad y su poder al estilo ("rayo laser", 99). A su vez, todas y cada una de las habilidades
deben estar dentro de una lista de habilidades, la cual debe ser el valor de una key que conforme un 
diccionario, como key par albergarlas usaremos “habilidades_UTN”.
Formato de resultado esperado:

{
 "habilidades_UTN": [("habilidad_alfa", número), ("habilidad_beta", número)] etc.
}

Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente. 
Una vez hecho esto, deberá recorrer dicha lista imprimiendo sus valores,  conjuntamente con la key 
que integra dicha estructura de datos.
EJEMPLO

habilidades_UTN:
Habilidad 1: habilidad_alfa | Poder: numero
Habilidad 2: habilidad_beta | Poder: numero
Etcétera.
Tip: ¡Te dejamos el diccionario de habilidades para que puedas utilizarlo!
"""

habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]

# debemos convertir el diccionario en tupla, la cual albergue solamente el nombre 
# de la habilidad y su poder al estilo ("rayo laser", 99).

# creo lista vacia
habilidades_UTN = []

# recorro las keys dentro del diccionario
for info_habilidades in habilidades:
    
    # creo variable y le asigno el valor que existe dentro de la key
    nombre_habilidad = info_habilidades['Nombre']
    poder_habilidad  = info_habilidades['Poder']
 
    # uno esos 2 valores en otra variable, para tenerlas juntas entre () como lo pide en el formato del ej.
    union = (nombre_habilidad, poder_habilidad)
    # agrego las dos variables a la lista vacia
    habilidades_UTN.append(union)
   


print(habilidades_UTN)

# creo una tupla de la lista 
tupla_habilidades_UTN = tuple(habilidades_UTN)
# ordeno la tupla, uso sorted---> permite ordenar cualquier tipo sea lista, tupla (funcion con cualquier iterable)
# se diferencia de sort, que solo funciona con listas unicamente
# La key tiene el valor lambda de la función, lo que indica al programa, ordenar al segundo elemento en orden ascendente
tupla_habilidades_UTN = sorted(tupla_habilidades_UTN, key = lambda poder: poder[1])
print(tupla_habilidades_UTN)

# se crea el diccionario
dic_habilidades_UTN = {'Habilidades_UTN': tupla_habilidades_UTN}
print(dic_habilidades_UTN)

# creo una variable que me permita acceder a la lista dentro de la key
lista_habilidades = dic_habilidades_UTN['Habilidades_UTN']
print(lista_habilidades)


i = 1
# recorro la lista con una variable
for habilidades_str in lista_habilidades:
    # esa variable va a contener un texto otras variables ---> uso el format
    # a cada variable le asigno el {} dentro del string
    # ese numero referencia a la posicion de lo que le voy a pasar como parametro en el () del format
    # habilidades_str = "habilidad {0}: {1} | Poder {2}".format(i, habilidades_str[0], habilidades_str[1])
    habilidades_str = f'habilidad {i}: {habilidades_str[0]} | Poder {habilidades_str[1]}'
    # habilidad 1: Vuelo | Poder 32
    print(habilidades_str)
    # incremento la i ---> para el numero de habilidad incremente para que la siguiente vuelta quede asi
    # habilidad 2: Vision-X | Poder 64
    i += 1


    
    


    



    
    
    








    


# A su vez, todas y cada una de las habilidades
#deben estar dentro de una lista de habilidades, la cual debe ser el valor de una key que conforme un 
# diccionario, como key par albergarlas usaremos “habilidades_UTN”.




# Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente.

# recorrer dicha lista imprimiendo sus valores,  conjuntamente con la key que integra dicha estructura de datos.


