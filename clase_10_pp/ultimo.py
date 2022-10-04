import re
import json
import ultimo_func

def ultimo_app():
    lista_heroes = ultimo_func.cargar_json("C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.json")
    lista_para_archivo = []

    while(True):
         
        ultimo_func.mostrar_menu()

        respuesta = input("Que opcion desea elejir ? : \n")

        if re.search("^1$",respuesta):
            
            top = input("Elija una cantidad de heroes a mostrar : \n")
            if top != "0" and (not re.search("^-[a-zA-Z]+$",top)):
                key = "fuerza"
                cantidad = ultimo_func.validar_entero(top,"^[0-9]+$")
                cantidad = ultimo_func.validar_largo_lista(lista_heroes,cantidad)
                lista_para_archivo = lista_heroes[:cantidad].copy()
                ultimo_func.mostrar_heroe(lista_para_archivo,key)
                

        elif re.search("^2$",respuesta):            
            orden = input("Por favor elija 'up' o 'down' : ")
            if re.match("up|down",orden,re.IGNORECASE):
                key = 'fuerza'
                lista_para_archivo = ultimo_func.ordenar_lista(lista_heroes,key,orden).copy()
                ultimo_func.mostrar_heroe(lista_para_archivo)
               

        elif re.search("^3$",respuesta):
          orden = input("Por favor elija 'up' o 'down' :  \n")
          orden = ultimo_func.validar_respuesta("^up|down$",orden)
          key = "altura"
          lista_para_archivo = ultimo_func.ordenar_lista(lista_heroes,key,orden).copy()
          ultimo_func.mostrar_heroe(lista_para_archivo,key)
                

        elif re.search("^4$",respuesta):
            key = input("Elija una key a consultar a que lista pertenece")
            orden = input(" Elja para consultar si quiere la lista de heroes por debajo del promedio o por encima - indique mayor o menor - ")
            lista_para_archivo = ultimo_func.promedio_key(lista_heroes,key,orden).copy()
            ultimo_func.mostrar_heroe(lista_para_archivo,key)

        elif re.search("^5$",respuesta):
            palabra = input("Elija un tipo de inteligencia para buscar heroes: \n")
            ultimo_func.buscar_por_palabra(lista_heroes,palabra)        
                            
        elif re.search("^6$",respuesta):
            ultimo_func.exportar_csv(lista_para_archivo,"C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.csv",key)
        elif re.search("^7$",respuesta):
            pass
        else:
            print("\n")
            print("Elija una opcion valida : \n")


ultimo_app()