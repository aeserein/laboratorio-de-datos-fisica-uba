import os
os.system("clear")

print("Outliers")
print("Arranco desde el dataframe corregido en notebook1")

import pandas as pd
df = pd.read_csv("dataframe_corregido.csv", )
print(df)


print("\n------------------------------------------------------")
print("La edad y la altura son distribuciones normales")
print("\tLa edad no parece tener ningún outlier")
print("\tEl peso parece tener dos, 432.0 y 8.0")
print("\t\t432 puede ser un peso extremo, pero no por eso se queda")
print("\t\tIncluso si lo es, no es representativo de una población general y me va a romper las mediciones")
print("Todo hay que verlo en contexto de:")
print("\tLo que uno sabe que está trabajando")
print("\tLos demás datos (que el peso, edad y altura coincidan\n")

import numpy as np
df = df[np.logical_and(df['Peso']<400, df['Peso']>10)]  # el indice donde esta la fila con un peso mayor a 400
print(df)


print("\n------------------------------------------------------")
print("Sacar z score de la edad\n")

from scipy.stats import zscore
df['Edad (z)'] = zscore(df['Edad'])
print(df)


print("\n------------------------------------------------------")
print("Sacar z score de la altura pero para hombres y mujeres")
print("Cosas así se pueden hacer en base al dataframe o a datos de la población total\n")

indice_h = df['Sexo']=='h'
indice_m = df['Sexo']=='m'

df['Altura (z)'] = np.zeros(len(df))  # ponemos 0 para despues poder modificarla
print(df)
print("\n")
df['Altura (z)'][indice_h] = zscore(df['Altura'][indice_h])
print(df)
print("\n")
df['Altura (z)'][indice_m] = zscore(df['Altura'][indice_m])
print("\n")
print(df)


print("\n------------------------------------------------------")
print("Normalizar los pesos")
print("Acá estandariza los pesos en lugar de sacar un z score para hacer el ejemplo")
print("\tpero para cosas así es mejor calcular un z score, y eso siempre es a mi criterio\n")

df['Peso (norm)'] = (df['Peso'] - df['Peso'].min())/(df['Peso'].max() - df['Peso'].min())
print(df)


print("\n------------------------------------------------------")
print("Poner una variable que se compara en términos nominales contra el promedio histórico")
print("En un caso así se necesitaría sacar el promedio de algún otro lado, no de la tabla\n")

historico=8.23      # Este promedio se tiene que sacar de la base de datos de todas las notas
df['Promedio (historico)'] = df['Promedio'] - historico
print(df)