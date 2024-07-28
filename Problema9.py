#Cree un menú que reutilice a manera de módulos las clases creadas en los ejercicios 3 y 4. El
#menú para utilizar deberá tener las siguientes funcionalidades:
#1. Calcular el área de un circulo
#2. Calcular el área de un rectangulo
#3. Calcular el área de un cuadrado
#4. Salir.
#Deberá emplear un método que valide que los datos ingresados sean números validos y
#positivos en caso corresponda.

# validamos el ingreso de los valores
def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Error: El valor debe ser positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Entrada no válida. Debe ingresar un número.")

# Importamos los modulos
from Problema3 import CIRCULO
from Problema4 import RECTANGULO, CUADRADO

def main():
    while True:
        print("\nMenú de Opciones:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            radio = validar_numero_positivo("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            print(f"El área del círculo es: {circulo.calcular_area()}")
        
        elif opcion == "2":
            largo = validar_numero_positivo("Ingrese el largo del rectángulo: ")
            ancho = validar_numero_positivo("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        
        elif opcion == "3":
            lado = validar_numero_positivo("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()

