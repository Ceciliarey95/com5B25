## ESTRUCTURAS DE CONTROL DE FLUJO ##
## Condicionales:
## Operadores:
color_1 = 'Blanco'
color_2 = 'Negro'
color_3 = 'Negro'

# if color_1 != color_2 and color_2 != color_3: # La 1ra es Verdadera y la 2da es Falsa
#     print('Los colores 1 y 3 son iguales')
# elif color_1 == color_2:
#     print('Los colores 1 y 2 son iguales')
# else:
#     print('Los colores 2 y 3 son iguales')

# if color_1 != color_2:
#     if color_2 != color_3:
#         print('Los colores 1 y 3 son iguales')
#     else:
#         print('Los colores 2 y 3 son iguales')
# else:
#     print('Los colores 1 y 2 son iguales')

## EJEMPLOS ##

# Evaluamos la edad ingressada de un usuario y le decimos si es mayor de edad o no

# edad = int(input('Ingrese su edad: '))

# if edad >= 18 :
#     print('Es mayor de edad')
# else:
#     print('Es menor de edad')
    
# Evaluar un entero si es positivo, negativo o cero

# numero = int(input('Ingresa un numero entero: '))

# if numero > 0:
#     print(f"El numero {numero} es positivo")
# elif numero < 0:
#     print(f"El numero {numero} es negativo")
# else:
#     print(f"El numero es cero")
    
## Evaluar si es multiplo de 2 y 3 a la vez

# numero = int(input('Ingresa un numero entero: '))

# if numero % 2 == 0 and numero % 3 == 0:
#     print(f"El numero {numero} es multiplo de 2 y 3 a la vez")
# else:
#     print(f"El numero {numero} NO es multiplo de 2 y 3 a la vez")
    
## Multiples condiciones
## Evaluamos el caracter ingresado para dar una respuesta

# caracter = input('Ingresa un caracter: ')

# if caracter.isupper():
#     print('El caracter es una letra mayuscula')
# elif caracter.islower():
#     print('El caracter es una letra minuscula')
# elif caracter.isdigit():
#     print('El caracter es un numero')
# else:
#     print('El caracter es un caracter especial')


## BUCLES ##

## FOR 

# numeros = [1,2,3,4,5]

# for n in numeros:
#     print(n)

# cadena = "Informatorio"

# for letra in cadena :
#     print(letra)

# for x in range(1,50,2):
#     print(x)

# diccionario = {
#     'a': 1, 
#     'b': 2, 
#     'c': 3
#     }
# # Iterar sobre las claves
# for clave in diccionario:
#     print(clave)
# print("-" * 10)
# # Iterar sobre los valores
# for valor in diccionario.values():
#     print(valor)
# print("-" * 10)
# # Iterar sobre claves y valores
# for clave, valor in diccionario.items():
#     print(f"Clave: {clave}\nValor: {valor}\n -----")

# frutas = ["Manzana", "pera", "naranja"]

# for indice , fruta in enumerate(frutas):
#     print(f"Indice: {indice}\nFruta: {fruta}\n ------")

# edades = {"Ceci": 10 , "Cristian": 20, "Luis": 50}

# for indice , clave in enumerate(edades):
#     print(indice, clave, edades[clave])
# nombres= ["Juan", "Pedro", "Maria"]
# for nombre in nombres:
#     print(nombre)
#     if nombre == "Pedro":
#         print("Encontrado")
#         break

## WHILE ##

# contador = 1
# # Cortamos la ejecucion con Ctrl + C
# while contador <= 10 :
#     contador += 1
#     if contador == 5:
#         print('Se salta este paso') 
#         continue
#     print(contador) 
    
# Luego de la palabra reservada While tenemos la opcion de:
# Bool directo (True)
# Variable bandera: inicia en True y su valor cambia a False en algun momento para cortar la ejecucion
# Condicion que cambia 
# Salir con Break
# while True:
#     respuesta = input('Desea salir? Ingrese "s"')
#     if respuesta == 's':
#         break

# numero = int(input("Ingresa un numero : "))
# i = 1
# suma = 0

# while i <= numero:
#     suma += i
#     i += 1

# print(f"La suma de los numeros naturales del 1 al {numero} es: {suma}")

# numero = int(input('Ingresa un numero:'))
# i = 1

# while i <= 10:
#     print(f"{numero} x {i} = {numero*i}")
#     i += 1

# palabra = input("Ingresa una palabra: ")
# palabra_invertida = ""

# i = len(palabra) - 1

# while i >= 0:
#     palabra_invertida += palabra[i]
#     i -= 1

# print(f"La palabra que ingresaste invertida quedaria asi: {palabra_invertida}")

import random

# Generamos un numero del 1 al 10
numero_secreto = random.randint(1,10)
intentos = 0

while True:
    # Pedir al usuario que ingrese su adivinanza
    adivinanza = input("Introduce tu adivinanza: ")

    #Verificar que es un numero
    if not adivinanza.isdigit():
        print("Por favor, introduce un numero")
        continue

    #Convertir la entrada a int
    adivinanza = int(adivinanza)
    intentos += 1

    # Verificar la adivinanza
    if adivinanza < numero_secreto:
        print("Es un numero mas grande")
    elif adivinanza > numero_secreto:
        print("Es un numero mas chico")
    else:
        print(f"Felicitaciones! Adivinaste el numero en {intentos} intentos!!!")
        break
        
print("Gracias por jugar!")
