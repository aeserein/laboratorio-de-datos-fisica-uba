import pandas as pd
import os
os.system("clear")

print("Leer un dataframe de un csv")
print("read_csv tiene muchas opciones que voy a tener que sacar de la documentación")
print("Se agarra un dataframe de datos sobre la personalidad con el modelo de los 5 grandes\n")
filename = 'ocean_safe.csv' 
df = pd.read_csv(filename)
print(df)


print("\n-----------------------------------------------------------------")
print("Se agarran las columnas más importantes")
print("Las de los 5 rasgos de la personalidad, edad, género y hash\n")
columnas = list(df.columns[44:49]) + list(df.columns[54:56]) + ['hash']
df_ocean = df[columnas]
print(df_ocean)


print("\n-----------------------------------------------------------------")
print("Agarrar el dataframe de las preguntas sobre vacunas")
print("Se agarra un subgrupo de columnas relativas a la actitud previa y algunas variables generales que pueden ser útiles\n")
df = pd.read_csv("vacunas_safe.csv")
columnas = list(df.columns[4:8]) + list(df.columns[19:22]) + ['hash']
df_vacunas = df[columnas]
print(df_vacunas)
print(df_vacunas["0_vacunaAplicada"].value_counts())
print(df_vacunas["0_preEfectiva"].value_counts())


print("\n-----------------------------------------------------------------")
print("Combinar")
print("Entre estos 2 dataframes no hay hashes en común")
df_combinado = pd.merge(df_vacunas, df_ocean, how='inner', on='hash')
print(df_combinado)
print("\n")
print(set(df_ocean['hash']).intersection(df_vacunas['hash']))   # No imprime ningún hash en común
print(type(df_vacunas['hash'][0]))
print(type(df_ocean['hash'][0]))


print("\n-----------------------------------------------------------------")
print("En la clase no encuentran hashes en común entonces agarran otro archivo")
print("No entiendo por qué, después de haberse pasado 1 hora hablando sobre el modelo de 5 dimensiones")
print("Agarran entonces otro dataframe sobre falopa\n")
df_coronadelicos = pd.read_csv("coronadelicos_safe.csv")
#print(set(df_ocean['hash']).intersection(df_coronadelicos['hash']))    Aca se ven los hashes en común


print("\n-----------------------------------------------------------------")
print("Se combinan los 2 datasets")
df_combinado = pd.merge(df_ocean, df_coronadelicos, on="hash")
print(df_combinado)
print(df_combinado.columns)