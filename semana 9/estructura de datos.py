# Desarrollar un sistema de gestion de inventarios
# Clase producto
# Definición de la clase Producto
class Producto:
 # Constructor de la clase
    def __init__(self, id, nombre, cantidad, precio):
# Atributo ID del producto
        self.id = id
# Atributo nombre del producto
        self.nombre = nombre
# Atributo cantidad del producto
        self.cantidad = cantidad
# Atributo cantidad del producto
        self.precio = precio
    def __str__(self):  #Método para mostrar información del producto
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:  # Definición de la clase Inventario
    def __init__(self):  # Constructor de la clase
        self.productos = []  # Lista para almacenar objetos Producto

    def añadir_producto(self, producto):  # Método para añadir un producto al inventario
        if self.buscar_producto(producto.id):  # Verifica si ya existe un producto con ese ID
            print("¡Error! Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)  # Añade el producto a la lista
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):  # Método para eliminar un producto por su ID
        producto = self.buscar_producto(id)  # Busca el producto en la lista
        if producto:  # Si el producto existe
            self.productos.remove(producto)  # Elimina el producto de la lista
            print("Producto eliminado correctamente.")
        else:
            print("¡Error! No existe ningún producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):  # Método para actualizar un producto
        producto = self.buscar_producto(id)  # Busca el producto en la lista
        if producto:  # Si el producto existe
            if cantidad is not None:  # Si se proporciona una nueva cantidad
                producto.cantidad = cantidad  # Actualiza la cantidad del producto
            if precio is not None:  # Si se proporciona un nuevo precio
                producto.precio = precio  # Actualiza el precio del producto
            print("Producto actualizado correctamente.")
        else:
            print("¡Error! No existe ningún producto con ese ID.")

    def buscar_producto(self, id):  # Método para buscar un producto por su ID
        for producto in self.productos:  # Itera sobre la lista de productos
            if producto.id == id:  # Si el ID del producto coincide con el ID buscado
                return producto  # Devuelve el objeto Producto
        return None  # Si no se encuentra el producto, devuelve None

    def buscar_productos_por_nombre(self, nombre):  # Método para buscar productos por nombre
        resultados = []  # Lista para almacenar los resultados de la búsqueda
        for producto in self.productos:  # Itera sobre la lista de productos
            if nombre.lower() in producto.nombre.lower():  # Si el nombre buscado está contenido en el nombre del producto (insensible a mayúsculas)
                resultados.append(producto)  # Añade el producto a la lista de resultados
        return resultados  # Devuelve la lista de resultados

    def mostrar_inventario(self):  # Método para mostrar todos los productos en el inventario
        if self.productos:  # Si la lista de productos no está vacía
            print("Inventario:")
            for producto in self.productos:  # Itera sobre la lista de productos
                print(producto)  # Muestra la información de cada producto
        else:
            print("El inventario está vacío.")

# Ejemplo de uso
inventario = Inventario()  # Crea un objeto Inventario

# Añadir productos
inventario.añadir_producto(Producto(1, "Camiseta", 10, 20.00))  # Añade una camiseta
inventario.añadir_producto(Producto(2, "Pantalón", 5, 35.00))  # Añade un pantalón
inventario.añadir_producto(Producto(3, "Zapatos", 8, 50.00))  # Añade unos zapatos

# Mostrar inventario
inventario.mostrar_inventario()  # Muestra el inventario actual

# Buscar productos por nombre
resultados = inventario.buscar_productos_por_nombre("a")  # Busca productos que contengan "a" en el nombre
if resultados:  # Si se encontraron resultados
    print("\nResultados de búsqueda:")
    for producto in resultados:  # Itera sobre los resultados
        print(producto)  # Muestra la información de cada producto

# Actualizar producto
inventario.actualizar_producto(2, cantidad=8)  # Actualiza la cantidad del pantalón

# Eliminar producto
inventario.eliminar_producto(1)  # Elimina la camiseta

# Mostrar inventario actualizado
inventario.mostrar_inventario()  # Muestra el inventario actualizado
