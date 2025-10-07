## LISTAS ##

lista = [ 'hola', 123 , True ]

lista_2 = ["Diego" , "Ceci", "Franco", "Cristian"]

lista_3 = [1, True, lista, "cadena", 1.5, lista_2]

# print("lista\notra linea\n3ra linea")
# print(lista_2)
# print(lista_3)


# print(lista_2[-1])

colores = ['blanco', 'negro' , 'celeste', 'rosa']
# print(colores)
# colores[-1]= 'rojo'
# print(colores)

colores.append('elemento_agregado')
# print(colores)

# nueva_lista = [123, 456, "hola", "info", 456]
# print(nueva_lista)

# nueva_lista.remove(456)
# print(nueva_lista)

tupla = ("Info", "Chaco", 2025)
# print(tupla[0])

conjunto = { "info", "chaco" , "info" , 2025 , 123 , 456 , 456 }
# print(conjunto)

# if "info" in conjunto:
#     print("'info' si existe en el conjunto")

diccionario = {
    "Marta" : 362400000,
    "Juan" : 362599999,
    "Pedro": 362455555,
    "Jose" : 379400000
}

# print(diccionario)

diccionario["Marta"] = 36241111111

# print(diccionario)

# for clave, valor in diccionario.items():
#     print(f"Clave: {clave}. Valor: {valor}")

## EJERCICIO FINAL DE CLASE ##

## Sistema de alumnos

# Lista de alumnos(cada alumno es un diccionario con datos)
alumnos = [
    {
        "nombre" : "Ceci", "apellido": "Rey", "materias": ("Matematicas", "Historia")
    },
    {
        "nombre" : "Pedro", "apellido": "Gomez", "materias": ("Matematicas", "Geografía")
    },
    {
        "nombre" : "Juan", "apellido": "Perez", "materias": ("Matematicas", "Programación")
    }
]

# Mostrar lista completa de alumnos
print("Lista completa de alumnos: ")
for alumno in alumnos:
    print(alumno)

print("-" * 10)

# Buscar un alumno por nombre
nombre = input("Ingrese el nombre del alumno: ")

encontrado = False

for alumno in alumnos:
    if alumno["nombre"].lower() == nombre.lower():
        print("Alumno encontrado!", alumno)
        encontrado = True
if not encontrado:
    print("Ese alumno no se encuentra en la Base de datos")
    
print("-" * 10)

# Mostrar todas las materias distintas ( usando set )
materias = set()
for alumno in alumnos:
    materias.update(alumno["materias"])

print("Materias distintas que se cursan: ", materias)

print("-" * 10)
# Contar cuantos alumnos cursan cada materia (usando dict)
conteo = {}
for alumno in alumnos:
    for materia in alumno["materias"]:
        conteo[materia] = conteo.get(materia, 0) + 1

print(" Cantidad de alumnos por materia: ")
for materia , cantidad in conteo.items():
    print(f"{materia}: {cantidad}")
print("-" * 10)