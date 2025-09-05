# entidades.py

class Autor:
    def __init__(self, nombre, biografia, cita_famosa):
        self.nombre = nombre
        self.biografia = biografia
        self.cita_famosa = cita_famosa
        self.libros = [] # Lista para guardar los libros que escribió

class Libro:
    def __init__(self, nombre, testamento, tipo, orden, cita_clave, autor):
        self.nombre = nombre
        self.testamento = testamento
        self.tipo = tipo
        self.orden = orden
        self.cita_clave = cita_clave
        self.autor = autor # Objeto de la clase Autor