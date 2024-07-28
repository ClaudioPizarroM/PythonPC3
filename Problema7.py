#Del ejercicio 2 del modulo 3

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

#  Usamos datos del ejemplo de experimentación
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

print("Puntos:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

print("\nCuadrantes:")
print(f"A está en el {A.cuadrante()}")
print(f"C está en el {C.cuadrante()}")
print(f"D está en el {D.cuadrante()}")

print("\nVectores:")
print(f"Vector AB: {A.vector(B)}")
print(f"Vector BA: {B.vector(A)}")

print("\nDistancias:")
print(f"Distancia AB: {A.distancia(B)}")
print(f"Distancia BA: {B.distancia(A)}")

distancia_origen_A = A.distancia(D)
distancia_origen_B = B.distancia(D)
distancia_origen_C = C.distancia(D)

if distancia_origen_A > distancia_origen_B and distancia_origen_A > distancia_origen_C:
    print("\nEl punto A está más lejos del origen.")
elif distancia_origen_B > distancia_origen_A and distancia_origen_B > distancia_origen_C:
    print("\nEl punto B está más lejos del origen.")
else:
    print("\nEl punto C está más lejos del origen.")

# Crear un rectángulo con los puntos A y B
rectangulo = Rectangulo(A, B)
print("\nRectángulo:")
print(f"Base: {rectangulo.base()}")
print(f"Altura: {rectangulo.altura()}")
print(f"Área: {rectangulo.area()}")
