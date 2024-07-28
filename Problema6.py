#Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
#Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
#método para agregar productos y otra para mostrar toda la lista de productos.
#Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
#agregar más atributos a los productos para que se puedan hacer otras funcionalidades.
#Cree 3 objetos de tipo producto y agregalos al catálogo. Colocar ejemplos empleandolos
#métodos de catálogo.

class Producto:
    def __init__(self, nombre, precio, año, categoria):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.categoria = categoria

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Año: {self.año}, Categoría: {self.categoria}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        filtrados = [producto for producto in self.productos if producto.año == año]
        return filtrados

    def filtrar_por_categoria(self, categoria):
        filtrados = [producto for producto in self.productos if producto.categoria == categoria]
        return filtrados

    def productos_en_rango_de_precio(self, precio_min, precio_max):
        filtrados = [producto for producto in self.productos if precio_min <= producto.precio <= precio_max]
        return filtrados


producto1 = Producto("Radiador hg56", 90.50, 2022, "Radiadores")
producto2 = Producto("Aceite de motor", 25.50, 2021, "Lubricantes")
producto3 = Producto("Llanta XLL", 60.77, 2024, "Neumáticos")

catalogo = Catalogo()
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos
print("Todos los productos:")
catalogo.mostrar_productos()

# Filtrar productos por año
print("\nProductos del año 2022:")
productos_2022 = catalogo.filtrar_por_año(2022)
for producto in productos_2022:
    print(producto)

# Filtrar productos por categoría
print("\nProductos en la categoría 'Radiadores':")
productos_radiadores = catalogo.filtrar_por_categoria("Radiadores")
for producto in productos_radiadores:
    print(producto)

# Filtrar productos por rango de precio
print("\nProductos con precio entre $10 y $30:")
productos_rango_precio = catalogo.productos_en_rango_de_precio(10, 70)
for producto in productos_rango_precio:
    print(producto)

