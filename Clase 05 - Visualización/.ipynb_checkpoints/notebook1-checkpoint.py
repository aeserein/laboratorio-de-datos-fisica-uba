import os
os.system("clear")

import pandas as pd # La usamos para manejar la base de datos (y también graficar) https://pandas.pydata.org/docs/

import matplotlib.pylab as plt # Herramienta principal de visualización https://matplotlib.org/stable/contents.html
import matplotlib.dates as mdates # Dentro de matplotlib, tenemos una herramienta para manejo de fechas
import seaborn as sbn # Herramienta complementaria de visualización https://seaborn.pydata.org/


from ipywidgets import interact, interactive, fixed, interact_manual, interactive_output
import ipywidgets as widgets # Podemos ganar interactividad en la misma notebook https://ipywidgets.readthedocs.io/en/latest/

import plotly.express as px # Generamos un html dinámico, compartible, sin necesidad de correr procesos por detrás https://plotly.com/python/

import numpy as np # Siempre resulta que la usamos
from wordcloud import WordCloud # Lo usamos para las nubes de palabras

d_1 = pd.read_csv("vacunas_safe.csv")



print("Hay fechas que tienen formato yanki")
print("También hay fechas con comas como separadores")

def cambio_fecha(f):
  f = f.split('/')
  return '/'.join([f[1],f[0],f[2]])

d_1.loc[
    [3575, 4043, 2130, 1590, 1439, 1121, 1073, 1008,  929,  917,  753, 579,  500,  548,  400,  123],
    'timestamp'
] = d_1.loc[
    [3575, 4043, 2130, 1590, 1439, 1121, 1073, 1008,  929,  917,  753, 579,  500,  548,  400,  123],
    'timestamp'
].apply(cambio_fecha) # Aplico la función previamente creada para arreglar aquellas fechas mal formateadas

d_1['timestamp'] = d_1['timestamp'].apply(lambda x : pd.to_datetime(x.replace(',',''), format = '%d/%m/%Y %H:%M:%S')) # Llevo a datetime la columna de fechas ya arreglada
print("\n")



print("Esta forma de crear figuras es mejor en la práctica que solo llamar plt.plot")
#fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(16,7))
print("\n")



print("No sorpresivamente hay una columna género con 6 valores numéricos\n")

generos = d_1['0_genero'].value_counts()
print(generos, "\n")



print("Diccionario de qué significa cada número")
dic_generos = {
    1 : 'Mujer',
    2 : 'Varón',
    3 : 'No binario',
    4 : 'Género Fluido',
    5 : 'Ninguna de las opciones me identifica',
    6 : 'Prefiero no decirlo'
}
print(dic_generos, "\n")



print("Graficar")

fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (18, 6))
axs[0].grid('on', linestyle = 'dashed', alpha = 0.5)
axs[0].set_title('Género de lxs Participantes')
axs[0].set_ylabel('Fracción')
axs[0].bar(
	x = [i for i in range(len(generos))],				# Ubicación de las barras a lo largo del eje horizontal
	height = generos.values  / generos.values.sum(),	# Definimos la altura de las barras
	color = plt.get_cmap('Set2').colors
)
# xticks e yticks llevan los labels de cada barra
axs[0].set_xticks([i for i in range(len(generos))])
axs[0].set_xticklabels([dic_generos[g][:10] for g in generos.keys()], rotation=90)
axs[0].set_yscale('log')

axs[0].tick_params(axis='both', which='major', labelsize = 12)

axs[1].pie(generos.values / generos.values.sum(), colors = plt.get_cmap('Set2').colors)
axs[1].legend([dic_generos[g][:10] for g in generos.keys()], loc = (-0.12,-0.15))

fig.suptitle("Esto pone un subtítulo", fontsize="18")

plt.show()
print("\n")



print("Gráfico de radar - Preparar los datos\n")

