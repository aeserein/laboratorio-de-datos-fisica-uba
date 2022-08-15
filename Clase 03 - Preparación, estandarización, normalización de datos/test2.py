import os
os.system("clear")

import pandas as pd
import json

print("Filtro la tabla de vacunas_safe.csv para limpiarle los datos en test3.py")
print("------------------------------------------------------------------------------\n")

print("Leo archivo\n")

df = pd.read_csv("vacunas_safe.csv")
columnas = list(df.columns[4:8]) + list(df.columns[19:34]) + ['hash']
df = df[columnas]

print("Agarro los que no se vacunaron")
print('El campo es "0_vacunaAplicada" y el valor para los que no se la aplicaron es -999\n')
df_vacunados = df[df["0_vacunaAplicada"] == -999]


print("Dropeo la columna 0_vacunaAplicada porque son todos -999\n")
df_vacunados = df_vacunados.drop(columns=["0_vacunaAplicada"])


print("Paso a minúsculas y saco espacios\n")
def minusculasYEspacios(x) :
    if (type(x)==str) :
        return x.lower().lstrip().rstrip()
    else :
        return x
df_vacunados = df_vacunados.applymap(minusculasYEspacios)


print("Jsonear todos los campos\n")
def jsonear(x) :
    array = x.split(",")
    array.sort()
    for i, a in enumerate(array) :
        array[i] = a.lstrip().rstrip()
        if (array[i].isnumeric()) :
            array[i] = int(a)
    return array

df_vacunados["0_redesSociales"] = df_vacunados["0_redesSociales"].apply(jsonear)
print(df_vacunados["0_redesSociales"].value_counts())


print("Guardo en un archivo aparte para simplificar\n")

print(df_vacunados["0_redesSociales"])
print("\n")

l1 = df_vacunados.loc[0]["0_redesSociales"]

df_vacunados.to_csv("df_vacunados.csv", index=False)