'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones



def starwars_app():
    lista_personajes = funciones.cargar_json("C:/Users/A129159/Desktop/utn/Prog1/garcilea/examen/data.json")
    lista_a_mostrar = lista_personajes[:]
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Elija una de las opciones: \n")

        if(respuesta=="1"):
            key = "height"
            orden = input("Por favor elija la opcion 'up' para ordenar de menor a mayor or 'down' para ordenar contrariamente: \n")
            
            lista_a_mostrar = funciones.convertir_keys_a_entero(lista_personajes,key)
            lista_a_mostrar = funciones.ordenar_por_key(lista_personajes,orden,key).copy()
            funciones.mostrar_personaje(lista_a_mostrar,key)

        elif(respuesta=="2"):
            print(funciones.muestra_personaje_mas_alto_por_genero_masc(lista_personajes))
            print(funciones.muestra_personaje_mas_alto_por_genero_fem(lista_personajes))

        elif(respuesta=="3"):
            key = "mass"
            orden = input("Por favor elija la opcion 'up' para ordenar de menor a mayor or 'down' para ordenar contrariamente: \n")
            lista_a_mostrar = funciones.convertir_keys_a_entero(lista_personajes,key)
            lista_a_mostrar = funciones.ordenar_por_key(lista_personajes,orden,key).copy()
            funciones.mostrar_personaje(lista_a_mostrar,key)

        elif(respuesta=="4"):
            palabra = input("Por favor escriba algo relacionado al personaje: \n")
            key = input("En que key desea consultar ? : \n")
            funciones.buscar_personaje(lista_personajes,palabra)
        elif(respuesta=="5"):
            funciones.exportar_csv(lista_a_mostrar,"C:/Users/A129159/Desktop/utn/Prog1/garcilea/examen/data.csv",key)
        elif(respuesta=="6"):
            break
        else:
            print("\n")
            print("Vuelva a elegir una opcion \n")



starwars_app()

