import os
os.system("clear")

print("Un dataframes de panda es a un diccionario lo que numpy es a una matriz nativa de python")
print("Es lo mismo en la base pero tiene funcionalidad extra")
print("Tiene keys que contienen listas")
print("Es una tabla donde las listas de cada key tienen que ser de la misma longitud")
print("Pandas trata los keys como columnas en lugar de filas, o sea que da vuelta la sintaxis de la declaración de un diccionario")
print("\n")
datos = {
    'alumno': ['Zutano', 'Mengano', 'Pepe' ,'Fulanito, Cosme', 'Maria'],
    'primer parcial': [7, 8,7,4, 10],
    'segundo parcial': [10,9,4,10,10],
    'observaciones':['ninguna','libre','ninguna','libre','oyente'],
    'DNI':[23000000, 12389100, 99999, 1001,30406011]
}

import pandas as pd
df = pd.DataFrame(datos)
print(df)


print("\n--------------------------------------------")
print("Se puede extraer las columnas o los índices\n")
print(list(df.columns))
print(list(df.index))

print("\n--------------------------------------------")
print("Se puede extraer columnas según el nombre de la columna\n")
print(type(df))
print("\n")
print(df['alumno'])
print("\n")
print(type(df['alumno']))


print("\n--------------------------------------------")
print("Se puede extraer filas según el índice\n")
print(df.loc[2])
print("\n")
print(df.loc[2:4])


print("\n--------------------------------------------")
print("Estos índices se pueden setear al construir el dataframe\n")
datos = {
    'alumno': ['Zutano', 'Mengano', 'Pepe' ,'Fulanito, Cosme', 'Maria'],
    'primer parcial': [7, 8,7,4, 10],
    'segundo parcial': [10,9,4,10,10],
    'observaciones':['ninguna','libre','ninguna','libre','oyente'],
    'DNI':[23000000, 12389100, 99999, 1001,30406011]
}
df = pd.DataFrame(datos, index=['uno',3,'cinco',7,'nueve'])
df.loc['uno']
print(df)
print("\n")
print(df.loc[[7,'uno']])

print("\n--------------------------------------------")
print("Se puede setear que un campo de cada fila sea el índex, para cosas como ids, dnis, emails únicos, etc\n")
df_DNI = df.set_index('DNI')
print(df_DNI)


print("\n--------------------------------------------")
print("Una ventaja del dataframe son los métodos que tiene para la limpieza de datos")
print("'dropna' elimina las cosas que tienen NaN en algún campo")
print("Argumentos:")
print("\tinplace\tMuta el dataframe en lugar de crear uno nuevo")
print("\taxis\t0 para filas (default), 1 para columnas")
print("\thow\tCriterio para los NaN. Ejemplo how=all dropea si toda la fila o columna tiene solo NaNs")
print("\tsubset\tBusca NaN solo en las columnas definidas")

import numpy as np # necesito numpy para escribir nan
datos = {
    'alumno': ['Zutano', 'Mengano', 'Zutano','Pepe' ,'Fulanito, Cosme', 'Maria'],
    'primer parcial': [7, 8,7,7,np.nan, 10],
    'segundo parcial': [10,9,10,4,10,np.nan],
    'observaciones':['ninguna','libre','ninguna','ninguna','libre','oyente'],
    'DNI':[23000000, 12389100,23000000, 99999, 1001,30406011]
}
df = pd.DataFrame(datos)
print("\n")
print(df)
print("\n")
print(df.dropna(axis=0))
print("\n")
print(df.dropna(how='all'))
print("\n")
print(df.dropna(subset=['primer parcial','observaciones']))
print("\n")
print(df.dropna(axis=1, subset=[4]))

print("\n--------------------------------------------")
print("fillna reemplaza los NaNs por un valor\n")
print(df.fillna(999))


print("\n--------------------------------------------")
print("Es normal que para reemplazar campos así se use un promedio los valores de esa columna")
print("Para eso se calcula la media con 'mean' (no con un for a mano)\n")
a = df['primer parcial']
print(a)
print("\n")
mean = a.mean()
print("Media -> ", mean)
print("\n")
print(df.fillna(mean))


print("\n--------------------------------------------")
print("fillna llena todos los NaN con el valor calculado, no solo los de la columna de la que se calculó la media")
print("Para reemplazar los NaNs con un promedio de su columna correspondiente")
print("\tse crea un diccionario con las keys y los promedios, y se le pasa a fillna\n")
a = df['primer parcial']
b = df['segundo parcial']
meanPrimerParcial = a.mean()
meanSegundoParcial = b.mean()
print("Media de primer parcial -> ", meanPrimerParcial)
print("Media de segundo parcial -> ", meanSegundoParcial)
print("\n")
fill_dict = {
    'primer parcial': meanPrimerParcial,
    'segundo parcial': meanSegundoParcial
}
df_4 = df.fillna(fill_dict)
print(df_4)

