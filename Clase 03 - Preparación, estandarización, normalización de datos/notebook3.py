import os
os.system("clear")

import pandas as pd

print("A partir del dataframe de vacunas\n")
df = pd.read_csv("vacunas_safe.csv")
print(df)
print("\n")
columnas = list(df.columns[4:8]) + list(df.columns[19:34]) + ['hash']
df = df[columnas]
print(df)


print("\n-----------------------------------------------------------")
print("Hay que quedarse solo con los que no se vacunaron")
print('El campo es "0_vacunaAplicada" y el valor para los que no se la aplicaron es -999\n')

print(df['0_vacunaAplicada'].value_counts())
# -999: no fue vacunado
# los otros numeros indican vacunado con distintas vacunas

import numpy as np
indice_no_vacunado = np.logical_not(df['0_vacunaAplicada']==-999)
df_vacunados = df.drop(df[indice_no_vacunado].index)

print("\n")
print(df_vacunados['0_vacunaAplicada'].value_counts())


print("\n-----------------------------------------------------------")
print('La columna "0_preTeDarias" dice de 1 a 100 la voluntad de vacunarse')
print('La columna "0_preEfectiva" dice de 1 a 100 la creencia de si la vacuna va a parar al coronavirus')

print(df_vacunados['0_preTeDarias'].value_counts())
print(df_vacunados['0_preEfectiva'].value_counts())


print("\n-----------------------------------------------------------")
print("Dice que quiere sacar los que dan 100 en 0_preTeDarias porque son la gran mayoría,")
print("\tpor el ámbito del cual sacaron los datos\n")

from scipy.stats import zscore

indice_seguros = np.logical_and(df_vacunados['0_preTeDarias']==100, df_vacunados['0_preEfectiva']==100)
df_vacunados = df_vacunados.drop(df_vacunados[indice_seguros].index)

df_vacunados['0_preTeDarias (z)'] = zscore(df_vacunados['0_preTeDarias'])
df_vacunados['0_preEfectiva (z)'] = zscore(df_vacunados['0_preEfectiva'])

print(df_vacunados)


print("\n-----------------------------------------------------------")
print("Ver qué material consumen\n")
#descomentar la que querramos ver
pd.options.display.max_rows = 2000
#print(df_vacunados['0_diarios'].value_counts())
#print(df_vacunados['0_redesSociales'].value_counts())
#print(df_vacunados['0_television'].value_counts())
#print(df_vacunados['0_youtube'].value_counts())
