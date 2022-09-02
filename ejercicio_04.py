"""
Preparando todo para reclutar héroes y heroínas para la liga de la justicia, 
el departamento de HR dispone de una larga lista de justicieros pero solo tiene 
información detallada de algunos de ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista 
'heroes_para_reclutar' busque en el diccionario 'heroes_info' los que coincidan y los 
guarde en un nuevo diccionario para luego imprimir por consola todos sus datos. (id, origen, etc)
TIP: Las habilidades están repetidas, busca la manera de que en el resultado final no existan 
duplicados, que usarías para eso?
"""

from math import inf


heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]
 
heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
            },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}
mensaje = ""
for heroe in heroes_para_reclutar:
     #accedo al key del diccionario
    if heroe in heroes_info.keys():
        info_heroe = heroes_info[heroe]
        #traemos cada uno de sus datos del heroe o del key secundario
        id = info_heroe["ID"]
        origen = info_heroe["Origen"]
        identidad = info_heroe["Identidad"]
        habilidades_lista = info_heroe["Habilidades"]

        # eliminar duplicados y lo conviero a lista
        habilidades_unica = list(set(habilidades_lista))
        print("ID : ", id, ", codename: ", heroe )
        print("Identidad :", identidad, "Origen ", origen)         
        habilidades_str = ' | '.join(habilidades_unica)
        print("Habilidades: ", habilidades_str)
        
        """
        una forma mas basica de hacer 

        for habilidad in habilidades_unica:
            
            mensaje += "{0} |".format(habilidad)
            
        print("habilidad :", habilidad)
        
          """
        




            




        

       




