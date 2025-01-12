class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def descontar_precio(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

    def calcular_precio_total(self, cantidad):
        return self.precio * cantidad

# Creando un objeto Producto para el arroz
arroz = Producto("Arroz", 20, "Una arroba de arroz")

# Calculando el precio de 2 arrobas de arroz
precio_total = arroz.calcular_precio_total(2)
print("El precio total de 2 arrobas de arroz es:", precio_total)