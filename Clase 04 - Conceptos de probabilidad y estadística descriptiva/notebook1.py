import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats
import os
import time
os.system("clear")

print("Numpy tiene un módulo random, se accede como np.random")
print("rand() devuelve un random entre 0 y 1 como cualquier otro lenguaje")
print("Sería un random sacado de una distribución uniforme\n")
print("random", np.random.random())
print("\n")


print("normal() genera un random a partir de una distribución normal")
print("A esta distribución se le asigna una media μ, y una desviación σ\n")
mu = 0.00
sigma = 1.00

for f in range(12) :
    randn = np.random.normal(loc = mu, scale = sigma)
    print(randn)
print("\n")


print("También se puede fijar el seed")
print("El seed afecta todas las funciones de números aleatórios\n")

print("Seed 123 ---------------------------")
np.random.seed(123)
print(np.random.random())
print(np.random.normal())
print("Seed 123 ---------------------------")
np.random.seed(123)
print(np.random.random())
print(np.random.normal())
print("Seed 123 ---------------------------")
np.random.seed(123)
print(np.random.random())
print(np.random.normal())
print("Mando un epoch como seed para que de acá en adelante me de valores diferentes")
np.random.seed(int(time.time()))
print("\n")


print("Módulo scipy.stats")
print("Se crea una distribución y se generan los valores")
print("Los parámetros de cada distribución se deben sacar de la documentación más la teoría matemática que necesite")
print("norm, expon, uniform son continuas\n")

distribucion = stats.norm(loc = 0.00, scale = 1.00) #  Distribución normal
#distribucion = stats.expon(scale = 2.00) #  Distribución exponencial
#distribucion = stats.uniform(loc=2, scale = 4.0) #  Distribución uniforme igual que random() pero poniéndole un rango

# Generar numeros aleatorios con la distribucion dada (.rvs random variates)
muestra = distribucion.rvs(size = 50)
print(muestra)
print("\n")


print("Se puede crear gráficos con matplotlib")
print("subplots devuelve dos valores")
print("fig ni idea por ahora")
print("ax es una lista a la que se le asignan distribuciones")
print("\tSe le puede asignar las etiquetas para los ejes y otras cosas indicadas en la documentación\n")
print("nrows y ncols indican cómo va a organizar los gráficos en la ventana")
print("\tEn este ejemplo sería un solo \"renglón\" de 2 \"columnas\" de gráficos")
print("figsize indica el tamaño de la ventana")
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (15,5))

# Rango de la variable aleatoria, tomamos un cuantil del 99% 
cuantil_99 = distribucion.interval(0.9999)
print("Cuantil 99%:", cuantil_99)

# Rango de la variable x 
x = np.linspace(cuantil_99[0], cuantil_99[1], 100)

# pdf = probability density function
densidad_proba = distribucion.pdf(x)
ax[0].plot(x, densidad_proba)
ax[0].set_xlabel('Eje x')
ax[0].set_ylabel('Densidad de probabilidad')

# cdf = cumulative density function
proba_acumulada = distribucion.cdf(x)
ax[1].plot(x, proba_acumulada)
ax[1].set_xlabel('x')
ax[1].set_ylabel('Probabilidad acumulada')
ax[1].set_ylim([0, 1.05])

plt.show()


print("También se pueden crear distribuciones discretas")

#distribucion = stats.binom(n = , p = 0.25) # Distribucion binomial
distribucion = stats.poisson(mu = 4.00) # Distribucion de Poisson

# Muestra de 20 numeros aleatorios (.rvs random variates)
muestra = distribucion.rvs(size = 20)
print("Muestra:", muestra)
plt.hist(muestra, bins=10, range=[0, 9], color="pink", rwidth=0.9, density=True)

fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (15,5))

# Rango de la variable x
cuantil_99 = distribucion.interval(0.99)
print("Cuantil 99%:", cuantil_99)
x = range(int(cuantil_99[0]), int(cuantil_99[1]))

# .pmf probability mass function
masa_proba = distribucion.pmf(x)
ax[0].plot(x, masa_proba, '.-', markersize = 20)
ax[0].set_xlabel('x')
ax[0].set_ylabel('Probabilidad')
ax[0].set_ylim(bottom = 0.00)

