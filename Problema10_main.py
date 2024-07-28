
from Problema10_gestion import GestionBiblioteca
from Problema10_libro import Libro

def main():
    gestion = GestionBiblioteca()
    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("1. Agregar un libro")
        print("2. Listar los libros")
        print("3. Buscar un libro por título")
        print("4. Buscar un libro por autor")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado exitosamente.")
        elif opcion == '2':
            print("\n--- Lista de Libros ---")
            gestion.listar_libros()
        elif opcion == '3':
            titulo = input("Ingrese el título del libro: ")
            gestion.buscar_por_titulo(titulo)
        elif opcion == '4':
            autor = input("Ingrese el autor del libro: ")
            gestion.buscar_por_autor(autor)
        elif opcion == '5':
            print("Saliendo del sistema de biblioteca.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == '__main__':
    main()
