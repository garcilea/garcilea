import json
import re
from ejercicio_08 import nombres_cada_heroe_masculinos
from ejercicio_08 import nombres_cada_heroe_femeninos
from ejercicio_08 import superheroe_mas_alto_masculino
from ejercicio_08 import superheroe_mas_alto_femenino
from ejercicio_08 import superheroe_mas_bajo_masculino
from ejercicio_08 import superheroe_mas_bajo_femenino
from ejercicio_08 import altura_promedio_masculino
from ejercicio_08 import altura_promedio_femenino
from ejercicio_08 import cantidad_heroes_por_color_ojos
from ejercicio_08 import cantidad_heroe_por_color_pelo
from ejercicio_08 import cantidad_por_tipo_inteligencia
from ejercicio_08 import agrupa_heroe_por_color_de_pelo
from ejercicio_08 import agrupa_heroe_por_tipo_inteligencia
from ejercicio_08 import agrupa_heroe_por_color_de_ojos
from ejercicio_08 import nombre_heroes_puntos_c_hasta_g



def imprimir_dato(cadena:str):
    if type(cadena) == type(str()):
        print(cadena)



def imprimir_menu_desafio_5():
    imprimir_dato( "A: nombre superheroe masculino \n"
                   "B: nombre superheroe femenino \n"
                   "C: Heroe M mas alto \n"
                   "D: Heroe F mas alto  \n"
                   "E: Heroe M mas bajo \n"
                   "F: Heroe F mas bajo \n"
                   "G: Altura promedio M \n"
                   "H: Altura promedio F \n"
                   "I: Nombre de cada heroe por cada uno de los puntos anteriores \n"
                   "J: cantidad heroes por color de ojos \n"
                   "K: cantidad heroes por color de pelo \n"
                   "L: cantidad heroes por tipo inteligencia\n"
                   "M: listar heroes agrupados por color de ojos \n"
                   "N: listar heroes agrupados por color de pelo \n"
                   "O: listar heroes agrupados por tipo de inteligencia \n"
                   "Z: Salir\n\n"
                                )

def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    respuesta = input("ingrese una letra para comenzar")
    if re.match("[a-oA-OzZ{1}]$",respuesta):
        return respuesta
    else:
        return -1

def stark_marvel_app_5(lista:list):
    respuesta = stark_menu_principal_desafio_5()
    while(True):
     if re.findall("a|A",respuesta):
        nombres_cada_heroe_masculinos()
     elif re.findall("b|B",respuesta):
        nombres_cada_heroe_femeninos()
     elif re.findall("c|C",respuesta):
        superheroe_mas_alto_masculino()
     elif re.findall("d|D",respuesta):
        superheroe_mas_alto_femenino()
     elif re.findall("e|E",respuesta):
        superheroe_mas_bajo_masculino()      
     elif re.findall("f|F",respuesta):
        superheroe_mas_bajo_femenino()
     elif re.findall("g|G",respuesta):
        altura_promedio_masculino()
     elif re.findall("h|H",respuesta):
        altura_promedio_femenino()
     elif re.findall("i|I",respuesta):
       nombre_heroes_puntos_c_hasta_g()
     elif re.findall("j|J",respuesta):
        cantidad_heroes_por_color_ojos
     elif re.findall("k|K",respuesta):
        cantidad_heroe_por_color_pelo()
     elif re.findall("l|L",respuesta):
        cantidad_por_tipo_inteligencia
     elif re.findall("m|M",respuesta):
        agrupa_heroe_por_color_de_ojos()
     elif re.findall("n|N",respuesta):
        agrupa_heroe_por_color_de_pelo()
     elif re.findall("o|O",respuesta):
        agrupa_heroe_por_tipo_inteligencia
     elif re.findall("z|Z",respuesta):
        break


#1.4
def leer_archivo(nombre_archivo:str):
    with open(nombre_archivo,"r") as archivo:
        resultado = json.load(archivo)
        resultado_dic = dict(resultado)
        resultado_lista = list[dict](resultado_dic["heroes"])

        return resultado_lista

"""
    
"""

lista_heroes = leer_archivo("C:/Users/A129159/Desktop/utn/Prog1/garcilea/data_stark.json")


# 1.5
def guardar_archivo(path_archivo:str,contenido:str):
   mensaje = ""
   flag = False
   with open(path_archivo,"w+") as archivo:
      archivo.writelines(contenido)
      flag = True
   
   if flag == True:
      mensaje = f'se creo el archivo: {path_archivo}'      
   else:
      mensaje = f'Error al crear el archivo: {path_archivo}'

   return mensaje

# 1.6

def capitalizar_palabras(varias_palabras:str):
   

   if re.findall("^[a-zA-Z ]+$",varias_palabras) == True:
      varias_palabras = varias_palabras.split(" ")
      i = 0
      for palabras in varias_palabras:
         varias_palabras[i] = palabras.capitalize()
         i +=1
      
      varias_palabras = " ".join(varias_palabras)
      return varias_palabras

print(capitalizar_palabras("hola leandro"))


      

   

       


   
   
   

   


# 1.7








