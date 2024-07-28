#Implemente un programa que solicite al usuario una fracción, con
#formato X/Y, donde cada uno de X e Y es un número entero, y luego
#muestra, como un porcentaje redondeado al número entero más
#cercano, donde se indicará la cantidad de combustible en el
#tanque. Se debe tener en cuenta los siguientes casos:
#- Colocar E en caso X/Y sea menor a 1% del total
#- Colocar F en caso X/Y sea mayor a 99%.
#- En otro caso, devolver el valor en porcentaje %
#También debe tomar en cuenta los siguientes casos:
#- X y Y deben ser números enteros
#- X debe ser menor o igual a Y, y Y != 0
#De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
#cualquier excepción como ValueError o ZeroDivisionError.

def calcular_porcentaje(fraccion):
    try:
        X, Y = map(int, fraccion.split('/'))
        if Y == 0:
            raise ZeroDivisionError("Y no debe ser 0.")
        if X > Y:
            raise ValueError("X debe ser menor o igual a Y.")
        porcentaje = (X / Y) * 100
        if porcentaje < 1:
            return "E"
        elif porcentaje > 99:
            return "F"
        else:
            return f"{round(porcentaje)}%"
    except ValueError:
        raise ValueError("Debe ingresar números enteros en el formato X/Y.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Y no debe ser 0.")

def main():
    while True:
        fraccion = input("Ingrese una fracción (X/Y): ")
        try:
            resultado = calcular_porcentaje(fraccion)
            print(resultado)
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)
            print("Por favor, inténtelo de nuevo.")

if __name__ == '__main__':
    main()
