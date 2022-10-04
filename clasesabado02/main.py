'''
1 - Listar TOP N videos
2 - Ordenar videos por duracion (UP/DOWN)
3 - Ordenar videos por cantidad de views (UP/DOWN)
4 - Buscar videos por título 
5 - Exportar lista de videos a CSV
6 - Salir

        {
            "title": "Papa rosti con salchicha parrillera 🥔#paparosti #salchicha #patatas #papa #recetadepapa #shorts",
            "views": 11432,
            "length": 42,
            "img_url": "https://i.ytimg.com/vi/ZGni3XkUEeU/hqdefault.jpg",
            "url": "https://youtube.com/watch?v=ZGni3XkUEeU",
            "date": "2022-09-20 00:00:00"
        }
'''
import re 
import func


def paulina_app():

    lista_videos = func.abrir_json("\Users\A129159\Desktop\utn\Prog1\garcilea\clasesabado02\data_paulina.json")

    while True:

        func.escribir_cadena("1- Listar Top N Videos: \n"
                             "2- Ordenar videos por duracion (UP/DOWN)\n"
                             "3- Ordenar videos por cantidad de views (UP/DOWN)\n"
                             "4- Buscar videos por título\n"
                             "5- Exportar lista de videos a CSV \n"
                             "6- Salir \n\n")
                             
        repuesta = input(" Por favor seleccione una opcion del menu: ")
        

        if re.findall("1",repuesta):
         top = input("cuantos videos desea mostrar ? ")
         if len(lista_videos) <= top:
           func.mostrar_videos(lista_videos[:top])
         else:
            return "Error! el numero supera la cantidad de videos mencionadas"
        elif re.findall("2",repuesta):
            func.buscar_min_max(lista_videos,"length","up")           

        elif re.findall("3",repuesta):
            func.buscar_min_max(lista_videos,"views","down")   
        
        elif re.findall("4",repuesta):
            func.buscar_por_titulo(lista_videos,"title","hola")

        elif re.findall("5",repuesta):
           func.exportar_csv(lista_videos)
        elif re.findall("6",repuesta):
            break 

paulina_app()
   
   