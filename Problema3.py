#Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
#“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
#Cree 2 objetos de tipo circulo y calcule su área.


import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

def main():
    # Creo los objetos de tipo CIRCULO
    circulo1 = CIRCULO(8)
    circulo2 = CIRCULO(18)

    # Cálculo del área de cada círculo
    area1 = circulo1.calcular_area()
    area2 = circulo2.calcular_area()

    
    print(f"El área del círculo con radio {circulo1.radio} es: {area1}")
    print(f"El área del círculo con radio {circulo2.radio} es: {area2}")

if __name__ == '__main__':
    main()
