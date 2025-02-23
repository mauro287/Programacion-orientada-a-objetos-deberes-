# Mejorar el sistema de gestión de inventarios desarrollado anteriormente
# sistema de Gestión de Inventarios Mejorado utilizando el anterior codigo
# Importa el módulo 'os' para trabajar con archivos y rutas
import os
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"  # Formato de precio con 2 decimales

class Inventario:
    def __init__(self, archivo_inventario="inventario.txt"):  # Constructor con parámetro para el nombre del archivo
        self.archivo_inventario = archivo_inventario  # Guarda el nombre del archivo
        self.productos = {}  # Diccionario para almacenar productos (clave: ID, valor: Producto)
        self.cargar_inventario()  # Carga el inventario desde el archivo al iniciar

    def cargar_inventario(self):  # Carga el inventario desde el archivo
        try:
            with open(self.archivo_inventario, "r") as archivo:  # Abre el archivo en modo lectura
                for linea in archivo:  # Itera sobre cada línea del archivo
                    id, nombre, cantidad, precio = linea.strip().split(",")  # Divide la línea en sus componentes
                    self.productos[int(id)] = Producto(int(id), nombre, int(cantidad), float(precio))  # Crea un objeto Producto y lo añade al diccionario
            print(f"Inventario cargado desde {self.archivo_inventario}")  # Mensaje de éxito
        except FileNotFoundError:  # Si el archivo no existe
            print(f"Archivo {self.archivo_inventario} no encontrado. Se creará al guardar.")  # Mensaje informativo
        except Exception as e:  # Si ocurre otro error
            print(f"Error al cargar el inventario: {e}")  # Mensaje de error

    def guardar_inventario(self):  # Guarda el inventario en el archivo
        try:
            with open(self.archivo_inventario, "w") as archivo:  # Abre el archivo en modo escritura (sobrescribe el contenido anterior)
                for producto in self.productos.values():  # Itera sobre los productos en el diccionario
                    archivo.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")  # Escribe la información del producto en una línea
            print(f"Inventario guardado en {self.archivo_inventario}")  # Mensaje de éxito
        except Exception as e:  # Si ocurre un error
            print(f"Error al guardar el inventario: {e}")  # Mensaje de error

    # ... (resto de métodos sin cambios significativos en este contexto)

# Ejemplo de uso
inventario = Inventario()  # Crea un objeto Inventario. Intenta cargar el inventario desde el archivo

# ... (resto del código de ejemplo sin cambios significativos)