
def resolve_welcome(obj, info):
    return "Welcome to the libray!"

libros = {
    "1": {"id": "1", "titulo": "La ciudad de cristal", "autor": "Paul Auster", "genero": "Ficción", "year": 1985},
    "2": {"id": "2", "titulo": "El despertar", "autor": "Kate Chopin", "genero": "Ficción", "year": 1899},
    "3": {"id": "3", "titulo": "Matar a un ruiseñor", "autor": "Harper Lee", "genero": "Drama", "year": 1960},
    "4": {"id": "4", "titulo": "1984", "autor": "George Orwell", "genero": "Distopía", "year": 1949},
    "5": {"id": "5", "titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "genero": "Romance", "year": 1813},
    "6": {"id": "6", "titulo": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "genero": "Ficción", "year": 1925},
    "7": {"id": "7", "titulo": "Moby Dick", "autor": "Herman Melville", "genero": "Aventura", "year": 1851},
    "8": {"id": "8", "titulo": "Guerra y paz", "autor": "Leo Tolstoy", "genero": "Histórico", "year": 1869},
    "9": {"id": "9", "titulo": "El guardián entre el centeno", "autor": "J.D. Salinger", "genero": "Ficción", "year": 1951},
    "10": {"id": "10", "titulo": "El hobbit", "autor": "J.R.R. Tolkien", "genero": "Fantasía", "year": 1937},
    "11": {"id": "11", "titulo": "Macbeth", "autor": "William Shakespeare", "genero": "Tragedia", "year": 1606},
    "12": {"id": "12", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "genero": "Realismo Mágico", "year": 1967},
    "14": {"id": "14", "titulo": "El otoño del patriarca", "autor": "Gabriel García Márquez", "genero": "Ficción", "year": 1975}
}

def resolve_libroID(obj, info, id):
    return libros.get(id)

def resolve_libro_autor(obj, info, autor):
    return [libro for libro in libros.values() if libro["autor"] == autor]

def resolve_libro_genero(obj, info, genero):
    return [libro for libro in libros.values() if libro["genero"] == genero]

def resolve_ListaLibros(obj, info):
    return list(libros.values())