from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import os
os.system("clear")


print("Se crea una distribución normal con media 0 y sigma 1 y se le agrega un número más")
print("Se puede ver que si se agrega un outlier muy grande la media se desvirtúa")
print("\tpero la mediana y los cuantiles se mantienen estables")
fig, ax = plt.subplots(1, 3, figsize=(18, 4))
fig_index = 0

for outlier in [0, 100, 1000]:

    # Creamos una muestra con una distribución normal y agregamos un outlier en algún lado.
    muestra = stats.norm.rvs(loc=0.00, scale=1.00, size=99)
    muestra = np.append(muestra, outlier)

    # Histograma
    ax[fig_index].hist(muestra, bins=np.arange(-4.25, 4.25,
                       0.50), rwidth=0.80, color='b', alpha=0.50)

    # Grafico de la media, mediana y cuantile
    ax[fig_index].vlines(x=np.mean(muestra), ymin=0, ymax=30, linewidth=3, linestyle='--', alpha=0.65, color='g', label='Media')
    ax[fig_index].vlines(x=np.median(muestra), ymin=0, ymax=30, linewidth=3, linestyle='--', alpha=0.65, color='k', label='Mediana')
    ax[fig_index].fill_between(x=np.quantile(muestra, [0.05, 0.95]), y1=30, color='r', alpha=0.15, label='90% central')
    ax[fig_index].set_ylim([0, 30])
    if fig_index == 2:
        ax[fig_index].legend(loc='best')
    ax[fig_index].set_title('Outlier en {}'.format(outlier))

    fig_index += 1

plt.show()
print("\n")


print("Correlaciones de Pearson y Spearman")

# Rango de x
x = np.arange(-2.00, 2.10, 0.10)
print(x, "\n")

# Relación de y con x: y ~ x^exponente
exponents = [0, 1, 7]

fig, ax = plt.subplots(1, 3, figsize=(16, 3))
for i in range(3):

    # Calculamos "y" agregandole un poco de ruido
    # (Esto es una lista por compresión, que permite crear listas rápidamente)
    y = [np.random.normal(loc=mu**exponents[i], scale=0.50) for mu in x]

    # Gráficos
    ax[i].scatter(x, y)
    ax[i].set_title('Pearson = {:.3f} - Spearman = {:.3f}'.format(pearsonr(x, y)[0], spearmanr(x, y)[0]))
    ax[i].set_xlabel('x', size=12)
    ax[i].set_ylabel('y', rotation=0, size=12)

plt.show()
print("\n")



print("Un valor bajo de correlación no significa que no haya relación entre las variables")
print("Acá pearson y spearman dan mal porque no se bancan una línea que no sea recta para pearson y de no decrecimiento con relación a x para spearman")
exponents = [2, 4]

fig, ax = plt.subplots(1, 2, figsize = (10,3))
for i in range(2):

  y = [np.random.normal(loc = mu**exponents[i], scale = 1.00) for mu in x]

  ax[i].scatter(x, y)
  ax[i].set_title('Pearson = {:.3f} - Spearman = {:.3f}'.format(pearsonr(x, y)[0], spearmanr(x, y)[0]))
  ax[i].set_xlabel('x', size = 12)
  ax[i].set_ylabel('y', rotation = 0, size = 12)

plt.show()
print("\n")



print("Teorema central del límite")
print("A números más grandes la distribución se achica")
print("si N tiende a infinito la media de una sola muestra es la media")
print("Cuanto más alto es N, más difícil es obtener una sumatoria de muestras que esté en valores extremos")
print("\tEjemplo: Obtener 2 (el mínimo posible) al tirar 2 dados es mucho más probable que obtener el mínimo posible de 10 dados")
fig, ax = plt.subplots(1, 3, figsize = (16, 7))
fig_index = 0

# Barremos en el tamaño de la muestra
for N in [10, 100, 1000]:

    sample_means = []

    # Simulamos 2500 veces en la que calculamos el promedio de n variables aleatorias
    for iteration in range(2500):

        sample = np.random.normal(loc = 0.00, scale = 1.00, size = N)
        sample_means.append(np.mean(sample))

    ax[fig_index].hist(sample_means, bins = 10, rwidth = 0.8, density = True, color = 'b', alpha = 0.50)

    x = np.arange(np.min(sample_means), np.max(sample_means), 0.001)
    
    # Distribución teórica según teorema central del límite
    ax[fig_index].plot(x, stats.norm.pdf(x, loc = np.mean(sample_means), scale = np.std(sample_means)), color = 'r', linewidth = 2, alpha = 0.65)
    
    ax[fig_index].set_xlim([-2, 2])
    ax[fig_index].set_title('N = {}'.format(N))
    ax[fig_index].legend(['Teórica', 'Simulación',])

    fig_index += 1

plt.show()
print("\n")



print("Teorema central del límite demosrtado con una distribución que no es normal y llega a una normal igualmente")
# Ejemplo, distribucion exponencial
distribution = stats.expon()

fig, ax = plt.subplots(1, 3, figsize = (16, 3))
fig_index = 0

# Barremos en el tamaño de la muestra
for N in [10, 100, 1000]:

    sample_means = []

    # Simulamos 2500 veces en la que calculamos el promedio de n variables aleatorias
    for iteration in range(2500):

        sample = distribution.rvs(size = N)
        sample_means.append(np.mean(sample))

    ax[fig_index].hist(sample_means, bins = 10, rwidth = 0.8, density = True, color = 'b', alpha = 0.50)

    x = np.arange(np.min(sample_means), np.max(sample_means), 0.001)

    # Distribución teórica según teorema central del límite
    ax[fig_index].plot(x, stats.norm.pdf(x, loc = np.mean(sample_means), scale = np.std(sample_means)), color = 'r', linewidth = 2, alpha = 0.65)
    
    ax[fig_index].set_xlim([0.0, 2.00])
    ax[fig_index].set_title('N = {}'.format(N))
    ax[fig_index].legend(['Teórica', 'Simulación',])

    fig_index += 1

plt.show()
print("\n")



print("Ley de grandes números")
print("Dice que para valores de N que tienden a infinito, la x bar tiende a la media")
print("Pero como obviamente uno no cuenta con infinitas muestras, se puede calcular un error, que va a ser menor a medida que N crezca")
print("             ______")
print("            /  S²")
print("Error = \  /  ———\tDonde S es la sumatoria de las N muestras")
print("         \/    N")
print("Esto solo aplica en distribuciones que tienen una media y desviación estándar bien definida")
sample_means = []
sample_errors = []

# Barremos en distintos valores de N 
N_range = [int(n) for n in np.logspace(0, 5, 21)]
for N in N_range:

  # Tomamos numeros aleatorios normalmente distribuidos y calculamos el promedio y el error
  sample = np.random.normal(loc = 0.00, scale = 1.00, size = N)
  sample_means.append(np.mean(sample))

  error = np.std(sample)/np.sqrt(N)
  sample_errors.append(error)

# Grafico con barras de error
plt.errorbar(x = N_range, y = sample_means, yerr = sample_errors, fmt ='b.-', linewidth = 2, markersize = 10, alpha = 0.65, label = 'Media de la muestra')
plt.hlines(y = 0.00, xmin = 0, xmax = np.max(N_range), linestyles='--', label = 'Valor medio de la población')
plt.xscale('log')
plt.xlabel('Tamaño de la muestra')
plt.legend(loc = 'best')
plt.show()