## POO ##

# class Vacia:
#     pass

# obj = Vacia()
# obj_2 = Vacia()
# obj_3 = Vacia()
# obj.saludo = "hola"

# from coche import Coche

# Crear una instancia de la clase Coche 
# un_coche = Coche("Toyota", "Corolla", "Rojo")
# otro_coche = Coche("Chevrolet", "Onix", "Blanco")

# Acceder al estado de los atributos 
# print("Atributos del coche 1:")
# print(f"Marca: {un_coche.marca}\nModelo: {un_coche.modelo}\nColor: {un_coche.color}\nRuedas: {un_coche.ruedas}\n -------------")

# print("Atributos del coche 2:")
# print(f"Marca: {otro_coche.marca}\nModelo: {otro_coche.modelo}\nColor: {otro_coche.color}\nRuedas: {otro_coche.ruedas}\n -------------")

#Uso de los métodos
# un_coche.acelerar()
# un_coche.frenar()

# otro_coche.acelerar()
# otro_coche.frenar()

# print(un_coche.ruedas)

# otro_coche.incrementar_ruedas()
# print(un_coche.ruedas)

# print(Coche.calcular_distancia(100,2))


# class Perro:
#     def __init__(self, nombre, raza, poder):
#         self.nombre = nombre
#         self.raza = raza
#         self.poder = poder

# catdog = Perro("CatDog", "Pastór", "Super Velocidad")

# print(catdog.nombre)

import random

class Dado:

    def __init__(self , caras = 6):
        self.caras = caras

    def lanzar(self):
        return random.randint(1, self.caras)
    
dado_1 = Dado()
dado_2 = Dado(20)

print(dado_1.lanzar())
print(dado_2.lanzar())
