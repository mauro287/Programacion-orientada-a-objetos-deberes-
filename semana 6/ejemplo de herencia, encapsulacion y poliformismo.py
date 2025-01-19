#Ejemplo de herencia, encapsulamiento y poliformismo
# clase:Molde para creer objetos
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre
        # Encapsulación
        self.edad = 0

    def hacer_sonido(self):
        pass  # Método abstracto
# herencia perro y gato heredan de animal
class Perro(Animal):
        def __init__(self, nombre, raza):
            super().__init__(nombre)
            self.raza = raza
# poliformismo
        def hacer_sonido(self):
            print("¡Guau!")
class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")
mi_perro = Perro("Firulais", "Labrador")
mi_gato = Gato("Garfield")

mi_perro.hacer_sonido()  # Imprime "¡Guau!"
mi_gato.hacer_sonido()  # Imprime "¡Miau!"