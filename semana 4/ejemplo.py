class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def descontar_precio(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

# Creando un objeto Producto para el arroz
arroz = Producto("Arroz", 20, "Una arroba de arroz")