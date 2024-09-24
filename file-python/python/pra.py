#batos csv
import pandas as pd
data={'first_name':['sigird','joe','theodoric','kennedy','beatrix'],
      'last_name':['mannock','hinners','rivers','donnell','parlett'],
      'age':[27,31,36,53,48],
      'amount_1':[7.17,1.90,1.11,1.41,6.69],
      'amount_2':[8.06, "?",5.90, "?","?"]}
datosDataFrame=pd.DataFrame(data)
print(datosDataFrame)
#acaba la implementacion
datosDataFrame.to_csv('example.csv')

#########################################################################################################
df=pd.read_csv('example.csv',header=None)
print(df)

########################################################################################################
df=pd.read_csv('example.csv',
               skiprows=1,
               names=['UID','first Name','last name','age','sale_#1','sale_#2'])
print(type(df['sale_#2'][2]))

########################################################################################################
df=pd.read_csv('example.csv',
               skiprows=1,
               names=['UID','first Name','last name','age','sale_#1','sale_#2'],
               na_values=['?'],
               index_col=['UID','first Name','last name'])
print(df)

#############################################################################################################
file=open("/personas.txt","r")
diccionario=[]
for linea in file:
  pal=linea.split(";")
  elemento={
      "id":pal[0],
      "nombre":pal[1],
      "apellido":pal[2],
      "nacimiento":pal[3]
  }
  diccionario.append(elemento)
file.close()
print(diccionario)

###################################################################################################################
import pandas as pd
data={'first_name':['sigird','joe','theodoric','kennedy','beatrix'],
      'last_name':['mannock','hinners','rivers','donnell','parlett'],
      'age':[27,31,36,53,48],
      'amount_1':[7.17,1.90,1.11,1.41,6.69],
      'amount_2':[8.06, "?",5.90, "?","?"]}
datosDataFrame=pd.DataFrame(data)
print(datosDataFrame)
#acaba la implementacion
datosDataFrame.to_excel('example.xlsx', sheet_name='example')

######################################################################################################################
data=["linea 1","linea 2","linea 3","linea 4","linea 5"]
fic=open("text_1","w")
for line in data:
  fic.write(line)
  fic.write("\n")
fic.close()
##########################################################################################################################

import pandas as pd

def process_stock_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Calculate the minimum, maximum, and average of each column
    result = pd.DataFrame({
        'Minimo': df.min(),
        'Maximo': df.max(),
        'Media': df.mean()
    })
    
    return result

# Example usage
file_path = '/content/cotizacion.csv'
result_df = process_stock_data(file_path)
print(result_df)

###############################################################################################################################
import pandas as pd

def cotizacion_data(fic_cot):
  df=pd.read_csv(fic_cot)
  df.replace({',':'.'}, regex=True, inplace=True)
  result=pd.DataFrame({
      'max':df.max(),
      'min':df.min(),
      'media':df.mean()
  })
  return result

fic_cot=open("/content/cotizacion.csv")
result_df=cotizacion_data(fic_cot)
print(result_df)

################################################################################################
import pandas as pd
def resumen_cotizacion(fichero):
    df=pd.read_csv(fichero,sep=';',desimal=',',thousands='.', index_col=0)
    return 

##########################################################################################################################################
#1.Generar un DataFrame con los datos del fichero.
import pandas as pd
titac=open('/content/titanic.csv')
df=pd.DataFrame(titac)

###########################################################################
#2.Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos 
#de las columnas, las 10 primeras filas y las 10 últimas filas.
print("dimensiones del DataFrame",df.shape)
print( )
print("el número de datos que contiene",df.describe())
print( )
#print(df.columns)
for column_name in df.columns:
  print("los nombres de sus columnas ",column_name)
print( )
print(df.index)
print( )
print(df.dtypes)
print( )
print(df.head(10))
print( )
print(df.tail(10))