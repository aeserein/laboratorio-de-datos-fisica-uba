import numpy as np
import pandas as pd
import os
os.system("clear")

print("Importar el dataframe\n")
try:
    dt = pd.read_csv("dataframe_clase_3.csv")
    print(dt)
except Exception as e:
    print('No se pudo importar porque los campos están delimitados por ", " en lugar de ","')
    print(e)


print("\n----------------------------------------------------")
print("Parseo cambiando el delimitador\n")
df = pd.read_csv("dataframe_clase_3.csv", delimiter=", ")
print(df)


print("\n----------------------------------------------------")
print("El profesor no cambia el delimitador")
print("Hay una columna que en vez de ser 99/999 es 99,999, entonces eso también perjudicaría el parseo")
print("Dice que para casos así muchas veces es más fácil decirle al que hace el archivo que lo haga bien")
print("Pero es probable que eso no sea posible entonces hay que arreglársela")
print("En este caso le modifica esa mala coma a mano, pero por supuesto en archivos reales no es tan fácil\n")

df = pd.read_csv("dataframe_clase_3_corregido.csv")
print(df)


print("\n----------------------------------------------------")
print("Hay muchos problemas en todas las columnas y se pueden abordar de varias formas")
print("dropna")

print(df.dropna())

print("\n----------------------------------------------------")
print("Las columnas están mal por los espacios")
print(df.columns)
try:
    print(df["Promedio"][20])
except Exception as e:
    print('No se encuentra el key "Promedio"')
    print(e)

print("\n----------------------------------------------------")
print("Se sacan los espacios con lstrip (como trim)")
print("Obviamente hay otras formas de hacerlo seguramente")
print("\tpero acá lo hace creando un array, modificándolo, y reemplazando los índices")
print("\tEsto lo hace así porque los índices de pandas son inmutables\n")

columns = list(df.columns)
print(columns)
for n, c in enumerate(df.columns):
    c = c.lstrip()              # lstrip remueve caracteres iniciales en blanco
    columns[n] = c.rstrip()     # rstrip hace lo mismo con los caracteres finales
    print(columns[n])
df.columns = columns
print(df.columns)


print("\n----------------------------------------------------")
print("Ahora se puede ubicar un dato según los índices sin espacios")
print(df["Promedio"][20])


print("\n----------------------------------------------------")
print("Los campos, no solo estan mal sino que tienen todos un espacio al principio")
print("Para corregir esto se puede:")
print("\t1 - Remover los espacios en todo el dataframe")
print("\t2 - Leer el csv con la opcion skipinitialspace=True")
print("\t3 - Editar el archivo original")

print("\n----------------------------------------------------")
print("La mejor es la 2")
print("Aunque sigue quedando el espacio al final de la columna Observación")
print("\ty no hay opcion skipendingspace ni nada parecido")
df2 = pd.read_csv("dataframe_clase_3_corregido.csv", skipinitialspace=True)
print(df2)
print(df2["Altura"][15])


print("\n----------------------------------------------------")
print("Opción 1 de sacarlo uno por uno")
print("applymap recibe una función y la corre en todos los datos de una columna")
print("Es importante no usar un for si se puede para recorrer cosas así porque pandas ya tiene métodos optimizados")


def remueve_espacio(x):
    if type(x) == str:
        return x.lstrip().rstrip()
    else:
        return x

df = df.applymap(remueve_espacio)
print(df)
print("\n")
print(df["Promedio"][20])
print(list(df.loc[18]))


print("\n----------------------------------------------------")
print('Reemplazar los "nan" por NaNs de verdad de numpy\n')

def cambiarNan(x):
    if x == "nan":
        return np.nan
    else:
        return x

df = df.applymap(cambiarNan)
print(df)


print("\n----------------------------------------------------")
print('dropna para sacar los NaNs de verdad\n')
df.dropna(inplace=True)
print(df)


print("\n----------------------------------------------------")
print("Pasar todo a minúsculas para poder matchear strings")

def aMinusculas(x):
    if type(x) == str:
        return x.lower()
    else:
        return x

df = df.applymap(aMinusculas)
print(df)


print("\n----------------------------------------------------")
print("Columna Observación")
print('"apply" para aplicar una función a una columna en vez de a toda la tabla')
print("Se puede normalizar los strings o se puede pasar todo a códigos numéricos")
print("En el caso de una tabla legible para personas es mejor dejar el texto")
print("\tpero en una tabla que se prepara para machine learning es mejor usar números")
print("Es muy importante considerar soluciones que no solo sirvan para el dataset que uno tiene")
print("\tsino también en datos futuros que se puedan agregar a la tabla")
print("\tTambién si se está trabajando en desarrollo con datos falsos para después pasarlo a desarrollo con datos reales")
print('En este caso se unifican "hipertension" e "hiper tension", los campos para "ninguna" y "dolor de cabeza"\n')

print(df["Observación"].value_counts())
print("\n")

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
print(df)


print("\n----------------------------------------------------")
print("Sacar los chars de las columnas que son datos numéricos\n")

def remueve_caracteres(x):
    if type(x)==str:
        return ''.join(c for c in x if c.isdigit() or c=='.') # list comprehension
    else:
        return x

df['Altura'] = df['Altura'].apply(remueve_caracteres)
df['Peso'] = df['Peso'].apply(remueve_caracteres)
print(df)


print("\n----------------------------------------------------")
print("Corregir los divisores en la libreta columna universitaria\n")
def arregla_LU(x): # esta función reemplaza las posibilidades por siempre el mismo símbolo
    lista = ['\\\\','\\','-', ' ','//']
    if type(x)==str:
        for l in lista:
            x=x.replace(l,'/')
        return x
    else:
        return x

df['LU'] = df['LU'].apply(arregla_LU)
print(df)


print("\n----------------------------------------------------")
print("Corregir la línea 17 de libreta universitaria que dice 099\n")

def normalizarNumeros(x):
    partes = x.split("/")
    n1 = int(partes[0])
    n2 = int(partes[1])
    return ("%s/%s" % (n1,n2))          # Una de las formas de concatenar strings, me gusta porque se parece a c
df["LU"] = df["LU"].apply(normalizarNumeros)
print(df)

print("\n----------------------------------------------------")
print("Pasar a float los promedios\n")

df['Promedio'] = df['Promedio'].apply(float)
print(df)


print("\n----------------------------------------------------")
print('Sacar la línea 16 que dice sexo "azul"\n')
print('"drop" funciona para valores individuales o strings')
print("\t(indices puede ser uno o varios)")

print(df['Sexo'].value_counts())

indices = df[df['Sexo']=='azul'].index
df = df.drop(indices)
print(df)


print("\n----------------------------------------------------")
print('Corregir columna sexo\n')

def jijijiEstoyEscribiendoLaPalabraSexo(x): 
	if ('h' in x):
		return 'h'
	elif ('m' in x) :
		return 'm'
	else:
		return 'n'

df['Sexo'] = df['Sexo'].apply(jijijiEstoyEscribiendoLaPalabraSexo)
print(df)


print("\n----------------------------------------------------")
print('Escribir en un csv nuevo\n')

df.to_csv("dataframe_corregido.csv", index=False)
print("Escrito")