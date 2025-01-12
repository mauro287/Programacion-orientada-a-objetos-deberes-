# ejemplo de una operacion matematica para sacar el radio de un circulo
import math
# aqui utilizamos el def para definir la funcion
def calcular_area_circulo(radio):
# especificamos la funcion
  """Calcula el área de un círculo dado su radio.

  Args:
    radio: El radio del círculo.

  Returns:
    El área del círculo.
  """
# agregamos una condicion para la funcion
  if radio <= 0:
#Agregamos raise para avaluar el error en caso de que la condicion no se cumpla
    raise ValueError("El radio debe ser un número positivo.")
  area = math.pi * radio**2
# return se utliza para devolver un valor o resultado al programa
  return area

# Asignar el valor del radio directamente
radio = 5

area = calcular_area_circulo(radio)
print("El área del círculo es: {:.2f} cm²".format(area))