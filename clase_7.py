## FUNCIONES ##

def saludar():
    return "Hola mundo!"
    
# print(saludar())

def sumar(x, y):
    """ Esta función toma dos números y devuelve la suma de ellos. """
    return x + y

resultado = sumar(y=5,x=3)

# print(resultado)

def saludar(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

# print(saludar("Ceci","Chau"))

def receta(titulo, *args):
    print(f"Receta de {titulo}")
    print("Ingredientes:")

    for ingrediente in args:
        print(ingrediente)

# receta("Tarta", "Harina", "Aceite", "Frutillas", "Crema")

def suma(**kwargs):
    resultado = 0

    for clave, valor in kwargs.items():
        print(clave, "=", valor)
        resultado += valor

    return resultado

# print(suma(x=5,y=6,a=3))

## Alcance de las variables

mensaje = "Hola desde afuera"

def saludo():
    print(mensaje)

# saludo()
# print(mensaje)

def mostrar():
    texto = "Soy local"
    print(texto)

# mostrar()
# print(texto)

contador = 0 # global

def incrementar():
    global contador
    contador+=1

# incrementar()
# incrementar()
# print(contador)

x = "global"

def ejemplo():
    x = "local"
    print("Dentro de la función: ", x)

# ejemplo()
# print(f"Fuera de la función: {x}")
    