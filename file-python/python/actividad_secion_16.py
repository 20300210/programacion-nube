# calculando la media, minimo, maximo del fichero cotizacion.csv
import pandas as pd
def calculo_cotizacion(fichero):
  df=pd.read_csv(fichero,sep=';',decimal=',',thousands='.',index_col=0)
  return pd.DataFrame([df.min(), df.max(), df.mean()], index=['minimo','maximo','media'])

calculo_cotizacion('/content/cotizacion.csv')

###########################################################################################

# calculando datos del titanic
#1.Generar un DataFrame con los datos del fichero.
import pandas as pd
titanic_dato='/content/titaniccoma.csv'
titanic_df = pd.read_csv(titanic_dato, delimiter=';')

#2.Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
print("dienciones del DataFrame: ",titanic_df.shape,"\n")
print("el número de datos que contiene el DataFrame: \n",titanic_df.describe(),"\n")
print("las columnas del DataFrame: \n",titanic_df.columns,"\n")
print("las 10 primeras filas del DataFrame: \n",titanic_df.head(10),"\n")
print("las 10 ultimas filas del DataFrame: \n",titanic_df.tail(10),"\n")

#3.Mostrar por pantalla los datos del pasajero con identificador 148.
pasajero_148 = titanic_df[titanic_df['ID'] == 148]
print('pasajero 148: \n',pasajero_148.to_string(),'\n')
#3.Mostrar por pantalla las filas pares del DataFrame.
filas_pares= titanic_df.iloc[lambda x: x.index % 2 == 0]
print(filas_pares)

#4.Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
filtro_priclass = titanic_df[titanic_df['Pclass'] == 1]
ordenamos_nombre = filtro_priclass['Name'].sort_values()
print(ordenamos_nombre)

#5. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
total = len(titanic_df)
survived = len(titanic_df[titanic_df['Survived'] == 1])
died = len(titanic_df[titanic_df['Survived'] == 0])
print("porcentaje de personas que sobrevivieron : \n", survived / total * 100,'\n')
print("porsentaje de personas que murieron : \n", died / total * 100,'\n')

#5. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
personas_sobrevivientes=titanic_df.groupby('Pclass')['Survived'].mean() * 100
personas_sobrevivientes

#6. Eliminar del DataFrame los pasajeros con edad desconocida.
titanic_df_cleaned = titanic_df.dropna(subset=['Age'])
pasajeros_edad_desconocida = titanic_df[titanic_df['Age'].notna()]
pasajeros_edad_desconocida

#7. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
pasajeras_femeninas = titanic_df[titanic_df['Sex'] == 'female']
edad_media_mujeres = pasajeras_femeninas.groupby('Pclass')['Age'].mean()

print(edad_media_mujeres)

#7. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
pasajeras_femeninas = titanic_df[titanic_df['Sex'] == 'female']
edad_media_mujeres = pasajeras_femeninas.groupby('Pclass')['Age'].mean()

print(edad_media_mujeres)

#8.  Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
titanic_df['Menoredad']=titanic_df['Age'] < 18
print(titanic_df.to_string())

#9.  Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
titanic_df['Menoredad'] = titanic_df['Age'] < 18

def grupo_edades(age):
  if age < 18:
    return 'Menor'
  else:
    return 'Adulto'

titanic_df['AgeGroup'] = titanic_df['Age'].apply(grupo_edades)
tasa_supervivientes = titanic_df.groupby(['Pclass', 'AgeGroup'])['Survived'].mean() * 100

print(tasa_supervivientes)