# .cdf cumulative density function
proba_acumulada = distribucion.cdf(x)
ax[1].plot(x, proba_acumulada, '.-', markersize = 20)
ax[1].set_xlabel('x')
ax[1].set_ylabel('Probabilidad acumulada')
ax[1].set_ylim([0, 1.05])

plt.show()


print("Se puede generar una distribución aleatoria de n veces")
print("En este caso una normal, que describe alturas de personas\n")

N = 1000
muestra = stats.norm.rvs(loc = 1.75, scale = 0.15, size = N)
#print(muestra, "\n")


print("Imprimir esta nueva distribución de alturas de personas")
print("Los parámetros que seteo en principio son:")
print("\tbins es la cantidad de rangos en x")
print("\tRango de los datos que voy a representar (sin especificar nada, toma el mínimo y el máximo)")
print("\trwidth es solo para visualizar, en vez de dibujar toda la barra, la angosta un poquito")
plt.hist(muestra, bins = 20, range = [1.00, 2.50], rwidth = 0.9)
plt.ylabel('Frecuencia')
plt.show()


print("Comparar el histograma con una distribución teórica")
# Density = True -> histograma normalizado
plt.hist(muestra, bins = 20, range = [1.00, 2.50], rwidth = 0.80, density = True)

# Lo comparamos con la distribución teórica (esto es trampa, es muy probable que nunca la sepamos)
x = np.arange(1.00, 2.50, 0.01)
plt.plot(x, stats.norm.pdf(x, loc = 1.75, scale = 0.15), label = 'Teórica')

plt.ylabel('Densidad de probabilidad')
plt.legend(loc = 'best')
plt.show()


print("cumulative = true, para hacer lo mismo pero con una distribución acumulada")
plt.hist(muestra, bins = 20, range = [1.00, 2.50], rwidth = 0.80, density = True, cumulative = True)

x = np.arange(1.00, 2.50, 0.01)
plt.plot(x, stats.norm.cdf(x, loc = 1.75, scale = 0.15), label = 'Teórica')

plt.ylabel('Probablidad acumulada')
plt.legend(loc = 'best')
plt.show()



print("Calcular observables")
media = np.mean(muestra)
mediana = np.median(muestra)
moda = stats.mode(muestra) # No tiene sentido calcular la moda porque "muestra" es una muestra

desviacion = np.std(muestra)
varianza = np.var(muestra)
rangoMax = np.max(muestra)
rangoMin = np.min(muestra)

cuartiles = np.quantile(muestra, [0.25, 0.50, 0.75])

print('Media = {:.3f}'.format(media))
print('Mediana = {:.3f}'.format(mediana))
print("Moda = ", moda)
print("numpy.mode devuelve un array. moda[0] son las modas, y moda[1] es el contador de estos campos")

print('Desviacion = {:.3f}'.format(desviacion))
print('Varianza = {:.3f}'.format(varianza))
print('Max = {:.3f}'.format(rangoMax))
print('Min = {:.3f}'.format(rangoMin))

print('Cuartiles 25%, 50%, 75% = {:.3f}, {:.3f}, {:.3f}'.format(*cuartiles))
print("\n")


print("Ver los cuartiles")
### Visualizacion de los cuantiles
plt.hist(muestra, bins = 50, range = [1.2, 2.4], density = True, cumulative = True, rwidth = 0.80)

# Cambiar aqui lo cuantiles que se quieran visualizar
for c in [0.20, 0.80]:
    plt.hlines(y = c, xmin = 1.2, xmax = np.quantile(muestra, c), linestyle = '--', color = 'r', alpha = 0.65, linewidth = 3)
    plt.vlines(x = np.quantile(muestra, c), ymin = 0.00, ymax = c, linestyles= '--', color = 'r', alpha = 0.65, linewidth = 3)

plt.ylabel('Probabilidad acumulada')
plt.ylim([0.00, 1.05])
plt.xlim([1.2, 2.4])
plt.show()



