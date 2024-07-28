#Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
#la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
#calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
#cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
#formato. (Los métodos de cadena le serán de utilidad)


def obtener_calificaciones():
    while True:
        entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
        try:
           
            calificaciones = [int(nota.strip()) for nota in entrada.split(',')]
            return calificaciones
        except ValueError:
            print("Error: Asegúrese de que todas las calificaciones sean números enteros y estén separadas por comas.")

def main():
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)

if __name__ == '__main__':
    main()

