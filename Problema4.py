#Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
#ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
#atributos de la clase. Además cree una clase CUADRADO que heredé de rectangulo. Cree un
#objeto de tipo rectangulo y 1 de tipo cuadrado.

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        
        super().__init__(lado, lado)

rectangulo = RECTANGULO(6, 5)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")

cuadrado = CUADRADO(8)
print(f"Área del cuadrado: {cuadrado.calcular_area()}")

