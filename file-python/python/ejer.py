import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)


#######################################################################################################


import pandas as pd

def analizar_notas(notas, nota_corte):
    """
    Analiza las notas de los estudiantes y determina quiénes están aprobados.
    
    Args:
    notas (dict): Un diccionario que contiene los nombres de los estudiantes como claves y sus respectivas notas como valores.
    nota_corte (float): La nota mínima requerida para aprobar.
    
    Returns:
    pandas.Series: Una serie que contiene las notas ordenadas de mayor a menor.
    pandas.Series: Una serie booleana que indica si cada estudiante está aprobado o no.
    """
    # Convertir el diccionario en una serie de pandas
    notas = pd.Series(notas)

    # Ordenar las notas de mayor a menor
    notas_ordenadas = notas.sort_values(ascending=False)

    # Determinar qué estudiantes están aprobados
    aprobados = notas >= nota_corte

    return notas_ordenadas, aprobados

# Definir las notas de los estudiantes
notas = {"juan": 3.5, "miguel": 4.5, "fran": 2.4, "jean": 1.0, "carlos": 1.2}

# Establecer la nota mínima requerida para aprobar
nota_corte = 3.0

# Llamar a la función y obtener los resultados
notas_ordenadas, aprobados = analizar_notas(notas, nota_corte)

# Imprimir resultados
print("Notas:")
print(notas_ordenadas)

print("\nEstudiantes aprobados:")
print(aprobados)


#########################################################################################################################

import pandas as pd

# Definir las notas de los estudiantes
notas = {"juan": 3.0, "miguel": 4.5, "fran": 2.4, "juan": 1.0, "carlos": 1.2}

# Convertir el diccionario en una serie de pandas
notas = pd.Series(notas, index=["juan", "miguel", "fran", "juan", "carlos"])

# Calcular la media de las notas
media = notas.mean()

# Determinar el criterio de aprobación (por ejemplo, nota de corte 3.0)
nota_corte = 3.0

# Crear una nueva serie que indique si los estudiantes están aprobados o no
aprobados = notas >= nota_corte

# Ordenar las notas de mayor a menor
notas_ordenadas = notas.sort_values(ascending=False)
print("Notas:")
print(notas_ordenadas)

print("\nEstudiantes aprobados:")
print(aprobados)

#################################################################################################################################


import pandas as pd

def notas_estudiantes(notas, nota_corte):
    notas = pd.Series(notas)
    notas_ordenadas = notas.sort_values(ascending=False)
    notas_apro = {}
    for estudiante, nota in notas_ordenadas.items():
        if nota >= nota_corte:
            notas_apro[estudiante] = "aprobado"
        else:
            notas_apro[estudiante] = "reprobado"
    return notas_ordenadas, notas_apro

# Definir las notas de los estudiantes
notas = {"juan": 1.0, "miguel": 4.5, "fran": 2.4, "jean": 5.0, "carlos": 1.2, "cris": 4.8}

# Establecer la nota mínima requerida para aprobar
nota_corte = 3.0

# Llamar a la función y obtener los resultados
notas_ordenadas, notas_apro = notas_estudiantes(notas, nota_corte)

# Imprimir resultados
print("Notas:")
print(notas_ordenadas)

print("\nEstado de aprobación de los estudiantes:")
for estudiante, estado in notas_apro.items():
    print(f"{estudiante}: {estado}")
    
    #ejercicios de panda
   # notas de estudiantes ordenadas,estado
    import pandas as pd
def notas_estudiantes(notas,notas_corte):
  notas = pd.Series(notas)
  notas_ordenadas=notas.sort_values(ascending=False)
  notas_aprobados={}
  for alumnos, nota in notas_ordenadas.items():
    if nota >= nota_corte:
      notas_aprobados[alumnos]="aprobado"
    else:
      notas_aprobados[alumnos]="reprobado"
  return notas_ordenadas,notas_aprobados

notas={"juan":1.0,"miguel":4.5,"fran":2.4,"jean":5.0,"carlos":1.2,"cris":4.8}
notas=pd.Series(notas)

nota_corte=3.0
notas_ordenadas, notas_aprobados = notas_estudiantes(notas, nota_corte)

print(notas_ordenadas)
estado_alumnos={}
for alumnos, estado in notas_aprobados.items():
  estado_alumnos[alumnos]=estado
  estado_alumnos=pd.Series(estado_alumnos)
print(estado_alumnos)

#balance de meses
import pandas as pd

def generar_tabla_balance(datos):
  
    contabilidad = pd.DataFrame(datos)
    contabilidad['Balance'] = contabilidad['ventas'] - contabilidad['Gastos']
    # Sumar balance total
    balance_total = contabilidad['Balance'].sum()
    tabla_meses = contabilidad[['mes', 'ventas', 'Gastos', 'Balance']]
    tabla_meses.loc[len(tabla_meses)] = ['Total', contabilidad['ventas'].sum(), contabilidad['Gastos'].sum(), balance_total]
    return tabla_meses

datos = {'mes': ['enero', 'febrero', 'marzo', 'abril'],
         'ventas': [30500, 35600, 28300, 33900],
         'Gastos': [22000, 23400, 18100, 20700]}

tabla_resultado = generar_tabla_balance(datos)
print(tabla_resultado)

#sin def
import pandas as pd

datos = {'mes': ['enero', 'febrero', 'marzo', 'abril'],
         'ventas': [30500, 35600, 28300, 33900],
         'Gastos': [22000, 23400, 18100, 20700]}


contabilidad = pd.DataFrame(datos)
contabilidad['Balance'] = contabilidad['ventas'] - contabilidad['Gastos']

balance_total = contabilidad['Balance'].sum()

tabla_meses = contabilidad[['mes', 'ventas', 'Gastos', 'Balance']]
tabla_meses.loc[len(tabla_meses)] = ['Total', contabilidad['ventas'].sum(), contabilidad['Gastos'].sum(), balance_total]

tabla_meses

#######################################################################################################################################################################
#alumnos
import pandas as pd

def obtener_estadisticas_notas(notas):
    if not notas:
        return {
            'nota_minima': None, 
            'nota_maxima': None,
            'nota_media': None,
            'desviacion_tipica': None
        }
    
    
    notas_serie = pd.Series(notas)

    nota_minima = notas_serie.min()
    nota_maxima = notas_serie.max()
    nota_media = notas_serie.mean()
    desviacion_tipica = notas_serie.std()
    
    return {
        'nota_minima': nota_minima,
        'nota_maxima': nota_maxima,
        'nota_media': nota_media,
        'desviacion_tipica': desviacion_tipica
    }

notas_alumnos = {
    'Juan': 85,
    'Maria': 92,
    'Luis': 78,
    'Ana': 95,
    'Carlos': 88
}

resultado = obtener_estadisticas_notas(notas_alumnos)
print(resultado)