class Vehiculo:

    def __init__(self, ruedas, marca, modelo, color):
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando!")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando!")

class Coche(Vehiculo):

    def __init__(self, ruedas, marca,modelo,color,dueño):
        super().__init__(ruedas, marca,modelo,color)
        self.dueño = dueño

    def bocina(self):
        print("PIIIIIIIIII")

    def acelerar(self):
        print("Ahora estoy acelerando desde Coche!")

class Bicicleta(Vehiculo):

    def acelerar(self):
        print("Ahora estoy acelerando desde Bicicleta!")
        

# un_coche = Coche(ruedas= 4, marca= "Toyota", modelo= "Corolla", color="Blanco", dueño= "Juan")
# un_coche.bocina()
# un_coche.acelerar()

# una_bici = Bicicleta(ruedas= 2, marca= "SLP", modelo= "Modelo", color="Blanco")
# una_bici.acelerar()

# print(f"Este auto {un_coche.marca} {un_coche.modelo} esta activo")
# print(f"Esta bici {una_bici.marca} {una_bici.modelo} esta activa")


class A:

    def __init__(self):
        print("Soy la clase A")

class B:

    def __init__(self):
        print("Soy la clase B")

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Soy la clase C")
        
## POLIMORFISMO ##

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 1/100)
        print(f"El sueldo anual de un empleado NORMAL es de {sueldoAnual}")

class Programador(Empleado):

    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 5/100)
        print(f"El sueldo anual de un PROGRAMADOR es de {sueldoAnual}")

class Diseñador(Empleado):

    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 3/100)
        print(f"El sueldo anual es de {sueldoAnual}")

empleados = [
    Empleado("Juan", 500),
    Programador("Ceci", 3000),
    Diseñador("Kevin", 1500),
    Empleado("Cesar", 2000)
]

def calculoSueldos():
    for empleado in empleados:
        empleado.calcularSueldoAnual()

# calculoSueldos()

## ENCAPSULAMIENTO ##
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.__pi = 3.1415

    def calcular_perimetro(self):
        return 2 * self.__pi * self.radio

    def calcular_area(self):
        return self.__pi * self.radio ** 2

    def __str__(self):
        return f"Este es un circulo de radio {self.radio}"

circulo_1 = Circulo(5)

# print(circulo_1.calcular_perimetro())
# print(circulo_1.calcular_area())

# print(f"El valor de PI es {circulo_1._Circulo__pi}") ## Forma de mostrar igualmente el valor (name mangling)
# print(circulo_1)

class Rectangulo:
    def __init__(self,ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def __str__(self):
        return f"El ancho del rectangulo es de {self.ancho}, el alto es de {self.alto}"

    def __add__(self, segundo):
        nuevo_ancho = self.ancho + segundo.ancho
        nuevo_alto = self.alto + segundo.alto
        return Rectangulo(nuevo_ancho, nuevo_alto)

rect_1 = Rectangulo(5,3)
rect_2 = Rectangulo(8,4)

rect_3 = rect_1 + rect_2
print(rect_3)


