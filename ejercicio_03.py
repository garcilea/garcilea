"""
Ejercicio Integrador 03

La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
Nombre de Heroína/Héroe
EDAD (mayores a 18 años)
Sexo ("m", "f" o "nb")
Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
El sexo y nombre de Heroe | Heroína de mayor edad.
La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
El promedio de edad entre Heroinas.
El promedio de edad entre Heroes de fuerza.
"""

nombre = ''
edad = 0
sexo = ''
habilidad = ''
respuesta = 's'
nombre_de_fuerza_mas_joven = ''
edad_mas_joven = 200
edad_mas_viejo = 18
sexo_de_mayor_edad = ''
nombre_de_mayor_edad = ''
promedio_edad_heroina = 0
acumulador_edad_heroina = 0
contador_heroinas = 0
promedio_edad_heroes_fuerza = 0
acumulador_edad_heroes_fuerza = 0
contador_heroes = 0
contador_heroinas_con_habilidad_magia_o_fuerza = 0


while respuesta == 's':

    nombre = input("Por favor ingrese su nombre : ")
   
    edad = int(input("Por favor ingrese la edad : "))

    while edad < 19 or edad == "":
        edad = int(input("Por favor ingrese la edad : "))
    
    sexo =  input("Por favor ingrese su sexo ['f', 'm', 'nb'] : ")

    while sexo != "f" and sexo != "m" and sexo != "nb" :
        sexo = input("Error. Por favor ingrese su sexo ['f', 'm', 'nb'] : ") 
    
    habilidad = input("Por favor ingrese su habilidad ['fuerza', 'magia', 'inteligencia'] : ")

    while habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia":
        habilidad = input("Por favor ingrese su habilidad ['fuerza', 'magia', 'inteligencia'] : ")

    if (sexo == 'f'):
      acumulador_edad_heroina += edad
      contador_heroinas += 1
      if (habilidad == 'fuerza' or habilidad == 'magia'):
         contador_heroinas_con_habilidad_magia_o_fuerza += 1  
    elif (sexo == 'm'):
        if( habilidad == 'fuerza'):
            acumulador_edad_heroes_fuerza += edad
            contador_heroes += 1
    
    if ( habilidad == "fuerza"):
        
        if (edad < edad_mas_joven) :
            edad_mas_joven = edad
            nombre_de_fuerza_mas_joven = nombre
    
    if (edad > edad_mas_viejo):
        edad_mas_viejo = edad
        nombre_de_mayor_edad = nombre
        sexo_de_mayor_edad = sexo


    respuesta = input("Si desea continuar escriba 's' ")

    
# punto 1
print("el nombre del heroe o heroina de fuerza mas joven es :", nombre_de_fuerza_mas_joven)

# punto 2
print("El nombre del heroe o heroina de mayor edad es : ", nombre_de_mayor_edad)
print("El sexo del heroe o heroina de mayor edad es : ", sexo_de_mayor_edad)

# punto 3
print("La cantidad de heroinas con habilidad de fuerza o magia son : ", contador_heroinas_con_habilidad_magia_o_fuerza)

# punto 4
promedio_edad_heroina = acumulador_edad_heroina / contador_heroinas
print("El promedio de edad de heroinas es : ", promedio_edad_heroina)

# punto 5
promedio_edad_heroes_fuerza = acumulador_edad_heroes_fuerza / contador_heroes
print("El promedio de edad de heroes de fuerza es : ", promedio_edad_heroes_fuerza)



    
