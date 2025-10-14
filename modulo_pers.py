## MODULOS PERSONALIZADOS ##

def crear_libro(titulo, autor, año):
    """ Retorna un libro en forma de dict() """
    return {'titulo': titulo, 'autor': autor, 'año': año}

def agregar_libro(biblioteca, libro):
    """ Agrega el libro pasado como argumento a la lista de libros dentro de la biblioteca"""
    biblioteca.append(libro)

def buscar_libro(biblioteca, titulo):
    """ Busca un libro dentro de una lista 'biblioteca' """
    for libro in biblioteca:
        if libro['titulo'] == titulo:
            return libro
    return None

def mostrar_catalogo(biblioteca):
    for libro in biblioteca:
        print(f"Titulo: {libro['titulo']}\nAutor: {libro['autor']}\nAño: {libro['año']}\n-------------")

def otra_funcion():
    pass
        
pi = 3.14
