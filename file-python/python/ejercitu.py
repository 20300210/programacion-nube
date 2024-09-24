# producto escslar 
v1=(1,2,3)
v2=(-1,2,0)
pe=0
for i in range(len(v1)):
    pe+=v1[i]*v2[i]
print(pe)

# media y desviacion tipica
import numpy as np
muestra = input("Por favor, ingresa una muestra de números, separados por comas: ")
muestra = [float(x) for x in muestra.split(",")]
muestra = tuple(muestra)
media = np.mean(muestra)
desviacion_tipica = np.std(muestra)
print(f"Media: {media:}")
print(f"Desviación estándar: {desviacion_tipica:}")

# Muestra la media y la desviación típica
print("La media de la muestra es: ", media)
print("La desviación típica de la muestra es: ", desviacion_tipica)
# lista de empleados
nombre = ('ramon', 'pedro', 'albaro', 'juan', 'raul')
apellidos = ('perez', 'rosal', 'paez', 'petro', 'alvarez')
cargo = ('admin', 'supervisor', 'jefe de ventas', 'jefe', 'contador')
depar = ('departamento de control', 'departamonto de logistica', 'depertamento de marketing', 'direccion general', 'departamento financiero')

print("Nombre\t\tApellidos\t\tCargo\t\tDepartamento")
print("-" * 50)
for n1, a1, c1, d1 in zip(nombre, apellidos, cargo, depar):
    print(f"{n1}\t\t{a1}\t\t{c1}\t\t{d1}")