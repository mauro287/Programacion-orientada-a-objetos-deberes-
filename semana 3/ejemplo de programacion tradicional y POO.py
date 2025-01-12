def ingresar_temperaturas():
  temperaturas = []
  for dia in range(1, 8):
    temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
    temperaturas.append(temperatura)
  return temperaturas

def calcular_promedio(temperaturas):
  suma = sum(temperaturas)
  promedio = suma / len(temperaturas)
  return promedio

# Llamamos a las funciones
temperaturas_semanales = ingresar_temperaturas()
promedio_semanal = calcular_promedio(temperaturas_semanales)
print("El promedio de temperatura semanal es:", promedio_semanal)