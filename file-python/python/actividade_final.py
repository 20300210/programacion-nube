
#!Importamos todas las librerias a usar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#!extraemos nuestro fichero csv
dcp=pd.read_csv('E:\@LGORITMO\python\Data_Caso_Propuesto.csv', delimiter=',')
print(dcp)
print('\n____________________________________________________________________________________________\n')

#!pregunta objetivo
#!¿que características de los inmuebles hacen o afectan al momento de la venta en todas las diferentes ciudades y departammentos?

#!extraere el total de registros del DataFrame
registro_total=len(dcp)
print(f"total de registros en el DataFrame : \n{registro_total}")
print('\n____________________________________________________________________________________________\n')

#!extrere el total de columnas del DataFrame
print(f"total de columnas en el DataFrame : \n{dcp.columns}")
print('\n____________________________________________________________________________________________\n')

#!detallado de cada columna
print(f"detallado del DataFrame : \n{dcp.info()}")
print('\n____________________________________________________________________________________________\n')

#!Identifico cuáles de las columnas son categóricas y numéricas
columnas_categorias=dcp.select_dtypes(include=['object']).columns.tolist()
columnas_numericas=dcp.select_dtypes(include=['int64','float64']).columns.tolist()
print(f"columnas de tipo categoria : \n{columnas_categorias}")
print(f"columnas de tipo numerica : \n{columnas_numericas}")
print('\n____________________________________________________________________________________________\n')

#!Se Identifica en que columnas existen valores nulos
valores_nulos=dcp.isnull().sum()
#!filtramos las columnas con valores nulos
columnas_nulas=valores_nulos[valores_nulos>0]
print(f"columnas con valores nulos : \n{columnas_nulas}")
print('\n____________________________________________________________________________________________\n')

#!Identifico si existen registros duplicados
valores_duplicados=dcp.duplicated().sum()
print(f"total de registros duplicados : \n{valores_duplicados}")
print('\n____________________________________________________________________________________________\n')

#!Realice un reporte estadístico de los datos numéricos (media, moda, mediana, desviación estándar, cuartiles, 
# !entre otros que considere)aqui se filtran los datos y s ignoran las columnas no numéricas
#!media
media=dcp.select_dtypes(include=[float,int]).mean()
#!moda
moda=dcp.select_dtypes(include=[float,int]).mode().iloc[0]
#!mediana
mediana=dcp.select_dtypes(include=[float,int]).median()
#!desviacion estandar
desviacion_estandar=dcp.select_dtypes(include=[float,int]).std()
#!cuartiles
cuartile=dcp.select_dtypes(include=[float,int]).quantile([0.25,0.5,0.75])
#!maximo
maximo=dcp.select_dtypes(include=[float,int]).max()
#!minimo
minimo=dcp.select_dtypes(include=[float,int]).min()

#!creamos un DataFrame y mostrar el reporte estadistico
reporte_estadistico=pd.DataFrame({
    'Media':media,
    'Moda':moda,
    'Mediana':mediana,
    'Desviación Estándar':desviacion_estandar,
    'Cuartil 25%':cuartile.loc[0.25],
    'Cuartil 50%':cuartile.loc[0.5],
    'Cuartil 75%':cuartile.loc[0.75],
    'Máximo':maximo,
    'Mínimo':minimo
    })
print(f"Reporte Estadistico : \n{reporte_estadistico}")
print('\n____________________________________________________________________________________________\n')

#!Identifique columnas con valores erróneos filtramos los valores numericos de cada columna numerica
columnas_numerica=dcp.select_dtypes(include=[float,int]).columns
for columna in columnas_numerica :
    no_numericos=dcp[~dcp[columna].apply(lambda x:isinstance(x,(float,int)))]
    if not no_numericos.empty:
        print(f"valores encontrados en la columna : \n {columna} :\n {no_numericos}")

#! todos los valores faltantes se obtienen y se suman
valores_faltantes=dcp.isnull().sum()
print(f"Valores faltantes por columna : \n{valores_faltantes}")
print('\n____________________________________________________________________________________________\n')

#!Utilice gráficos para identificar valores atípicos filtramos todos los valores numericos
columnas_numerico=dcp.select_dtypes(include=(float,int)).columns
#!creamos un subplots para cada una de las columnas
num_subplots=len(columnas_numerico)
#!creamos una figura (fig) y una matriz de subplots (axs) y utilizamos la funcuon subplots de matplotlib
fig,axs=plt.subplots(len(columnas_numerico),1,figsize=(8,6*num_subplots))
#!se itera sobre cada columna y dubuja un boxplot
for i,columna in enumerate(columnas_numerico):
    sns.barplot(data=dcp, x=columna, ax=axs[i])
    axs[i].set_title(f'boxplot de {columna}')