print("\n--------------------------------------------")
print("Filtrar por condiciones en lugar de NaNs\n")

datos = {
    'alumno': ['Zutano', 'Mengano', 'Zutano','Pepe' ,'Fulanito, Cosme', 'Maria'],
    'primer parcial': [7, 8,7,7,np.nan, 10],
    'segundo parcial': [10,9,10,4,10,np.nan],
    'observaciones':['ninguna','libre','ninguna','ninguna','libre','oyente'],
    'DNI':[23000000, 12389100,23000000, 99999, 1001,30406011]
}
df = pd.DataFrame(datos)

for x in df.index:
  if not df.loc[x, "observaciones"] == 'libre':
    df.drop(x, inplace = True)
print("1")
print(df)
print("\n")

df = pd.DataFrame(datos)

print("2 - Este método de indexar 2 veces es más eficiente que el for")
df_libre = df[df['observaciones']=='libre']
print(df_libre)
print("\n")

df = pd.DataFrame(datos)

for x in df.index:
  if df.loc[x, "primer parcial"] <= 7:
    df.drop(x, inplace = True)
print("3")
print(df)
print("\n")


print("\n--------------------------------------------")
print("'drop_duplicates' elimina duplicados en un dataframe y también usa las demás opciones de dropna y fillna\n")
datos = {
    'alumno': ['Zutano', 'Mengano', 'Zutano','Pepe' ,'Fulanito, Cosme', 'Maria'],
    'primer parcial': [7, 8,7,7,np.nan, 10],
    'segundo parcial': [10,9,10,4,10,np.nan],
    'observaciones':['ninguna','libre','ninguna','ninguna','libre','oyente'],
    'DNI':[23000000, 12389100,23000000, 99999, 1001,30406011]
}
df = pd.DataFrame(datos)
print(df)
print("\n")
print(df.drop_duplicates())


print("\n--------------------------------------------")
print("'value_counts' se comporta como un select distinct count en sql")
print("Devuelve un histograma\n")
print(df['observaciones'].value_counts())


print("\n--------------------------------------------")
print("'pd.concat' sirve para concatenar dataframes")
print("Sin embargo también concatena los índices tal cual están en lugar de calcularlos incrementalmente")
print("Para concatenar calculando índices únicos usar la opcion 'ignore_index'\n")

datos_1 = {
    'alumno': ['Zutano', 'Mengano', 'Zutano','Pepe' ,'Fulanito, Cosme', 'Maria'],
    'primer parcial': [7, 8,7,7,np.nan, 10],
    'segundo parcial': [10,9,10,4,10,np.nan],
    'observaciones':['ninguna','libre','ninguna','ninguna','libre','oyente'],
    'DNI':[23000000, 12389100,23000000, 99999, 1001, 30406011]
}
df_1 = pd.DataFrame(datos_1)

datos_2 = {
    'alumno': ['Diego', 'Flor', 'José'],
    'primer parcial': [10,10,8],
    'segundo parcial': [8,8,8],
    'observaciones': ['ninguna','libre','libre'],
    'DNI': [23299, 1043101,4406533]
}
df_2 = pd.DataFrame(datos_2)

df_3 = pd.concat([df_1, df_2])
print(df_3)

print("\n")
df_3 = pd.concat([df_1, df_2], ignore_index=True)
print(df_3)


print("\n--------------------------------------------")
print("Siempre se puede reindexar un dataframe con reindex\n")
print(df_3.reindex(index=list(range(1,len(df_3)))))


print("\n--------------------------------------------")
print("'pd.merge' para unir dataframes con campos diferentes")
print("En este caso se hace por los índices")
print("Algunas personas están en ambos dataframes entonces tendrán datos de ambos, mientras que otras solo de uno de ellos")
print("O sea como un diagrama de Venn")
print("how puede ser 'inner' (interseccion) u 'outer' (union), entre otros menos comunes")
print("\tObviamente al hacer una unión va a haber un montón de campos NaN porque no hay datos")
datos_1 = {
    'alumno': ['Roberto', 'Mengano', 'Carlos','Marisol' ,'Fulanito, Cosme'],
    'cuota al día': ['sí','sí','no','no','sí'],
    'año que cursa': [2, 2, 2, 1, 4]
}
df_1 = pd.DataFrame(datos_1, index=[3934444, 12389100, 2939393, 10102394,1001])
print(df_1)
print("\n\t\t\t+\n")
print(df_DNI)
print("\n")

df_all = pd.merge(df_DNI,df_1, how="outer")
print("how=outer")
print(df_all)
print("\n")
print("how=inner")
df_all = pd.merge(df_DNI,df_1, how="inner")
print(df_all)