print("Otras distribuciones")
print("Uniforme y lineal")
# Distribucion uniforme entre 0 y 1
distribucion = stats.uniform()

# Muestra de numeros aleatorios
N = 1000
muestra = distribucion.rvs(size = N)

# Rango de la variable x 
x = np.arange(0.00, 1.01, 0.5) # No le encuentro ninguna diferencia al cambiar el step (tercer argumento)

fig, ax = plt.subplots(nrows=1, ncols = 2, figsize = (15, 5))

# Histograma de los datos  
ax[0].hist(muestra, bins = 20, range = [0, 1], rwidth = 0.8, density = True)

# Densidad de probabilidad teórica
ax[0].plot(x, distribucion.pdf(x))
ax[0].set_ylabel('Densidad de probabilidad')

# Histograma acumulado de los datos  
ax[1].hist(muestra, bins = 20, range = [0, 1], rwidth = 0.8, cumulative = True, density = True)

# Probabilidad acumulada teórica
ax[1].plot(x, distribucion.cdf(x))
ax[1].set_ylabel('Probabilidad acumulada')
  
print('Media = {:.3f}'.format(np.mean(muestra)))
print('Desviacion = {:.3f}'.format(np.std(muestra)))
print('Mediana = {:.3f}'.format(np.median(muestra)))
print('90% central = [{:.3f} - {:.3f}]'.format(*np.quantile(muestra, [0.05, 0.95])))
print("\n")
plt.show()



print("Lo mismo pero con una distribución exponencial, no acumulada y acumulada")
distribucion = stats.expon()

# Muestra de numeros aleatorios
N = 1000
muestra = distribucion.rvs(size = N)

# Rango de la variable x 
x = np.arange(0.00, 8.01, 0.01)

fig, ax = plt.subplots(nrows=1, ncols = 2, figsize = (15, 5))

# Histograma de los datos  
ax[0].hist(muestra, bins = 20, range = [0, 8], rwidth = 0.96, density = True, color="deeppink")

# Densidad de probabilidad teórica
ax[0].plot(x, distribucion.pdf(x))
ax[0].set_ylabel('Densidad de probabilidad')

# Histograma acumulado de los datos  
ax[1].hist(muestra, bins = 20, range = [0, 8], rwidth = 0.96, cumulative = True, density = True, color="purple")

# Probabilidad acumulada teórica
ax[1].plot(x, distribucion.cdf(x))
ax[1].set_ylabel('Probabilidad acumulada')
  

print('Media = {:.3f}'.format(np.mean(muestra)))
print('Desviacion = {:.3f}'.format(np.std(muestra)))
print('Mediana = {:.3f}'.format(np.median(muestra)))
print('90% central = [{:.3f} - {:.3f}]'.format(*np.quantile(muestra, [0.05, 0.95])))
print("\n")
plt.show()



print("Distribucion binomial, variables discretas")
distribucion = stats.binom(n = 10, p = 0.25)

# Muestra de numeros aleatorios
N = 1000
muestra = distribucion.rvs(size = N)

# Rango de la variable x 
x = range(0, 11)

fig, ax = plt.subplots(nrows=1, ncols = 2, figsize = (15, 3))

# Histograma de los datos  
ax[0].hist(muestra, bins = 11, range = [0, 11], rwidth = 0.5, density = True, align="left")

# Masa de probabilidad teórica (notar el cambio aquí respecto de las distribuciones continuas)
ax[0].plot(x, distribucion.pmf(x), '.-', markersize = 15)

# Histograma acumulado de los datos  
ax[1].hist(muestra, bins = 11, range = [0, 11], rwidth = 0.8, cumulative = True, density = True, align="left")

# Probabilidad acumulada teórica
ax[1].plot(x, distribucion.cdf(x), '.-', markersize = 15)
  

print('Media = {:.3f}'.format(np.mean(muestra)))
print('Mediana = {:.3f}'.format(np.median(muestra)))
moda = stats.mode(muestra)
print("Moda =", moda[0])
print('Desviacion = {:.3f}'.format(np.std(muestra)))
print('90% central = [{:.3f} - {:.3f}]'.format(*np.quantile(muestra, [0.05, 0.95])))
print("\n")
plt.show()



