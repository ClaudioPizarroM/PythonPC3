
from Problema10_libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_por_titulo(self, titulo):
        encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontró ningún libro con ese título.")

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontró ningún libro de ese autor.")
