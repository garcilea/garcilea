
import re
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str)->str:
    retorno = "N/A"
    if nombre_heroe != "" and len(nombre_heroe) > 0:
      
     nombre_heroe = nombre_heroe.strip()
     
     nombre_heroe = nombre_heroe.replace("The ","")
     nombre_heroe = nombre_heroe.replace("-"," ")
         
     nombre_heroe = nombre_heroe.upper()
     
     
    
     partes_nombre = nombre_heroe.split(" ")
     

     iniciales = ""
     for una_parte in partes_nombre:
        
        iniciales += una_parte[0] + "."

     retorno =  iniciales

   
    
    return retorno




""" if nombre_heroe.count("-")>0:
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

    return retorno """
            
    

   




    


def definir_iniciales_nombre(heroe:dict):
    retorno = False
    if (type(heroe) == type({}) and 'nombre' in heroe.keys()):
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
         else:
            mensaje = True
    
    return mensaje




def stark_imprimir_nombres_con_iniciales(lista:list):
    
    if type(lista) == type([]) and len(lista) > 0:
        
        for heroe in lista:
            agregar_iniciales_nombre(lista)
            print(f'* {heroe["nombre"]} ({heroe["iniciales"]})')


            
def generar_codigo_heroe(id_heroe:int,genero_heroe:str) -> str:
    retorno = "N/A"

    if type(id_heroe) == type(int()) and genero_heroe != "" and re.search("F|M|NB", genero_heroe,re.IGNORECASE):
        
        id_heroe = str(id_heroe)
        if genero_heroe == "M" or genero_heroe == "F":
          id_heroe = id_heroe.zfill(8)     
        else:
          id_heroe = id_heroe.zfill(7)

        string = f'{genero_heroe.upper()}-{id_heroe}'
        retorno = string

    return retorno
#print(generar_codigo_heroe(5,"m"))

def agregar_codigo_heroe(heroe:dict,id_heroe:int):
    retorno = False
    codigo = generar_codigo_heroe(id_heroe,heroe["genero"])
    if heroe != {} and len(codigo) == 10:
        
        
        heroe["codigo_heroe"] = codigo
                
        retorno = True
        
    return retorno
       

# agregar_codigo_heroe(lista_personajes[10],12) 

# Falta 2.3
def stark_generar_codigos_heroes(lista_heroes:list[dict]):
    
    if len(lista_heroes)>0:
        i = 0
        for heroe in lista_heroes:            
            if "genero" in heroe.keys() and type(heroe) == type({}):
                i += 1
                agregar_codigo_heroe(heroe,i)
                codigo = heroe['codigo_heroe']
                if i == 1:
                 mensaje = f'*  El codigo del primer heroe es:    {codigo}'
                 print(mensaje)
                if i == len(lista_heroes):                
                 mensaje = f'*  El codigo del ultimo heroe es:    {codigo}'
                 print(mensaje)
            else:
                mensaje = "El origen de datos no contiene el formato correcto"
                
    
# stark_generar_codigos_heroes(lista_personajes)

def sanitizar_entero(numero_str:str):
    numero_str = numero_str.strip()
    
   
    if (len(re.findall("^[0-9]+$",numero_str))) > 0:
        return int(numero_str)
    elif (len(re.findall("[a-zA-Z.]+",numero_str))) > 0:
        return -1
    elif re.findall("^[-]",numero_str):
        return -2
    else:
        return -3            

    
    
    
    
    
    
            

#print(sanitizar_entero("0"))

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
    

    if re.findall("[0-9]+",valor_str):
        return "N/A"
    elif re.sub("/", " ", valor_str):
        valor_str = re.sub("/", " ", valor_str)
        return valor_str
    elif re.findall("^[a-zA-Z ]+$",valor_str):
        valor_str = re.findall("^[a-zA-Z]+$",valor_str)
        valor_str =  valor_str.lower()
        return valor_str
    elif re.findall("[' ']",valor_str) and type(valor_por_defecto) == type(str()):
        valor_str =  valor_str.lower()
        return valor_por_defecto
#print(sanitizar_string(" ","hola")) 





    
# 4.1

def generar_indice_nombres(lista_heroes:list[dict]):
    
    if len(lista_heroes) > 0:     
     
     nombre_heroe = ""
     for heroe in lista_heroes:
        if type(heroe) == type({}) and  "nombre" in heroe.keys():           
          nombre_heroe += heroe['nombre'] + " "

     nombre_heroe = nombre_heroe.strip()
     nombre_heroe = nombre_heroe.replace(" ",",")  
     lista_nombres = nombre_heroe.split(",")
     return lista_nombres
     
   

#generar_indice_nombres(lista_personajes)         
  
    
#  4.2
def stark_imprimir_indice_nombre(lista:list) -> str:
    lista = generar_indice_nombres(lista)
    lista = "-".join(lista)
    
  

#   stark_imprimir_indice_nombre(lista_personajes)
def convertir_cm_a_mtrs(valor_cm:float): # 5.1
        
      
    if  type(valor_cm) == type(float()) :
        if valor_cm > 0:
          valor_mts = valor_cm / 100
          return f'{valor_mts} mts.'
    else:
        return -1

# print(convertir_cm_a_mtrs(100.00))

def generar_separador(patron,largo:int,imprimir:bool = True) -> str:
    
    if len(re.findall("[*-/{2}]",patron))<3 and len(re.findall("[*-/{2}]",patron)) >0 and (largo > 1 and largo < 236):
       retorno = patron * largo
    else : 
        return "N/A"   
    
    if not imprimir:
        return patron
    else:        
        return retorno

#print(generar_separador("*",10,))

# 5.3

def generar_encabezado(titulo:str) -> str:
    if not re.search("^[0-9]",titulo):
        titulo = titulo.upper()
        
        separador = generar_separador("*",20,)
        retorno = f'{separador} \n{titulo} \n{separador}'

        return retorno


def imprimir_ficha_heroe(heroe:dict):
    print(generar_encabezado("principal"))
    
    mensaje = f'NOMBRE DEL HEROE:   {heroe["nombre"]}{agregar_iniciales_nombre(heroe)} \n\n IDENTIDAD SECRETA:  {heroe["identidad"]}\n\n CONSULTORA: {heroe["empresa"]}\n\n CÓDIGO DE HÉROE:  {generar_codigo_heroe(5,heroe["genero"])}' 
    print(mensaje)     

    print(generar_encabezado("fisico"))



    generar_encabezado("señas particulares")

#imprimir_ficha_heroe(lista_personajes[5])

def  stark_navegar_fichas(lista:list):
    heroe = imprimir_ficha_heroe(lista[0])
    print(heroe)



    print(f'[1] Ir a la izquierda \n\n'
           '[2] Ir a la derecha \n\n' 
           '[3] Salir \n\n')
    respuesta = input("ingrese una opcion\n\n")
    while(True):
        if respuesta == 1:
               pass

        elif respuesta == 2:
          pass
        elif respuesta == 3:
            break
stark_navegar_fichas(lista_personajes)


        









 



    








    



       

    


    




















