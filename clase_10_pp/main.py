import json
import re

import funciones


def stark_app():
    lista_heroes = funciones.cargar_json("C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.json")
    lista_para_mostrar = lista_heroes
    while(True):
        funciones.imprimir_menu()
        respuesta = input("Por favor seleccione una opcion: ")
        
        if re.search("^1{1}$",respuesta):
            key = 'fuerza'
            top = input("Elija un numero que desee consultar: ")
            if top != "0" and (not re.search("^-[a-zA-Z]+$",top)):
                top = funciones.validar_entero(top,"^[0-9]+$")
                top = funciones.validar_largo_lista(lista_heroes,top)
                lista_para_mostrar = lista_heroes[:top].copy()
                funciones.mostrar_heroe(lista_para_mostrar,key)

        if re.search("^2{1}$",respuesta):
            key = 'fuerza'
            orden = input("Por favor elija un orden: 'up' o 'down'")
            if funciones.validar_respuesta("up|down",orden):
                lista_para_mostrar = funciones.ordenar_lista_orden(lista_heroes,key,orden).copy()
                funciones.mostrar_heroe(lista_para_mostrar,key)

        elif re.search("^3{1}$",respuesta):
             key = 'altura'
             orden = input("Por favor elija un orden: 'up' o 'down'\n")
             if funciones.validar_respuesta("up|down",orden):
                lista_para_mostrar = funciones.ordenar_lista_orden(lista_heroes,key,orden).copy()
                funciones.mostrar_heroe(lista_para_mostrar,key)

        elif re.search("^4{1}$",respuesta):
            orden = input("Elija un orden: 'mayor' o 'menor'\n")
            key = input("Elija una key a consultar fuerza|peso|altura: \n")

            lista_para_mostrar = funciones.promedio_heroes(lista_heroes,key,orden)
            funciones.mostrar_heroe(lista_para_mostrar,key) 

        elif re.search("^5{1}$",respuesta):
            palabra = input("Buscar: good|average|high\n")
            palabra = funciones.validar_respuesta("good|average|high",palabra)
            funciones.buscar_heroe_por_inteligencia(lista_heroes,palabra)

        elif re.search("^6{1}$",respuesta):
            funciones.exportar_csv(lista_para_mostrar,"C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.csv",key)
        elif re.search("^7{1}$",respuesta):
            break
        else:
            print("\n Vuelva a elegir otra opcion\n")



    

stark_app()