nivel_educativo_segun_edad = d_1.groupby([pd.cut(d_1['0_edad'], 4), '0_nivelEducativo'])['hash'].count().unstack(1).drop([1,2], axis = 1).apply(lambda x : x / x.sum(), axis = 1)
print(nivel_educativo_segun_edad)
print("\n")



print("Matplotlib no tiene función de graficar radares, así que hay que hacerlo a mano")
print("Queda la función acá como referencia")

def radar_plot(df, title = '',):
    categories = df.columns
    N = len(categories)
    # Lo primero que hacemos es setear los ángulos a destacar en nuestro radar plot: uno para cada categoría que tengamos
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
     
    # Inicializamos una figura, teniendo en cuenta que debemos indicarle que vamos a trabajar en polares
    fig, ax = plt.subplots(figsize = (6,6), subplot_kw = {'projection': 'polar'})
     
    # Estas líneas ordenan las categorías de forma tal que la primera vaya arriba en el centro y el resto se distribuya en orden según las agujas del reloj
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
     
    # En cada uno de los ángulos, agregamos un tick con una etiqueta igual a la de la categoría en cuesitón
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories,
                       fontsize = 12)
     
    # Con estas líneas agregamos anillos que indiquen la distancia radial al centro del gráfico
    ax.set_rlabel_position(0)
    ax.set_yticks([0.1,0.2,0.3,0.4,0.5,])
    ax.set_yticklabels(["0.1","0.2","0.3","0.4","0.5",],
                       color = "darkgrey",
                       size = 10)
    ax.set_ylim(0,0.8)

    # ¿Y mis datos, dónde están mis datos?
    # Con esta iteración, recorremos las filas del data frame, agregando cada una a la figura
    for row in df.iloc:
            values = row.values.flatten().tolist()
            values += values[:1]
            ax.plot(angles, values, linewidth=1.5, linestyle = 'solid', label = 'Edad entre {} y {}'.format(int(row.name.left), int(row.name.right))) # Ploteamos la línea
            ax.fill(angles, values, 'b', alpha=0.1) # La rellenamos. Esto puede evitarse, o variar el alpha
    # Agregamos una legend que indique cuál es cada línea
    ax.legend(loc=(-0.2,-0.3),fontsize=12)
    # Seteamos el título
    ax.set_title(title, position=(.5, 1.2),fontsize=15)
    plt.show()

radar_plot(nivel_educativo_segun_edad, title = 'Nivel Educativo según Edad de lxs Participantes')
print("\n")



print("imshow para imprimir matrices")
print("Preparar los datos")
print("\"Taza\" de cambio indica cuánto cambió la opinión inicial de la vacuna luego de haber sido intervenido")

d_taza_de_cambio = d_1[(d_1['0_forkNarrativa'] != '-999') & (d_1['0_forkVacuna'] != '-999')& (d_1['0_preEfectosAdversos'] != 0)][['0_forkNarrativa', '0_forkVacuna','0_preEfectosAdversos', '0_postEfectosAdversos']].copy() # Seleccionamos columnas y nos quedamos con las filas que no tengan los -999
d_taza_de_cambio['taza de cambio'] = d_taza_de_cambio['0_postEfectosAdversos'] / d_taza_de_cambio['0_preEfectosAdversos']
d_taza_de_cambio = d_taza_de_cambio.groupby(['0_forkNarrativa', '0_forkVacuna'])['taza de cambio'].mean().unstack(1)
d_taza_de_cambio = d_taza_de_cambio.sort_values(by = d_taza_de_cambio.columns.to_list(), ascending = False) # Este ordenamiento hace que mínimamente la matriz vaya a quedar mejor ordenada para la visualización
print(d_taza_de_cambio, "\n")



print("Graficar")
fig, ax = plt.subplots(figsize = (8,8))

im = ax.imshow(d_taza_de_cambio.values, cmap = 'bwr', vmin = 0.95, vmax = 1.05)

