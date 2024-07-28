# calculos

import Operaciones_Problema8

# Calculo de suma
resultado_suma = Operaciones_Problema8.suma(17, 5)
print(f"Suma: {resultado_suma}")

# Calculo de resta
resultado_resta = Operaciones_Problema8.resta(30, 8)
print(f"Resta: {resultado_resta}")

# Calculo del producto
resultado_producto = Operaciones_Problema8.producto(9, 1)
print(f"Producto: {resultado_producto}")

# Calculo de la división
resultado_division = Operaciones_Problema8.division(28, 7)
print(f"División: {resultado_division}")

# Pruebas con errores
print(Operaciones_Problema8.suma(10, "cinco"))  # Error de tipo
print(Operaciones_Problema8.division(10, 0))    # Error de división por cero
