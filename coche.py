class Coche:
    ruedas = 4

    # Constructor 
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # Métodos de instancia
    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando!!!")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando!")

    #Método de clase
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas += 1

    # Método estático
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        return velocidad * tiempo