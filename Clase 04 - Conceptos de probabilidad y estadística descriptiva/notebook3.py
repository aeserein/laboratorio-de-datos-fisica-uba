import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import os
os.system("clear")

print("Algunos observables e histogramas de participantes de los experimentos coronadélicos y OCEAN")
print("Primero cargar ambos dataframes")
print("Para ocean, cargar solo las columnas que se van a usar\n")

df_coronadelicos = pd.read_csv("coronadelicos_safe.csv")
print(df_coronadelicos.head())
print("\n")

columnas_ocean = ['1_extraversion', '1_agreeableness', '1_conscientiousness', '1_neuroticism', '1_openness', '2_edad', '2_genero', 'hash']
df_ocean = pd.read_csv("ocean_safe.csv", usecols = columnas_ocean)
print(df_ocean.head())
print("\n")


print("Combinar")
df_combinado = pd.merge(df_coronadelicos, df_ocean, how='inner', on='hash')
print("\n")


print("Histograma de edades")

edades = df_combinado["2_edad"]
media = round(edades.mean(), 3)
mediana = round(edades.median(), 3)
moda = edades.mode().values[0]
varianza = edades.var()
desviacionEstandar = edades.std()
rango90Central = edades.quantile([0.05, 0.95])

print('Media: ', media)
print('Varianza: ', varianza)
print('Desviacion: ', desviacionEstandar)
print('90% central: {} - {}'.format(*rango90Central))
print('Mediana: ', mediana)
print('Moda: ', moda)
print("\n")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))
ax[0].hist(edades, bins = 20, rwidth=0.9, density=True)
ax[0].set_xlabel('Edad')
ax[0].set_ylabel('Frecuencia')

ax[1].axvspan(xmin=edades.quantile(0.05), xmax=edades.quantile(0.95), color="yellow", alpha=0.4, label="90% Central")
ax[1].hist(edades, bins=20, rwidth=0.9, density=True, color="lightcoral")
ax[1].set_xlabel('Edad')
ax[1].set_ylabel('Frecuencia')
ax[1].axvline(x = media, ls="--", color='darkorchid', linewidth=2, label="Media - " + str(media))
ax[1].axvline(x = moda, ls="--", color='crimson', linewidth=2, label="Moda - " + str(moda))
ax[1].axvline(x = mediana, ls="--", color='green', linewidth=2, label="Mediana - " + str(mediana))
ax[1].legend(loc = 'best')
plt.show()


print("Religiosidad\n")

religiosidad = df_combinado['0_religiosidad']
media = round(religiosidad.mean(), 3)
mediana = round(religiosidad.median(), 3)
moda = religiosidad.mode().values[0]
varianza = religiosidad.var()
desviacionEstandar = religiosidad.std()
rango90Central = religiosidad.quantile([0.05, 0.95])
print('Media: ', media)
print('Varianza: ', varianza)
print('Desviacion: ', desviacionEstandar)
print('90% central: {} - {}'.format(*rango90Central))
print('Mediana: ', mediana)
print('Moda: ', moda)
print("\n")

#ax = religiosidad.hist(bins = 20, grid = False, rwidth = 0.80)
ax = religiosidad.hist(bins = 100, grid = False, rwidth = 0.6, log = True)
ax.set_xlabel('Religiosidad')
ax.set_ylabel('Frecuencia')
plt.show()
print("\n")


print("Personalidad\n")

personalidades = ['1_extraversion', '1_agreeableness', '1_conscientiousness',
       '1_neuroticism', '1_openness']

fig, ax = plt.subplots(nrows = 1, ncols=5, figsize = (18, 3))
for i in range(len(personalidades)):
	ax[i].hist(df_combinado[personalidades[i]], bins = 20, rwidth = 0.80, density = True)
	ax[i].set_title(personalidades[i])
	ax[i].set_xlim([0, 50])

for p in personalidades:
	print(p)
	print('Media: {:3f}'.format(df_combinado[p].mean()))
	print('Desviacion: {:.3f}'.format(df_combinado[p].std()))
	print('90% central: {} - {}'.format(*df_combinado[p].quantile([0.05, 0.95])))
	print('Mediana: {}'.format(df_combinado[p].median()))
	print('Moda: {}'.format(df_combinado[p].mode().values))
	print('\n')

plt.show()



print("Correlaciones entre religiosidad y edades")

from scipy.stats import pearsonr, spearmanr 

# ¿Habrá alguna relación entre la religiosidad y edad de la persona?
print('Pearson {}'.format(pearsonr(religiosidad, edades)[0]))
print('Spearman {}'.format(spearmanr(religiosidad, edades)[0]))

fig, ax = plt.subplots(nrows=1, ncols = 2, figsize = (16, 6))
ax[0].scatter(edades, religiosidad)
ax[1].hist2d(edades, religiosidad, bins = 20)

ax[0].set_ylabel('Religiosidad')
ax[0].set_xlabel('Edades')
ax[1].set_xlabel('Edades')

plt.show()
print("\n")


print("Correlación entre edades y personalidades")
personalidades = ['1_extraversion', '1_agreeableness', '1_conscientiousness', '1_neuroticism', '1_openness']

for personalidad in personalidades:
	pear = pearsonr(df_combinado[personalidad], df_combinado['2_edad'])[0]
	spear = spearmanr(df_combinado[personalidad], df_combinado['2_edad'])[0]
	print(personalidad, "-------")
	print('Pearson {:.3f}'.format(pear))
	print('Spearman {:.3f}'.format(spear))
print("\n")


print("Correlación entre los 5 rasgos entre sí")
plt.matshow(df_combinado[personalidades].corr(method = 'spearman'))
plt.yticks(range(len(personalidades)), personalidades)
plt.xticks(range(len(personalidades)), personalidades, rotation = 90)
plt.colorbar()
plt.show()