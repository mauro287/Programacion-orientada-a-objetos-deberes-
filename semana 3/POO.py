class Dia:
  def __init__(self, temperatura):
    self.temperatura = temperatura

class Semana:
  def __init__(self):
    self.dias = []

  def agregar_dia(self, dia):
    self.dias.append(dia)

  def calcular_promedio(self):
    suma_temperaturas = sum(dia.temperatura for dia in self.dias)
    promedio = suma_temperaturas / len(self.dias)
    return promedio

# Creando una semana y agregando días
semana = Semana()
for dia in range(1, 8):
  temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
  semana.agregar_dia(Dia(temperatura))

# Calculando el promedio
promedio_semanal = semana.calcular_promedio()
print("El promedio de temperatura semanal es:", promedio_semanal)