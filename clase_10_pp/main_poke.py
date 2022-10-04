import re
import json
import func_poke


def poke_app():
    lista_poke = func_poke.cargar_json("C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_poke.json")
    lista_para_mostrar = lista_poke
    
    while(True):
        func_poke.imprimir_menu()
        
        respuesta = input("Por favor elija una opcion\n")
        

        if re.search(respuesta,"^1${1}"):
            key = "poder"
            top = input("Elija un numero a mostrar: ")
            top = func_poke.validar_entero(top,"^[0-9]+$")
            top = func_poke.validar_largo_lista(lista_poke,top)
            lista_para_mostrar = lista_poke[:top].copy()
            func_poke.mostrar_poke(lista_para_mostrar)

        elif re.search(respuesta,"^2${1}"):
            key = "poder"
            orden = input("Elija una opcion de ordenamiento: 'up' o 'down' ")
            if re.match("up|down",orden,re.IGNORECASE):
                lista_para_mostrar = func_poke.ordena_lista_poke_segun_key(lista_poke,key,orden).copy()
                func_poke.mostrar_poke(lista_para_mostrar)

        elif re.search(respuesta,"^3${1}"):
            key = "id"
            orden = input("Elija una opcion de ordenamiento: 'up' o 'down' ")
            if re.match("up|down",orden,re.IGNORECASE):
                lista_para_mostrar = func_poke.ordena_lista_poke_segun_key(lista_poke,key,orden).copy()
                func_poke.mostrar_poke(lista_para_mostrar,key)

        elif re.search(respuesta,"^4${1}"):
            key = input("Por favor elija una key: evoluciones | fortaleza | debilidad | tipo \n")
            orden = input("Por favor elija un orden : mayor o menor - al promedio \n")
            #lista_para_mostrar = func_poke.determina_promedio(lista_poke,key,orden).copy()
           

        elif re.search(respuesta,"^5${1}"):
            tipo = input("Elija un tipo que desee buscar\n")
            key = "tipo"
            tipo = func_poke.validar_respuesta("fuego|agua|volador|electrico",tipo)
            if  type(tipo) != type(None) :
                func_poke.buscar_por_tipo(lista_poke,tipo,key)

        elif re.search(respuesta,"^6${1}"):
            func_poke.exportar_csv(lista_para_mostrar,"C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_poke.csv",key)

        elif re.search(respuesta,"^7${1}"):
            break
        else:
            print("\n")
            print("Error vuelva a elegir : \n\n")






    


poke_app()