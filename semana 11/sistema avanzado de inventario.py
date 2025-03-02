import json  # Para almacenamiento en archivos JSON


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario
        self.precio = precio  # Precio del producto

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad  # Actualiza la cantidad del producto

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio  # Actualiza el precio del producto

    def to_dict(self):
        return {"ID": self.id_producto, "Nombre": self.nombre, "Cantidad": self.cantidad, "Precio": self.precio}


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos con ID como clave
        self.cargar_desde_archivo()  # Carga el inventario desde el archivo al iniciar

    def agregar_producto(self, producto):
        if producto.id_producto not in self.productos:
            self.productos[producto.id_producto] = producto
            print("Producto agregado con éxito.")
        else:
            print("El producto con este ID ya existe.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado con éxito.")
        else:
            print("El producto no existe en el inventario.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            print("Producto actualizado con éxito.")
        else:
            print("El producto no existe en el inventario.")

    def buscar_producto(self, nombre):
        encontrados = [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados if encontrados else "No se encontraron productos con ese nombre."

    def mostrar_todos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump([p.to_dict() for p in self.productos.values()], archivo, indent=4)
        print("Inventario guardado en archivo.")

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                productos_cargados = json.load(archivo)
                for p in productos_cargados:
                    self.productos[p["ID"]] = Producto(p["ID"], p["Nombre"], p["Cantidad"], p["Precio"])
                print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("No se encontró un archivo de inventario previo. Se inicia con un inventario vacío.")


# Menú interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            print(inventario.buscar_producto(nombre))

        elif opcion == "5":
            print(inventario.mostrar_todos())

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
