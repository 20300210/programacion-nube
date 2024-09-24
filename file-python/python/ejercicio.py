import locale
# Establecer la configuración local para el formato de moneda
locale.setlocale(locale.LC_ALL, '')
deposito=int(input("cuanto desea depositar: "))
años=int(input("a cuntos años: "))
interes=4
total=(deposito*(interes/100+1)**años)
total_d=(total*(interes/100+1)**años)
total_de=(total_d*(interes/100+1)**años)
#formato moneda
print("Total generado el primer año:", locale.currency(total, grouping=True))
print("Total generado el segundo año:", locale.currency(total_d, grouping=True))
print("Total generado el tercer año:", locale.currency(total_de, grouping=True))

#calculo media
import math
muestra = input("Por favor, ingresa una muestra de números, separados por comas: ")
muestra = muestra.split(",")
muestra = [float(i) for i in muestra]
muestra = tuple(muestra)
media = sum(muestra) / len(muestra)
varianza = sum((i - media) ** 2 for i in muestra) / len(muestra)
desviacion_tipica = math.sqrt(varianza)