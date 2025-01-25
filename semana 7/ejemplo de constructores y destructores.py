#definicion de clase
class Coche:
    """Clase que representa un coche"""
# Aplicacion del constructor
    def __init__(self, marca, modelo, año):
        """Constructor de la clase Coche.
        Inicializa los atributos del objeto.

        Args:
            marca (str): Marca del coche.
            modelo (str): Modelo del coche.
            año (int): Año de fabricación.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        print(f"Se ha creado un coche {marca} {modelo} del año {año}")
#aplicacion del destructor 
    def __del__(self):
        """Destructor de la clase Coche.
        Imprime un mensaje cuando el objeto es destruido.
        """
        print(f"El coche {self.marca} {self.modelo} ha sido eliminado.")

# Creación de objetos
coche1 = Coche("Toyota", "Corolla", 2023)
coche2 = Coche("Honda", "Civic", 2022)

# Eliminación de objetos
del coche1