ax.set_yticks(range(len(d_taza_de_cambio)))
ax.set_yticklabels(d_taza_de_cambio.index, fontsize = 12)

ax.set_xticks(range(len(d_taza_de_cambio.keys())))
ax.set_xticklabels(d_taza_de_cambio.columns, fontsize = 12, rotation = 90)

fig.suptitle('Taza de Cambio en Percepción de Efectos Adversos', fontsize = 15)

fig.colorbar(im, orientation = 'vertical')

plt.show()
print("\n")



print("Word cloud\n")
print("Improviso el diccionario de nombres porque es de un archivo que no esta en el Drive")

d_diarios_consumidos = d_1[(d_1['0_diarios'].str.contains('[^0-9]+') == False) & (d_1['0_diarios'] != '-999')][['0_diarios','hash']] # Nos quedamos con aquellas filas que contengan las opciones pre-establecidas (nos ahorramos el tema de texto libre)
d_diarios_consumidos['0_diarios'] = d_diarios_consumidos['0_diarios'].astype(int) # Lo llevamos a entero por una compatibilidad
print(d_diarios_consumidos["0_diarios"].value_counts())

"""
diarios_file = '/content/drive/My Drive/Clase 05_04_2022/Diccionario Vacunas - Diarios.csv'
d_diarios = pd.read_csv(diarios_file)
"""
array_ids = []
array_nombres = []
palabras = ["Noticias", "Diario", "Periódico", "News", "Noticiero", "Journal"]
import random
for f in range(0, 80) :
	array_ids.append(f)
	array_nombres.append(random.choice(palabras) + str(f))

nombresHC = {
    "ID" : array_ids,
	"Opción" : array_nombres
}
d_diarios = pd.DataFrame(nombresHC)

d = d_diarios_consumidos.merge(d_diarios, how = 'inner', right_on = 'ID', left_on = '0_diarios')['Opción']

wc = WordCloud(
	width = 1600, # Estos dos campos son importantes para definir la calidad de la imagen final
    height = 800,
    background_color = 'white', # El color de fondo que buscamos
    colormap = 'Reds' # La gama de colores para coloreal
).generate_from_frequencies(d.value_counts().to_dict())
fig, ax = plt.subplots(figsize = (10,6))
ax.imshow(wc, interpolation = 'bilinear')
ax.axis("off")
plt.show()
print("\n")



print("Pandas también tiene sus propias funciones de graficación")
print("pd.Series.plot()")
print("pd.DataFrame.plot()")
print("El problema de esto es que tiene muy pocas opciones")
print("En este gráfico no se puede manejar los labels entonces no se sabe qué está mostrando")

d_1.groupby(
    pd.Grouper(key = 'timestamp', freq = '2d') # 2d significa 2 días. Se le pueden poner varios intervalos
).hash.count().plot(
    kind = 'line', # por default
    #ax = algun eje,
    title = '¿Cómo respondieron temporalmente?',
    xlabel = 'Fechas',
)

plt.show()
print("\n")



print("Entonces se puede hacer lo mismo pero con matplotlib")
print("Se genera una figura y un axis, y se plotea con pandas")
print("\tpero se plotea sobre el axis de matplotlib, y ese axis te da los métodos de siempre de matplotlib")

actividad_temporal = d_1.groupby(
    pd.Grouper(key = 'timestamp', freq = '5h') # Guarden esta funcioncita porque es clave para agrupar fechas como se les plazca
).hash.count()

fig, ax = plt.subplots()
actividad_temporal.plot(
    kind = 'line', # por default
    #title = '¿Cómo respondieron temporalmente?',
    #xlabel = 'Fechas',
    ax = ax,
    x_compat = True # Esto parece importante, matplotlib trabaja distinto que pandas el tema de fechas y esto parece acomodar todo
)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d',)) #Como el formateador de php. b es el mes en palabras, d es el día, m es el mes en números
plt.gcf().autofmt_xdate()
ax.axvline(actividad_temporal.sort_values().keys()[-1],
           linestyle = 'dashed',
           color = 'red')
