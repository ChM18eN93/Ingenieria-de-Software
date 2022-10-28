import pandas as pd

datos = pd.read_csv('C:/Users/YO/iris.data', header = None)
print(datos.head())
datos.to_excel('C:/Users/YO/iris.xlsx', sheet_name = 'pag', 
               engine = 'openpyxl')

datos3 = pd.read_excel('C:/Users/YO/sifer_07_2022.xlsx', index_col = 0, engine = 'openpyxl')

print(datos3.head())

df = pd.DataFrame(datos) # Cargar un Data.frame

print(df.head()) # Mostrar los 5 primeros registros
print(df.tail()) # Mostrar los 5 últimos registros
print(df.info()) # Mostrar información del DataFrame resumida
print(df.describe()) # Muestra la cantidad , media, ST, cuartiles, min y max
print(df[0]) # Muestra todos los datos de la primera fila
print(df.loc[1:5,[0, 1]]) # Muestra los primeros 5 de las columnas 0 y 1
print(df.iloc[1:5, 0:2]) # Muestra los primeros 5 datos de las columnas 0 y 1( excluye la 2)
print(df.iloc[1:5, 0:3]) # Muestra los primeros 5 datos de las columnas 0 y 1( excluye la 3)
print(df[df[0] > 0]) # Muestra todos los valors de la columna0 que sean mayores que 0
print(df[df[3].isin([2])]) # Muestra los datos de la columna 3 que contengan el valor 2
