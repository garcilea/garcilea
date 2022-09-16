from data_stark import lista_personajes

"""
lista_personajes =
[
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
 
"""
def nombres_cada_heroe_masculinos():
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            print(heroe["nombre"])

def nombres_cada_heroe_femeninos():
    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            print(heroe["nombre"])

def superheroe_mas_alto_masculino():
    maximo_altura = float(lista_personajes[0])
    for heroe in lista_personajes:
         if heroe["genero"] == "M":
            
            if(float(heroe["altura"]) > maximo_altura['altura']):
                
                superheroe_mas_alto = heroe
    print(f' El nombre superheroe mas alto masculino es :{superheroe_mas_alto["nombre"]}')


def superheroe_mas_alto_femenino():
    maximo_altura_f = lista_personajes[3]
    for heroe in lista_personajes:
         if heroe["genero"] == "F":
            
            if(float(heroe["altura"]) > float(maximo_altura_f['altura'])):
                
                superheroe_mas_alto_f = heroe
    print(f' El nombre del superheroe mas alto femenino es : {superheroe_mas_alto_f["nombre"]}')

def superheroe_mas_bajo_masculino():
    
    superheroe_mas_bajo_masculino = lista_personajes[0]
    for heroe in lista_personajes:
         if heroe["genero"] == "M":
            
            if(float(heroe["altura"]) < float(superheroe_mas_bajo_masculino['altura'])):
                
                superheroe_mas_bajo_masculino = heroe
    print(f' El nombre del superhoroe mas bajo masculino es :{superheroe_mas_bajo_masculino["nombre"]}')


def superheroe_mas_bajo_femenino():
    superheroe_mas_bajo_femenino = float(lista_personajes[3])
    for heroe in lista_personajes:
         if heroe["genero"] == "F":
            
            if(float(heroe["altura"]) < (superheroe_mas_bajo_femenino["altura"])):
                
                superheroe_mas_bajo_femenino = heroe
    print(f' Nombre del superheroe mas bajo femenino es : {superheroe_mas_bajo_femenino["nombre"]}')


def altura_promedio_masculino():
    acumulador_altura = 0
    lista_genero_masculino = []
    for heroe in lista_personajes:
         if heroe["genero"] == "M":            
            lista_genero_masculino.append(heroe)          
            heroe["altura"] = float(heroe["altura"])
            acumulador_altura += heroe["altura"]

    len_lista_genero_masculino = len(lista_genero_masculino)
    print(len_lista_genero_masculino)
    print(f'El promedio de altura de heroes masculinos es {acumulador_altura/len_lista_genero_masculino:.2f}')
altura_promedio_masculino()
def altura_promedio_femenino():
    acumulador_altura_f = 0
    lista_genero_femenino = []
    for heroe in lista_personajes:
         if heroe["genero"] == "F":            
            lista_genero_femenino.append(heroe)            
            heroe["altura"] = float(heroe["altura"])
            acumulador_altura_f += heroe["altura"]

    len_lista_genero_femenino = len(lista_genero_femenino)
    print(len_lista_genero_femenino)
    print(f'El promedio de altura de heroes femeninos es {acumulador_altura_f/len_lista_genero_femenino:.2f}')
altura_promedio_femenino()

def nombre_heroes_puntos_c_hasta_g():
     superheroe_mas_alto_masculino()
     superheroe_mas_alto_femenino()     
     superheroe_mas_bajo_masculino()
     superheroe_mas_bajo_femenino()

def cantidad_heroes_por_color_ojos():
    lista_ojos = []

    for heroe in lista_personajes:
        lista_ojos.append(heroe['color_ojos'])
    
    lista_ojos = list(set(lista_ojos))

    for color in lista_ojos:
        cantidad_heroes_por_color_ojos = 0 
        for heroe in lista_personajes:
            if heroe["color_ojos"] == color:
               cantidad_heroes_por_color_ojos += 1
    
        print(f'cantidad de heroes {cantidad_heroes_por_color_ojos} y con color de ojos {color}')
    
    # usando diccionarios:
    """
    dic_ojos = {}

    for heroe in lista_personajes

    if heroe['color_ojos] not in dic_ojos.keys():
        dic_ojos[heroe['color_ojos]] = 1
    else
        dic_ojos[heroe['color_ojos]] += 1
    
    for color in dic_ojos.items():
        mensaje = f'color : {color[0]} - cantidad : {color[1]}
    print(mensaje)
          
    """



def cantidad_heroe_por_color_pelo():
    #uso dicc.
    dic_pelo = {}

    for heroe in lista_personajes:
        
        if heroe['color_pelo'] not in dic_pelo.keys():
            dic_pelo[heroe['color_pelo']] = 1
        else:
            dic_pelo[heroe['color_pelo']] += 1
    
    for clave, valor in dic_pelo.items():
        mensaje = f'color de pelo : {clave} - cantidad {valor}'
        print(mensaje)



