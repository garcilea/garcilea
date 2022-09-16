from data_ import lista_bzrp
'''


[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]
1 - Tema mas visto
2 - Tema menos visto
3 - Tema mas largo
4 - Tema mas corto
5 - Duracion promedio de temas
6 - Promedio de vistas 
7 - Salir
'''
dic_test = {"a":22, "b":"Hola", "c":3}
print(dic_test) # {'a': 22, 'b': 'Hola', 'c': 3}

print(dic_test['a']) # 22

dic_test['a']=28
print(dic_test)

dic_test['j']=4
print(dic_test) # {'a': 28, 'b': 'Hola', 'c': 3, 'j': 4}

print(dic_test.items())
print(dic_test.values())

def mostrar_video(video:dict):
    print(f"- Titulo : {video['title']} \n- vistas: {video['views']/1000000:.2f} \n- duracion : {video['length']} \n- imagen : {video['img_url']} \n- url : {video['url']} \n- fecha : {video['date']}")



def calcular_maximo_minimo(lista:list,clave:str,tipo:str) -> dict:
    retorno = -1
    if type(lista) == type(list()) and type(clave) == type(str()) and type(tipo) == type(str()) and len(lista) > 0:
        max_min = lista[0]
        for video in lista:
            if tipo == "maximo" and video[clave] > max_min[clave]:
                max_min = video
            if tipo == "minimo" and video[clave] < max_min[clave]:
                max_min = video
        retorno = max_min
        
    return retorno


def calcular_tema_mas_visto():
    #---------TEMA MAS VISTO----------------
    """     video_maximo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["views"] >  video_maximo["views"]):
            video_maximo = video

    print("Video: {1} - Vistas: {0}".format(video_maximo["views"]/1000000,video_maximo["title"])) 
    
    """
    video = calcular_maximo_minimo(lista_bzrp,"views","maximo")
    mostrar_video(video)

    #-------------------------------------------

def calcular_tema_menos_visto():
    #---------TEMA MENOS VISTO----------------
    """ video_minimo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["views"] <  video_minimo["views"]):
            video_minimo = video

    print("Video: {1} - Vistas: {0}".format(video_minimo["views"]/1000000,video_minimo["title"])) """
    video = calcular_maximo_minimo(lista_bzrp,"views","minimo")
    mostrar_video(video)
    #-------------------------------------------  
def calcular_tema_mas_largo():
    #--------- TEMA MAS LARGO ----------------
    """ video_length_maximo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["length"] >  video_length_maximo["length"]):
            video_length_maximo = video

    print("Video: {1} - Tiempo: {0}".format(video_length_maximo["length"],video_length_maximo["title"])) """
    video = calcular_maximo_minimo(lista_bzrp,"length","maximo")
    mostrar_video(video)
    #-------------------------------------------
def calcular_tema_mas_corto():
    #--------- TEMA MAS CORTO ----------------
    """ video_length_minimo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["length"] <  video_length_minimo["length"]):
            video_length_minimo = video

    print("Video: {1} - Tiempo: {0}".format(video_length_minimo["length"],video_length_minimo["title"])) """
    video = calcular_maximo_minimo(lista_bzrp,"length","minimo")
    mostrar_video(video)
    #-------------------------------------------

def calcular_proedio(lista:list,clave:str):
    acumulador = 0
    for tema in lista:
        acumulador +=1
        acumulador += tema[clave]
    if clave == "length":
        print("Promedio: {2:.2f} - QTY: {0} - ACUM: {1} ".format(len(lista),acumulador, acumulador/len(lista)))
    if clave == "views":
        print("Promedio: {0:.2f} millones".format((acumulador/len(lista))/1000000))

    



def calcular_promedio_tiempo():
    # -------- PROMEDIO TIEMPO ------------
    """ acumulador_tiempo_videos = 0
    for tema in lista_bzrp:
        acumulador_tiempo_videos = acumulador_tiempo_videos +  tema["length"]

    print("Promedio: {2} - QTY: {0} - ACUM: {1} ".format(len(lista_bzrp),acumulador_tiempo_videos, acumulador_tiempo_videos/len(lista_bzrp))) """
    calcular_proedio(lista_bzrp,"length")

def calcular_promedio_vistas():
    # -------- PROMEDIO VISTAS ------------
    """ acumulador_vistas_videos = 0
    for tema in lista_bzrp:
        acumulador_vistas_videos +=  tema["views"]

    print("Promedio: {0:.2f} millones".format((acumulador_vistas_videos/len(lista_bzrp))/1000000)) """
    calcular_proedio(lista_bzrp,"views")

while True:
    respuesta = input("\n1 - Tema mas visto\n2 - Tema menos visto\n3 - Tema mas largo\n4 - Tema mas corto\n5 - Duracion promedio de temas\n6 - Promedio de vistas\n7 - Salir\n\n> ")
    if(respuesta == "1"):
        calcular_tema_mas_visto()
    elif(respuesta == "2"):
       calcular_tema_menos_visto()
    elif(respuesta == "3"):
        calcular_tema_mas_largo()
    elif(respuesta == "4"):
        calcular_tema_mas_corto()
    elif(respuesta == "5"):
        calcular_promedio_tiempo()
    elif(respuesta == "6"):
        calcular_promedio_vistas()
    elif(respuesta == "7"):
        break


