#! se ajusta el diseño de los subplots
plt.tight_layout()
plt.show()
print('\n____________________________________________________________________________________________\n')

#!Realice histogramas de frecuencia utilizan solo las columnas numericas
columnas_numericos=dcp.select_dtypes(include=[float,int]).columns
#! se crea el histograma de frecuenci de las columnas numericas
for columna in columnas_numericos :
    sns.histplot(dcp[columna],bins=50)
    plt.title(f"histograma de frecuencia de {columna}")
    plt.xlabel(columna)
    plt.ylabel('frecuencia')
    plt.show()
print('\n____________________________________________________________________________________________\n')

#!Use la herramienta para gráficos para determinar correlación entre variables Seleccionar solo columnas numéricas
dcp_numerico=dcp.select_dtypes(include=[float,int])
#!realisamos la eliminacion de las columnas con una sola entrada
dcp_numerico=dcp_numerico.loc[:, dcp_numerico.nunique() > 1]
#!se remplaza valores infinitos o muy grades
dcp_numerico.replace([np.inf, -np.inf],np.nan,inplace=True)
#!se crea la matriz de correlación
matrix_correlacion=dcp_numerico.corr()

#!definimos los parametros
annot_param=True  #! se anotan los valores de correlacion
cmap_param='RdBu'  #!la paleta de colores
fmt_param='.2f'   #!formato de valores anotados en pulgadas
figsize_param=(10, 8)   #!tamaño de la figura en pulgadas
linewidths_param=0.5   #! grosor de las lineas que separan las seldas

#!se crea el mapa de calor de correlacion con los parametros ya definidos
plt.figure(figsize=figsize_param)
sns.heatmap(matrix_correlacion,annot=annot_param,cmap=cmap_param,fmt=fmt_param,linewidths=linewidths_param)
plt.title('mapa de calor de correlacion')
plt.show()
print('\n____________________________________________________________________________________________\n')

#!Realice y explique la eliminación de datos nulos y duplicados
# !Eliminan filas con valores nulos
datos_nulos=dcp.dropna()
print(f"eliminacion de datos nulos : \n{datos_nulos}")
print('\n____________________________________________________________________________________________\n')
#! eliminacion de datos duplicados
datos_duplicados=dcp.drop_duplicates()
print(f"eliminacion de datos duplicados : \n{datos_duplicados}")
print('\n____________________________________________________________________________________________\n')

#!Agrupe columnas que considere pueden generar información importante Seleccionan las columnas importantes que desen agrupar
columnas_importantes=['Area Construida','Area Terreno','Precio']
#!creamos un nuevo DataFrame con las columnas selecionadas
columnas_importante=dcp.loc[:, columnas_importantes]
print(f"columnas importantes : \n{columnas_importante}")
print('\n____________________________________________________________________________________________\n')

#!Cree nuevas columnas a partir de las existentes
#! creamos una columna llamada pricio por metro cuadrado de terreno
dcp['Precio_m2_Terreno'] = dcp.apply(lambda row: row['Precio'] / row['Area Terreno'] if row['Area Terreno'] > 0 else np.nan, axis=1)

#!creamos otra columna llamada precio por metro cuadrado construido
dcp['Precio m2 Construido'] = dcp.apply(lambda row: row['Precio'] / row['Area Construida'] if row['Area Construida'] > 0 else np.nan, axis=1)

#!creamos otra columna sobre la categoria del terreno
def categoria_terreno(area):
    if area < 1000:
        return 'pequeño'
    elif area < 10000:
        return 'mediano'
    else :
        return 'grande'

#! los valores infinitos reemplasandolos por NaN
dcp.replace([np.inf,-np.inf],np.nan,inplace=True)

print(f"nuevas columnas : \n{dcp}")
print('\n____________________________________________________________________________________________\n')

#!Identifique columnas que no aportan de acuerdo con su pregunta objetivo
columnas_irrelevantes=['Codigo','Precio m2 costruido','Categoria terreno',]
dcp=dcp.drop(columns=columnas_irrelevantes,errors='ignore')
print(f"se verifican las columnas restantes : \n {dcp}")