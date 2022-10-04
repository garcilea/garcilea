import re
import func_stark

def stark_app():
    lista_heroes = func_stark.cargar_json("C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.json")
    lista_para_imprimir = []

    while(True):
        func_stark.imprimir_menu()
        respuesta = input("Que opcion desea elejir ?\n")

        if re.search("^1$",respuesta):
            top = input("escriba la cantidad de heroes a consultar:  \n")
            if top != "0":
                cantidad_a_validar = func_stark.validar_entero(top,"^[0-9]+$")
                cantidad_a_validar = func_stark.validar_largo_lista(lista_heroes,cantidad_a_validar)
                lista_para_imprimir = lista_heroes[:cantidad_a_validar].copy()
                func_stark.mostrar_heroe(lista_para_imprimir,"fuerza")
                key = "fuerza"

        elif re.search("^2$",respuesta):
            orden = input("Por favor ingrese 'up' para ordenar la lista de menor a mayor o 'down' en caso contrario\n")
            if re.match("up|down",orden):
                lista_para_imprimir = func_stark.ordenar_lista(lista_heroes,"altura",orden).copy()
                
                func_stark.mostrar_heroe(lista_para_imprimir,"altura")
                key = "altura"
                

        elif re.search("^3$",respuesta):
            orden = input("Por favor ingrese up o down\n")
            if re.match("up|down",orden):
                lista_para_imprimir = func_stark.ordenar_lista(lista_heroes,"fuerza",orden).copy()
                func_stark.mostrar_heroe(lista_para_imprimir,"fuerza")
                key = "fuerza"

        elif re.search("^4$",respuesta):
            
            orden = input("indique mayor o menor respecto al promedio\n")
            respuesta = input("indique una key : \n")
            
            if re.match("fuerza|altura|peso",respuesta) :
                lista_para_imprimir = func_stark.promedio_heroes(lista_heroes,respuesta,orden).copy()
                func_stark.mostrar_heroe(lista_para_imprimir,respuesta)
                key = respuesta

        elif re.search("^5$",respuesta):
            
            palabra = input("elija una palabra a buscar : ")
            print("\n")
            func_stark.lista_heroes_por_inteligencia(lista_heroes,palabra)

        elif re.search("^6$",respuesta):
            func_stark.exportar_csv(lista_para_imprimir,"C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.csv",key)
   
        elif re.search("^7$",respuesta):
            break
        else:
            print("\n")
            print("opcion incorrecta, vuelva a elejir\n")


stark_app()