ax.text(
    x = actividad_temporal.sort_values().keys()[-1],
    y = 1000,
    s = 'Acá disparamos una campaña'
)
plt.show()
print("\n")



print("Seaborn es una librería que integra pandas y matplotlib")
print("La figura se crea con matplotlib igualmente")
print("Seaborn no requiere crear las distribuciones para ponerlas en un gráfico")
print("Los puntos en el boxplot son outliers")

sbn.set_context("paper", font_scale = 1.9) # Existen otros contextos, lo relevante es font_scale, que maneja valores dinámicos a diferencia de matplotlib
sbn.set_style("whitegrid",rc = {'grid.linestyle': '--'})

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize = (16,8)) # Medio que esta línea la vamos a necesitar casi siempre

sbn.violinplot(
    data = d_1,
    x = pd.cut(d_1['0_edad'], 4), # Pero lo jugoso está acá, en una línea, esto nos ahorró el laburo de agrupar y etc
    y = '0_posturaGobierno',
    ax = ax1
)
ax1.set_xlabel('Rango Etario')
ax1.set_ylabel('Postura frente al Gobierno')
ax1.set_xticklabels(['{}-{}'.format(int(i.left), int(i.right)) for i in sorted(pd.cut(d_1['0_edad'], 4).unique())])

sbn.boxplot(
    data = d_1,
    x = pd.cut(d_1['0_edad'], 4), # Pero lo jugoso está acá, en una línea, esto nos ahorró el laburo de agrupar y etc
    y = '0_posturaGobierno',
    ax = ax2
)
ax2.set_xlabel('Rango Etario')
ax2.set_ylabel('Postura frente al Gobierno')
ax2.set_xticklabels(['{}-{}'.format(int(i.left), int(i.right)) for i in sorted(pd.cut(d_1['0_edad'], 4).unique())])
plt.show()
print("\n")



print("Muy buena visualización con Seaborn que da scatter plots con distribuciones en los ejes")
print("\tcon colores según una tercera variable")
sbn.set_style("whitegrid",rc = {'grid.linestyle': '--'})

grid = sbn.JointGrid(data = d_1, height = 8)
ax = sbn.scatterplot(data = d_1[(d_1['0_preTeDarias'] != -999) & (d_1['0_postTeDarias'] != -999)], # Definimos la base de datos a trabajar
                x = '0_preTeDarias', # Definimos el campo a plotear en el eje x
                y = '0_postTeDarias',# Definimos el campo a plotear en el eje y
                ax = grid.ax_joint, # Definimos el eje al cual se le adjunta el gráfico
                hue = '0_posturaGobierno', # hue : es el campo que determina el color (puede ser númerico o categórico)
                alpha = 0.8 # La transparencia de los puntos
                )
sbn.kdeplot(d_1[(d_1['0_preTeDarias'] != -999) & (d_1['0_postTeDarias'] != -999)]['0_preTeDarias'], ax = grid.ax_marg_x)
sbn.kdeplot(y = d_1[(d_1['0_preTeDarias'] != -999) & (d_1['0_postTeDarias'] != -999)]['0_postTeDarias'], ax = grid.ax_marg_y)
ax.set_xlabel('¿Te la darías?')
ax.set_ylabel('Y ahora ¿te la darías?')
ax.legend(loc = (1.3,0), title = 'Postura frente al Gobierno')
ax.axis([-1,101, -1, 101])
plt.show()

sbn.reset_orig() # Usamos esta línea para resetear la configuración de ploteo. Permite que, en las siguientes celdas, creemos figuras con la configuración standar de matplotlib
print("\n")



print("Widgets interactivos en el notebook porque no andan ni en la consola de jupyter ni, obviamente, en bash")