import re
import func2





def stark_app():
    lista_heroes = func2.cargar_json("C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.json")
    lista_a_mostrar_copiada = lista_heroes.copy()
    func2.imprimir_menu()
    while(True):

        respuesta = input("Por favor elija una de las opciones: ")

        if re.match("^1$",respuesta):
            top = input("Por favor elija una cantidad de heroes a mostrar")
            
            cantidad_a_validar = func2.validar_entero(top,"^[0-9]+$")
            cantidad_a_validar = func2.validar_largo_lista(lista_heroes,cantidad_a_validar)
            lista_a_mostrar_copiada = lista_heroes[:cantidad_a_validar].copy()
            func2.mostrar_heroe(lista_a_mostrar_copiada)  
                  

        elif re.match("2",respuesta):
            orden = input("Desea orden de formas ascendente( escriba 'asc' ) o descendente (escriba 'des') ")
            if re.match("asc|des",orden):
              lista = func2.buscar_minimo_maximo_por_key(lista_heroes,"altura",orden)
              lista_a_mostrar_copiada =  func2.mostrar_heroe(lista,"altura")
              lista_a_mostrar_copiada = list(lista_a_mostrar_copiada).copy()

        elif re.match("3",respuesta):
            orden = input("Desea orden de formas ascendente( escriba 'asc' ) o descendente (escriba 'des') ")
            if re.match("asc|des",orden):
              lista = func2.buscar_minimo_maximo_por_key(lista_heroes,"fuerza",orden)
              func2.mostrar_heroe(lista,"fuerza")

        elif re.match("4",respuesta):
            lista = func2.heroes_superan_promedio(lista_heroes,"fuerza","mayor")
            print(lista)

        elif re.match("5",respuesta):
            lista = func2.lista_por_inteligencia(lista_heroes,"good")
            print(lista)

        elif re.match("6",respuesta):
            func2.exportar_csv(lista_a_mostrar_copiada,"C:/Users/A129159/Desktop/utn/Prog1/garcilea/clase_10_pp/data_stark.csv")
        
        elif re.match("7",respuesta):
              break

stark_app()