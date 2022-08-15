import os
os.system("clear")
import pandas as pd

print("Leer archivo\n")
df = pd.read_csv("dataframe_clase_3_corregido.csv")

print("Sacar los espacios de las columnas\n")
columns = list(df.columns)
for n, c in enumerate(df.columns):
    c = c.lstrip()              # lstrip remueve caracteres iniciales en blanco
    columns[n] = c.rstrip()     # rstrip hace lo mismo con los caracteres finales
df.columns = columns

print("Pasar todo a minúsculas y sacar los espacios\n")
def aMinusculasYSinEspacios(x) :
    if (type(x) == str) :
        return x.lower().lstrip().rstrip()
    else :
        return x
df = df.applymap(aMinusculasYSinEspacios)

print("Corregir la columna sexo\n")

# Sacando "Azul"
df = df[df["Sexo"]!="azul"]

# Pasar a minúsculas
def parsearSexo(x) :
    if ("h" in x) :
        return "h"
    elif ("m" in x) :
        return "m"
    else :
        return "o"
df["Sexo"] = df["Sexo"].apply(parsearSexo)

print("Arreglar columna LU (libreta universitaria)\n")
def arregla_LU(x) :
    lista = [" ", "-", "//", "\\", "."]
    for l in lista:
        x = x.replace(l, '/')
    return x
def sacarCeros(x) :
    xArray = x.split("/")
    return ("%i%s%i" % (int(xArray[0]), "/", int(xArray[1])))
df["LU"] = df["LU"].apply(arregla_LU)
df["LU"] = df["LU"].apply(sacarCeros)


print("Arreglar columna Observación\n")
def arreglarObservacion(x):
    if type(x) == str:
        if "hiper" in x:
            return "hipertension"
        elif "dolor" in x and "cabeza" in x:
            return "dolor de cabeza"
        else:
            return "ninguna"
    else:
        return x

df["Observación"] = df["Observación"].apply(arreglarObservacion)


print("Pasar strings \"nan\" a verdaderos NaN\n")
import numpy as numpy
def pasarNaN(x) :
    if (x == "nan") :
        return numpy.NaN
    else :
        return x
df = df.applymap(pasarNaN)

print("Sacar promedios NaN\n")
df.dropna(subset=["Promedio"], inplace=True)

print("Sacar chars de columnas peso y altura\n")
def sacarChars(x):
    if type(x)==str:
        return ''.join(c for c in x if c.isdigit() or c=='.') # list comprehension
    else:
        return x
df["Altura"] = df["Altura"].apply(sacarChars)
df["Peso"] = df["Peso"].apply(sacarChars)


print("Pasar a float los promedios, el peso y la altura, y pasar a int las edades\n")
df['Promedio'] = df['Promedio'].apply(float)
df['Peso'] = df['Peso'].apply(float)
df['Altura'] = df['Altura'].apply(float)
df['Edad'] = df['Edad'].apply(int)


print("Sacar outliers de peso\n")
df = df[numpy.logical_and(df["Peso"] >= 35, df["Peso"] <= 180)]


print("Calcular ratio de peso y altura por sexo para aproximar los que no tienen altura\n")
df["PesoAlturaRatio"] = df["Peso"] / df["Altura"]
df_h = df[df["Sexo"] == "h"]
df_m = df[df["Sexo"] == "m"]
meanH = df_h["PesoAlturaRatio"].mean()
meanM = df_m["PesoAlturaRatio"].mean()

print("Calcular aproximación de los que no tienen altura\n")
df_h_sinAltura = df[ numpy.logical_and(pd.isnull(df["Altura"]), df["Sexo"]=="h") ]
df_m_sinAltura = df[ numpy.logical_and(pd.isnull(df["Altura"]), df["Sexo"]=="m") ]

pd.options.mode.chained_assignment = None   # default='warn'
                                            # Pandas tiene una advertencia para asignaciones de este tipo porque son riesgosas
df_h_sinAltura["Altura"] = (df_h_sinAltura["Peso"] / meanH).round(2)
df_m_sinAltura["Altura"] = (df_m_sinAltura["Peso"] / meanM).round(2)

df.loc[df_h_sinAltura.index, :] = df_h_sinAltura[:]
df.loc[df_m_sinAltura.index, :] = df_m_sinAltura[:]


print("Dropear columna del ratio\n")
df.drop(columns=["PesoAlturaRatio"], inplace=True)


print("Calcular aproximación de los que no tienen altura\n")
df.to_csv("mi_correccion.csv", index=False)

print(df)