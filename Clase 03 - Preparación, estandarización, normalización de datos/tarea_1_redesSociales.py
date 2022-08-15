import os
os.system("clear")

import pandas as pd
from ast import literal_eval

print("Normalizo los valores de los medios que consumen los de la tabla del notebook3")
print("------------------------------------------------------------------------------\n")

print("Leo archivo\n")

df = pd.read_csv("df_vacunados.csv",converters={"0_redesSociales": literal_eval})


#print(df['0_diarios'].value_counts())
#print(df['0_television'].value_counts())
#print(df['0_youtube'].value_counts())
def pasarAInt(x) :
    for v in x :
        if (v.isnumeric()) :
            v = int(v)
    return x


print("1 - Redes sociales")
print("\tHay 5 redes sociales identificadas con un número")
print("\t\t1\tFacebook")
print("\t\t2\tInstagram")
print("\t\t3\tTwitter")
print("\t\t4\tTikTok")
print("\t\t5\tLinkedIn")
print("\t\t6\tReddit")
print("\t\t7\tYouTube")
print("\t\t8\tTelegram")
print("\t\t9\tWhatsApp")
print("\t\t10\tTumblr")
print("\tPero también hay respuestas libres en letras")
print("\t\tAlgunas son las mismas 5 pero escritas en letras (\"twitter\")")
print("\t\tOtras son múltiples separadas por coma (\"2,3,facebook\")")
print("\t\tY otras son otras redes sociales a las que les tengo que poner yo un número")
print("\t-999 es no redes sociales\n")

length = len(list(df['0_redesSociales'].value_counts()))
print("Len", length, "\n")
print(df['0_redesSociales'].value_counts())
print("\n")

unicos = []
columnaRedesSociales = df["0_redesSociales"]

for i in columnaRedesSociales:
    for j in i :
        if j not in unicos :
            unicos.append(j)

#print(unicos)

dictRRSS = {
    1 : ["facebook"],
    2 : ["instagram"],
    3 : ["twitter", "love tw"],
#   4 : [],
    5 : ["linkedin"],
    6 : ["reddit", "reditt", "redit"],
    7 : ["youtube", "yt videos", "you tube"],
    8 : ["telegram"],
    9 : ["whatsapp"],
    10 : ["tumblr"]
}

def corregirRedesSociales(x) :

    # Si no usa ninguna red social, no puede decir -999 y el número de una red social
    # Así que le pongo -999
    if (-999 in x or "-999" in x) :
        return [-999]
    
    array = []
    #print(x, "\n")
    for a in x :
        #print(a, type(a), type(a)==int)
        if type(a)==int and a not in array:
            array.append(a)
        elif a != "" :
            for d in dictRRSS :
                for rsString in dictRRSS[d] :
                    if rsString in a and d not in array :
                        array.append(d)
        
    if len(array) == 0 :
        array = [-999]

    array.sort()
    return array

df["0_redesSociales"] = df["0_redesSociales"].apply(corregirRedesSociales)
length = len(list(df['0_redesSociales'].value_counts()))
print("\nLen", length, "\n")
print(df["0_redesSociales"].value_counts())

df.to_csv("tarea1.csv", index=False)