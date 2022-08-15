import os
os.system("clear")
import pandas as pd

print("Hay que estandarizar la columna 0_youtube")
print("El problema es que es muy homogenea, entonces hay que crear una forma de categorizar los canales que miran")
print("Y hay que codificarlo en números")
print("Lo voy a hacer con 2 categorizaciones en dos columnas separadas")
print("\t0_youtube_categoria\t\tCategoría de contenido")
print("\t\t1\tNoticias de política")
print("\t\t2\tNoticias generales")
print("\t\t3\tCiencia")
print("\t\t4\tReligión")
print("\t\t5\tEntretenimiento")
print("\t\t6\tEconomía y/o finanzas (no hay ninguno)")
print("\t\t-999\tNo dice o no mira nada")
print("\t0_youtube_orientacion_politica\tOrientación política del contenido, juzgado a ojo")
print("\t\t2\tDerecha explícita")
print("\t\t1\tDerecha soft")
print("\t\t0\tCentro o apolítico")
print("\t\t-1\tIzquierda soft")
print("\t\t-2\tIzquierda explícita")
print("\t\t-999\tNo dice o no mira nada")

print("Leo el archivo\n")

df = pd.read_csv("tarea1.csv")
columnaChutub = df["0_youtube"]
length = len(list(columnaChutub.value_counts()))
todosLosValores = columnaChutub.value_counts().index.tolist()

#print(todosLosValores, "\n")

print("Declaro arrays para matchear como substrings\n")
categorias = {
    1 : [	# Noticias de política
        "bolu", "pdb", "c5n", "les va", "bbc", "destape", "russian today", "rosada", "top de impacto", "rt ", "220 podcast", "marcelo peretta",
		"gzero", "peroncho delivery", "visual po", "visualpo", "diario k", "gobierno", "rt,", "presto", "milei"
	],
	2 : [	# Noticias generales
		"filo", "dw", "welle", "reunion secreta", "reunión secreta", "pero entonces", "vice", "diario uno", "cnn", "vox", "aljazeehra", "alta data"
		"nbc", "guardian", "rtve", "wsj", "economist", "de franco", "defranco", "telam", "altadata", "euronews", "chequeado", "asian", "radio con vos",
		"telemundo", "filó", "the times", "infonews", "telenoche", "infobae"
	],
	3 : [	# Ciencia
		"date un", "data un vlog", "dateun", "javier santaolalla", "platón", "platon", "scishow", "sci-show", "sci show", "robotitus", "kurzgesagt",
		"kurtzgesagt", "kurgenestsat", "kurzgesast", "kutzge" "glóbulo", "globulo", "veller", "doctor mike", "hiperactina", "dr mike", "doctormike",
		"damián kuc", "damian kuc", "world health", "salud", "gato y la caja", "quantum", "cientific", "científic", "science", "john campbell",
		"theskepticsguide", "seeker", "ciencia", "científicos", "tartaglione", "veritasium", "dr. stick", "dr stick", "doctor vic", "doc vic",
		"de un mir", "jamanetwork", "jama network", "healthcare triage", "neurocosas", "fernando polack", "kurgesaksjhsjdfhskd", "floreal ferrara",
		"medcram", "smartereveryday", "scenio", "cinthia", "mama dr jones", "dras en vivo", "medlife", "atienza", "nicosastre",
	],
	4 : [	# Religión
		"que no te la cuenten"
	],
	5 : [	# Entretenimiento
		"vorterix", "wisecrack", "usted está aquí", "usted esta aqui", "usted esta aquí", "usted está aqui", "ibai", "gata",
		"futurock", "vlogbrothers", "luisito", "jacobo wong", "frikidoctor", "delcarajo", "platzi", "javiertzo", "john oliver",
		"pedro ro", "insider", "futuröck"
	],
	-999 : [
		"no se", "no sé", "ninguno", "no tengo", "ballarini", "sputnik", "no recuerdo", "no me", "no reviso", "miniaturas en general en la parte",
		"muchos", "asd", "todos los canales que entrevistan", "nose", "varios", "aleatorios", "no sigo", "hhhh", "no identifico",
		"no soy", "no busco", "n/n", "no hay", "videos en general", "no recuerdo", "no podr", "...", "no te voy", "no puedo"
	]
}
orientaciones = {
	-2 : [	# Izquierda explícita
        "bolu", "pdb", "c5n", "les va", "destape", "pero entonces", "vice", "wisecrack", "cnn", "vox", "nbc", "russian today",
		"220 podcast", "altadata", "futurock", "dr. stick", "dr stick", "fernando polack", "peroncho delivery", "javiertzo", "diario k", "john oliver",
		"floreal ferrara", "alta data", "telemundo", "futuröck"
    ],
	-1 : [	# Izquierda soft
		"filo", "scishow", "sci-show", "sci show", "dw", "welle", "world health", "ministerio", "gato y la caja", "wsj", "asian", "rosada",
		"economist", "rt ", "telam", "vlogbrothers", "healthcare triage", "aljazeehra", "radio con vos", "gobierno", "filó",
		"mama dr jones", "pedro ro", "rt,", "infonews", "min de salud", "telenoche", "infobae"
    ],
	0 : [	# Centro o apolítico
		"date un", "data un vlog", "dateun", "javier santaolalla", "platón", "platon", "robotitus", "bbc", "kurzgesagt", "kurtzgesagt", "kurgenestsat", "kurzgesfast",
		"kutzge", "glóbulo", "globulo", "veller", "hiperactina", "dr mike", "damián kuc", "damian kuc", "vorterix",
		"quantum", "diario uno", "cientific", "científic", "asapscience", "asap science", "atraviesa lo desconocido", "guardian", "rtve",
		"doctor", "usted está aquí", "usted esta aqui", "usted esta aquí", "usted está aqui", "theskepticsguide", "seeker", "ciencia", "de franco", "defranco",
		"ibai", "científicos", "tartaglione", "gata", "veritasium", "saud en corto", "euronews", "luisito", "de un mir", "medcram"
		"jamanetwork", "jama network", "jacobo wong", "chequeado", "marcelo peretta", "neurocosas", "platzi", "kurgesaksjhsjdfhskd",
		"smartereveryday", "scenio", "cinthia", "dras en vivo", "medlife", "the times", "insider", "atienza", "nicosastre", "doc vic"
	],
	1 : [	# Derecha soft
		"reunion secreta", "reunión secreta", "john campbell", "top de impacto", "gzero", "delcarajo", "verdad oculta"
	],
	2 : [	# Derecha explícita
		"visual po", "visualpo", "que no te la cuenten", "presto", "milei"
	],
	-999 : [
		"no se", "no sé", "ninguno", "no tengo", "ballarini", "sputnik", "no recuerdo", "no me", "no reviso", "miniaturas en general en la parte",
		"muchos", "asd", "todos los canales que entrevistan", "nose", "varios", "aleatorios", "no sigo", "hhhh", "no identifico",
		"no soy", "no busco", "n/n", "no hay", "videos en general", "no recuerdo", "no podr", "...", "no te voy", "no puedo"
	]
}


