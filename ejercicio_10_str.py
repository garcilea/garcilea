
import re
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str):
    retorno = "N/A"
    if nombre_heroe.count("-")>0:
        nombre_heroe.replace("-"," ")
    if nombre_heroe[0:4] != "the " and nombre_heroe != "":
        if nombre_heroe.count(" ")>0:   
            lista = nombre_heroe.split(" ")            
            lista1 = lista[0]
            lista2 = lista[1]
            lista1 = lista1[0:1]
            lista2 = lista2[0:1]
            retorno = f'{lista1}.{lista2}.'           
        else:
            lista = nombre_heroe.split()
            lista = lista[0] 
            lista = lista[0:1]
            retorno = f'{lista}.'  

    return retorno
            
    
    """
    nombre_heroe = nombre_heroe.replace("The ","")
    nombre_heroe = nombre_heroe.replace("the ","")
    nombre_heroe = nombre_heroe.replace("-"," ")
    nombre_heroe = nombre_heroe.upper
    nombre_heroe = nombre_heroe.strip()
    
    partes_nombre = nombre_heroe.split(" ")
    iniciales = ""
    for una_parte in partes_nombre:
        
        iniciales += una_parte[0] + "."




    
    """

def definir_iniciales_nombre(heroe:dict):
    retorno = False
    if type(heroe) == type({}) and 'nombre' in heroe.keys():
        nuevaclave = "iniciales"
        heroe[nuevaclave] = extraer_iniciales(heroe['nombre'])
        retorno = True
        
    return retorno



def agregar_iniciales_nombre(lista:list):
    mensaje = ""
    if type(lista) == type([]) and len(lista) > 0:
       
       for heroe in lista:
         retorno = definir_iniciales_nombre(heroe)
         if retorno == False:
            mensaje = "El origen de datos no contiene el formato correcto"
            return  mensaje
         else:
            mensaje = True
    
    return mensaje



def stark_imprimir_nombres_con_iniciales(lista:list):
    
    if type(lista) == type([]) and len(lista) > 0:
        
        for heroe in lista:
            agregar_iniciales_nombre(lista)
            print(f'* {heroe["nombre"]} ({heroe["iniciales"]})')
            
def generar_codigo_heroe(id_heroe:int,genero_heroe:str):
    retorno = "N/A"

    if type(id_heroe) == type(int()) and genero_heroe != "" and (genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB"):
        id_heroe = str(id_heroe)
        if genero_heroe == "M" or genero_heroe == "F":
          id_heroe = id_heroe.zfill(8)     
        else:
          id_heroe = id_heroe.zfill(7)

        string = f'{genero_heroe}-{id_heroe}'
        retorno = string

    return retorno
print(generar_codigo_heroe(12,lista_personajes[0]["genero"]))

def agregar_codigo_heroe(heroe:dict):
    retorno = False
    if heroe != {}:
        codigo = generar_codigo_heroe(12,heroe["genero"])
        print(codigo)
        heroe["codigo_heroe"] = codigo
        print(heroe)
        if len(codigo) == 10:
            retorno = True
        
    return retorno
       

 # agregar_codigo_heroe(lista_personajes[0]) # porque me da none ? ---> no habia puesto el return !!

# Falta 2.3
def stark_generar_codigos_heroes(lista_heroes:list[dict]):
    
    if len(lista_heroes)>0:
        for heroe in lista_heroes:
            if "genero" in heroe.keys() and type(heroe) == type(dict):
                codigo = agregar_codigo_heroe(heroe)

                
                  



    



def sanitizar_entero(numero_str:str):
    numero_str = numero_str.strip()
    
    lista_numero = re.findall("[0-9]",numero_str)

    if (len(re.findall("^[0-9]+$",numero_str))) > 0:
        return int(numero_str)
    elif (len(re.findall("[a-zA-Z.]+",numero_str))) > 0:
        return -1
    elif re.findall("^[-]",numero_str):
        return -2
    else:
        return -3

    
    
    
    
    
    
            
    
# como puedo saber si un num no puede convertirse a entero ?? retorno -3
# print(sanitizar_entero("0"))

def sanitizar_flotante(numero_str:str):
    
    numero_str = numero_str.strip()
    
    if len(re.findall("^[0-9.]+$",numero_str)) > 0:
        
        return float(numero_str)
    elif len(re.findall("[a-zA-Z]+",numero_str)) > 0:
        return -1
    elif re.findall("^[-]+",numero_str):
        return -2
    else:
        return -3

#print(sanitizar_flotante("hola"))  

    

def sanitizar_string(valor_str:str, valor_por_defecto:str):
    
    valor_por_defecto = "-"
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    if re.findall("[0-9]+",valor_str):
        return "N/A"
    elif re.sub("/", " ", valor_str):
        return valor_str
    elif re.findall("^[a-zA-Z]+$",valor_str):
        valor_str =  valor_str.lower()
        return valor_str
    elif re.findall("[' ']",valor_str) and valor_por_defecto == str():
        valor_str =  valor_str.lower()
        return valor_por_defecto
print(sanitizar_string("     HOLA ","hola"))

    

    
# 4.1

def generar_indice_nombres(lista_heroes:list):
    
    nombre = " "
    lista = []
    for heroe in lista_heroes:
        
        nombre = str(heroe['nombre'])
        nombre = nombre.split(" ")
        lista.append(nombre)
     
    
    print(lista)
# generar_indice_nombres(lista_personajes)       
    





    



       

    


    




