print("Si tengo un array de numpy o un dataframe de pandas, tengo métodos para calcular algunos observables")
A = np.array([[1, 2, 3, 3], [3, 1, 3, 9], [0, 0, 1, 2]])

# Observables por fila o columnas
print('Media: {}'.format(A.mean(axis = 0)))
print('Desviacion: {}'.format(A.std(axis = 0)))
print("\n")

print("También se puede calcular valores de los gráficos, pero sin graficarlos como matplotlib")
print("Puedo ver la frecuencia dentro de cada bin")
data = np.random.normal(loc = 0.00, scale = 1.00, size = 1000)
freq, bin_limits = np.histogram(data, bins = 10)

print('Frecuencia por bin: {}'.format(freq))
print('Límite de los bins: {}'.format(bin_limits))
print("\n")



print("Lo mismo pero en pandas")
import pandas as pd
dataframe = pd.DataFrame()
dataframe['x'] = np.random.normal(loc = 3.00, scale = 1.00, size = 100)
dataframe['y'] = np.random.exponential(scale = 2.00, size = 100)
dataframe['z'] = np.random.binomial(n = 10, p = 0.75, size = 100)

print('Media:')
print(dataframe.mean())

print('Desviacion:')
print(dataframe.std())

print('90% central:')
print(dataframe.quantile([0.5, 0.95]))

print('Mediana:')
print(dataframe.median())

print('Moda de la variable discreta: ')
print(dataframe['z'].mode())

# Histogramas 
fig, ax = plt.subplots(1, 3, figsize = (15, 3))
dataframe.hist(ax = ax, bins = 20, rwidth = 0.8, grid = False, cumulative = False, density = True)
plt.show()
print("\n")



print("Diferencia entre log normal y power-law")
print("El logaritmo es más exacto, mientras que la power-law tiene valores que no son insignificantes en rangos más extremos")
distribucion_lognormal = stats.lognorm(s = 2.00)
distribucion_powerlaw = stats.powerlaw(0.10, scale = 1000)

muestra_lognormal = distribucion_lognormal.rvs(size = 1000)
muestra_powerlaw = distribucion_powerlaw.rvs(size = 1000)

fig, ax = plt.subplots(1, 2, figsize = (15, 8))
ax[0].hist(muestra_lognormal, bins = 20, density = True, rwidth = 0.80)
ax[0].set_xlabel('x')
ax[0].set_title('Log-normal')
ax[1].hist(muestra_powerlaw, bins = 20, density = True, rwidth = 0.80)
ax[1].set_xlabel('x')
ax[1].set_title('Power-law')
plt.show()
print("\n")



print("El logaritmo normal se llama así porque si hacés el logaritmo de todas las variables dan una distribución normal")
print("Entonces si imprimís el gráfico en escala logarítmica da una campana gaussiana")
fig, ax = plt.subplots(1, 2, figsize = (15, 3))
ax[0].hist(np.log(muestra_lognormal), bins = 20, density = True, rwidth = 0.80, log=True)
ax[0].set_xlabel('log(x)')
ax[0].set_title('Log-normal')

ax[1].hist(np.log(muestra_powerlaw), bins = 20, density = True, rwidth = 0.80, log=True)
ax[1].set_xlabel('log(x)')
ax[1].set_title('Power-law')
plt.show()
print("\n")



print("Hay distribuciones de más de una variable")
print("En esta clase está a modo de demo, se explica en la siguiente")

# Coeficiente de correlacion
corr_x12 = 0.80

distribucion = stats.multivariate_normal(mean = [0.00, 0.00], cov = np.array(([1.00, corr_x12], [corr_x12, 1.00])))
muestra = distribucion.rvs(size = 1000) 

# Histograma 2D, notar que la muestra tiene dos columnas
plt.hist2d(muestra[:,0], muestra[:,1], bins = 20)

# Calculamos la correlacion de Pearson de los datos a modo de chequeo
plt.title('Pearson r = {:.3f}'.format(stats.pearsonr(muestra[:,0], muestra[:,1])[0]))

plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.colorbar(label = 'Frecuencia')
plt.show()