print("Declaro arrays para matchear como iguales")
print("Para las opciones de las que no hay en estos arrays no hay porque no encontré cosas para matchear como strings exactos\n")
categorias_exacto = {
    1 : [	# Noticias de política
        "rt"
	],
	2 : [	# Noticias generales
		"noticias", "ted", "ip"
	],
	3 : [	# Ciencia
		"sadi", "who", "canales relacionados a vacunas", "rebecca watson"
	],
	-999 : [
		"-", "desconozco", "no conozco", "canales de televisión", "--", "na/nc", "múltiples canales", "cualquiera"
	]
}
orientaciones_exacto = {
	-2 : [	# Izquierda explícita
        "rebecca watson"
    ],
	-1 : [	# Izquierda soft
		"rt", "who", "ted"
    ],
	0 : [	# Centro o apolítico
		"sadi", "noticias", "ip"
	],
	-999 : [
		"-", "desconozco", "no conozco", "canales de televisión", "--", "canales relacionados a vacunas", "na/nc", "múltiples canales",
		"cualquiera"
	]
}


print("Creo dos columnas extras que voy a usar para crear los arrays\n")
index = df.columns.get_loc("0_youtube")
df.insert(index+1, "0_youtube_categoria", columnaChutub)
df.insert(index+2, "0_youtube_orientacion_politica", columnaChutub)


print("Aplico la función que crea las formatea las columnas de categoría y orientación política")

def formatearCategoria(x) :
	
	# Parte que devuelve si encuentra exacto
	for f in categorias_exacto :
		if (x in categorias_exacto[f]) :
			return [f]

	# Parte que busca por substring
	array = []
	for f in categorias :
		for canal in categorias[f] :
			if (canal in x) and (f not in array) :
				array.append(f)

	# Si no encontró nada devuelvo -999
	if (len(array) == 0) :
		return [-999]
	# Y si encontró -999, pero también encontró canales de verdad, saco -999 porque no es una respuesta vacía
	elif -999 in array and len(array) > 1 :
		array.remove(-999)

	array.sort()
	return array

df["0_youtube_categoria"] = df["0_youtube_categoria"].apply(formatearCategoria)
#print(df["0_youtube_categoria"].value_counts())

print("Formateo columna de orientación política por canal\n")

def formatearOrientacionPolitica(x) :
	
	# Parte que busca exacto
	for f in orientaciones_exacto :
		if (x in orientaciones_exacto[f]) :
			return f

	# Parte que busca por substring
	puntajes = []
	for f in orientaciones :
		for canal in orientaciones[f] :
			if (canal in x) :
				puntajes.append(f)

	puntajes = list(filter(lambda x: (x != -999), puntajes))
	
	# Si no queda nada es porque no encontró o solo había -999
	if (len(puntajes) == 0) :
		return -999

	total = sum(puntajes)
	resultado = total / len(puntajes)
	resultado = round(resultado, 2)
	return resultado

df["0_youtube_orientacion_politica"] = df["0_youtube_orientacion_politica"].apply(formatearOrientacionPolitica)
#print(df["0_youtube_orientacion_politica"].value_counts())


df.to_csv("tarea2.csv", index=False)