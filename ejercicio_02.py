"""
Ejercicio Integrador 02

La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
PESO: (entre 10 y 100 kilos)
PRECIO POR KILO: (mayor a 0 [cero]).
TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
El importe total a pagar, BRUTO sin descuento.
El importe total a pagar con descuento (Solo si corresponde).
Informar el tipo de alimento más caro.
El promedio de precio por kilo en total.

"""

peso = 0
precio_por_kilo = 0
tipo_alimento = " "
tipo_alimento_mas_caro = " "
promedio_de_precio_por_kilo_total = 0
respuesta = "s"
descuento = 0
importe_bruto_total = 0
acumulador_de_precios = 0
importe_bruto = 0
acumulador_de_kilos = 0 
descuento = 0
precio_neto_con_descuento = 0
si_corresponde_descuento = False
precio_alimento_caro = -1
contador_precio_por_kilo = 0


while respuesta == "s" :

    peso = int(input("cuanto pesa ? : "))

    while peso < 10 or peso > 100 : 
        peso = int(input("Podras decirme un peso entre 10 y 100 kg  ? : "))

    precio_por_kilo = int(input("cual es el precio por kilo ? : "))

    while precio_por_kilo < 1 : 
         precio_por_kilo = int(input("cual es el precio por kilo ? : "))
    
    tipo_alimento = input("Escriba un tipo de alimento [v, a , m ] ")

    while tipo_alimento != "v" and tipo_alimento != "a" and tipo_alimento != "m":
         tipo_alimento = input("Escriba un tipo de alimento [v, a , m ] ")

    importe_bruto = precio_por_kilo * peso

    contador_precio_por_kilo += 1
    acumulador_de_precios += precio_por_kilo

    importe_bruto_total += importe_bruto

    acumulador_de_kilos += peso

    if precio_por_kilo > precio_alimento_caro:
      precio_alimento_caro = precio_por_kilo
      tipo_alimento_mas_caro = tipo_alimento

    
    respuesta = input("Si Desea continuar escriba 's' ") 

# punto 1

print("El precio bruto total es : ", importe_bruto_total)

# punto 2
if acumulador_de_kilos > 100 and acumulador_de_kilos < 301:
    descuento = 15
    si_corresponde_descuento = True
elif acumulador_de_kilos > 300:
    descuento = 25
    si_corresponde_descuento = True

if si_corresponde_descuento == True:
   precio_neto_con_descuento = importe_bruto_total * (1-descuento/100)
   print("el precio neto con descuento es : ", precio_neto_con_descuento)

# punto 3
print("El tipo del alimento mas caro es : ",tipo_alimento_mas_caro)

# punto 4
promedio_de_precio_por_kilo_total = acumulador_de_precios/contador_precio_por_kilo
print("El promedio de precios de alimentos por kilo es : ", promedio_de_precio_por_kilo_total)









      





    


