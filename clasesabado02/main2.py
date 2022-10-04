import func2
import re
def paulina_app():
    
    lista_videos = func2.abrir_json("C:/Users/A129159/Desktop/utn/Prog1/garcilea/clasesabado02/data_paulina.json")
    
    while(True):
        func2.imprimir_menu()
     
        respuesta = input("Que opcion dese elegir ?  ")
        respuesta = func2.validar_entero(respuesta,"^[1-6{1}]$")

        if respuesta == 1:
            top = input(" Elija una cantidad de heroes a mostrar: ")
            cantidad_a_validar = func2.validar_entero(top,"^[0-9]+$")
            cantidad_a_validar = func2.validar_largo_lista(lista_videos,cantidad_a_validar)
            if cantidad_a_validar != 0:
               lista_de_copia = lista_videos[:cantidad_a_validar]
               lista_de_copia = func2.mostrar_video(lista_de_copia)
        elif respuesta == 2:
            lista_por_duracion = func2.ordenar_videos_por_key(lista_videos,"length","up")
            func2.mostrar_video(lista_por_duracion,"length")            
        elif respuesta == 3:
            lista_por_duracion = func2.ordenar_videos_por_key(lista_videos,"views","up")
            func2.mostrar_video(lista_por_duracion,"views")
        elif respuesta == 4:
            func2.buscar_videos_por_titulo(lista_videos,"title","MENÚ")  
            
        elif respuesta == 5:
            func2.exportar_csv(lista_videos,"C:/Users/A129159/Desktop/utn/Prog1/garcilea/clasesabado02/data_paulina.csv","title")
        elif respuesta == 6:
            break
            
paulina_app()
