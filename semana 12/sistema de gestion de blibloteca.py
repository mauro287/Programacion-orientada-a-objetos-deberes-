# ejemplo de sistema para gestionar una biblioteca digital para abministar los libros
# definir la clase
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Constructor para crear un objeto Libro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Método para representar el objeto Libro como una cadena (para imprimir)
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        # Constructor para crear un objeto Usuario
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar los libros prestados al usuario

    def __str__(self):
        # Método para representar el objeto Usuario como una cadena
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        # Constructor para crear un objeto Biblioteca
        self.libros = {}  # Diccionario: ISBN (clave) -> Libro (valor) para búsquedas eficientes
        self.usuarios = set()  # Conjunto: IDs de usuarios únicos para garantizar unicidad
        self.usuarios_data = {} # Diccionario: ID (clave) -> Usuario (valor) para acceso rápido a usuarios

    def agregar_libro(self, libro):
        # Método para agregar un libro a la biblioteca
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro  # Almacena el libro en el diccionario usando el ISBN como clave
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        # Método para quitar un libro de la biblioteca
        if isbn in self.libros:
            del self.libros[isbn]  # Elimina el libro del diccionario usando el ISBN
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        # Método para registrar un nuevo usuario
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)  # Añade el ID del usuario al conjunto de IDs únicos
            self.usuarios_data[usuario.id_usuario] = usuario # Añade el usuario al diccionario de usuarios
            print(f"Usuario '{usuario.nombre}' registrado con ID {usuario.id_usuario}.")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        # Método para dar de baja un usuario
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)  # Elimina el ID del usuario del conjunto
            del self.usuarios_data[id_usuario] #Elimina el usuario del diccionario de usuarios
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        # Método para prestar un libro a un usuario
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios_data[id_usuario]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)  # Añade el libro a la lista de libros prestados del usuario
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print("El libro ya está prestado a este usuario.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        # Método para devolver un libro de un usuario
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios_data[id_usuario]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)  # Elimina el libro de la lista de libros prestados del usuario
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print("El libro no está prestado a este usuario.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libros(self, criterio, valor):
        # Método para buscar libros por título, autor o categoría
        resultados = []
        for libro in self.libros.values():  # Itera sobre los valores (libros) del diccionario
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        # Método para listar los libros prestados a un usuario
        if id_usuario in self.usuarios:
            usuario = self.usuarios_data[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9780061120084")
libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "9780451524935")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("Juan Pérez", "123")
usuario2 = Usuario("María García", "456")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro("123", "9780061120084")
biblioteca.prestar_libro("456", "9780451524935")

biblioteca.listar_libros_prestados("123")
biblioteca.listar_libros_prestados("456")

biblioteca.devolver_libro("123", "9780061120084")

biblioteca.buscar_libros("autor", "orwell")