def cantidad_por_tipo_inteligencia():
    dic_inteligencia = {}
    

    for heroe in lista_personajes:
        
        
        if heroe['inteligencia'] not in dic_inteligencia.keys():
            dic_inteligencia[heroe["inteligencia"]] = 1        
        else:
            dic_inteligencia[heroe["inteligencia"]] += 1

            
    for clave, valor in dic_inteligencia.items():
        if clave == "":
            clave = 'no tiene'
        mensaje = f'inteligencia : {clave} - cantidad : {valor}'
        print(mensaje)

cantidad_por_tipo_inteligencia()        

def lista_heroe_por_color_de_ojos():
   
    
    dic_nombre_ojos = {}

    for heroe in lista_personajes:
        if heroe['color_ojos'].title() not in dic_nombre_ojos.keys():
            lista_nombres = []
            lista_nombres.append(heroe['nombre'])
            dic_nombre_ojos[heroe['color_ojos']] = lista_nombres
        else:
            otra_lista = list(dic_nombre_ojos[heroe['color_ojos'].title()])
            otra_lista.append(heroe["nombre"])
            dic_nombre_ojos[heroe['color_ojos']] = otra_lista
      
    
    
    for clave, concepto in dic_nombre_ojos.items():
        mensaje = f'estos son los superheores {concepto}, con color de ojos {clave}'
        print(mensaje)
             
lista_heroe_por_color_de_ojos()



def agrupa_heroe_por_color_de_pelo():
    dic_pelo = {}

    for heroe in lista_personajes:
        if heroe['color_pelo'] not in dic_pelo.keys():
            lista = []
            lista.append(heroe['nombre'])
            dic_pelo[heroe["color_pelo"]] = lista
            
        else:
            otra_lista = list(dic_pelo[heroe["color_pelo"]])
            otra_lista.append(heroe['nombre'])
            dic_pelo[heroe["color_pelo"]] = otra_lista
            print(dic_pelo) 
    
    for clave, valor in dic_pelo.items():
        if clave == "":
            clave = "No tiene"
        mensaje = f'color de pelo : {clave} --> superheroes {valor}'
        print(mensaje) 

agrupa_heroe_por_color_de_pelo()
def agrupa_heroe_por_tipo_inteligencia():

    dic_inteligencia = {}

    for heroe in lista_personajes:
        if heroe['inteligencia'] not in dic_inteligencia.keys():
            lista = []
            lista.append(heroe['nombre'])
            dic_inteligencia[heroe['inteligencia']] = lista
        else:
            otra_lista = list(dic_inteligencia[heroe['inteligencia']])
            otra_lista.append(heroe['nombre'])
            dic_inteligencia[heroe['inteligencia']] = otra_lista
    
    for clave, valor in dic_inteligencia.items():
        if clave == "":
            clave = "No tiene"
        mensaje = f'tipo inteligencia {clave} - heroes : {valor}'
        print(mensaje)
# agrupa_heroe_por_tipo_inteligencia()  



""" 
while True:
    respuesta = input("\n1 - nombre de todos los superheroes genero masculino\n
                         2 - nombre de todos los superheroes genero femenino\n
                         3 -  superheroe mas alto masculino\n
                         4 - superheroe mas alto femenino\n
                         5 - superheroe mas bajo masculino\n
                         6 - superheroe mas bajo Femenino\n
                         7 - altura promedio masculino\n
                         8 - altura promedio femenino\n
                         9 - nombre de cada superheroe de item 3 a 6\n
                         10 - cantidad heroes por distintos color de ojos\n
                         11 - cantidad heroes por distintos color de pelos \n
                         12 - cantidad heroes por tipo inteligencia\n
                         13 - listar superheroe por distinto tipo de color de ojos\n
                         14 - Listar heroes por distintos color de pelos\n
                         15 - Listar heroes por tipo de inteligencia\n
                         16 - Salir\n\n> ")
    if(respuesta == "1"):
        nombres_cada_heroe_masculinos()   
    elif(respuesta == "2"):
        nombres_cada_heroe_femeninos()  
    elif(respuesta == "3"):
        superheroe_mas_alto_masculino()   
    elif(respuesta == "4"):
        superheroe_mas_alto_femenino()   
    elif(respuesta == "5"):
        superheroe_mas_bajo_masculino()        
    elif(respuesta == "6"):
        superheroe_mas_bajo_femenino()     
    elif(respuesta == "7"):
        altura_promedio_masculino()   
    elif(respuesta == "8"):
        altura_promedio_femenino()
    elif(respuesta == "9"):
        nombre_heroes_puntos_c_hasta_g()
    elif(respuesta == "10"):
        cantidad_heroes_por_color_ojos()
    elif(respuesta == "11"):
        cantidad_heroe_por_color_pelo()
    elif(respuesta == "12"):
        cantidad_por_tipo_inteligencia() 
    elif(respuesta == "13"):
        agrupa_heroe_por_color_de_ojos()
    elif(respuesta == "14"):
        agrupa_heroe_por_color_de_pelo()
    elif(respuesta == "15"):
        agrupa_heroe_por_tipo_inteligencia()
    elif(respuesta == "16"):
        break

 """