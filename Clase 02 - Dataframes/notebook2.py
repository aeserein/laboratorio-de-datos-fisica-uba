import os
os.system("clear")

print("Uno puede declarar una matriz como lo haría en cualquier lenguaje de programación\n")
a = [[2,5,1],[3,10,12],[2,0,0]]
print(a)
print(a[0][0])
print(a[1][2])


print("\n-----------------------------------------------------")
print("El problema es cuando se intenta operar matrices como se operarían normalmente en matemática")
print("\ten lugar de sumarlas, como son listas, Python solo las concatena\n")
a = [[2,5,1],[3,10,12],[2,0,0]]
b = [[2,5,1],[3,10,12],[2,0,0]]
print(a+b)


print("\n-----------------------------------------------------")
print("Para eso se usa la librería *nativa* de Python numpy\n")
import numpy as numpy
a = numpy.array([
    [2,5,1],
    [3,10,12],
    [2,0,0]
])
b = numpy.array([
    [2,5,1],
    [3,10,12],
    [2,0,0]
])
print(a+b)
print(type(a))


print("\n-----------------------------------------------------")
print("Numpy se crachea si le ponés chars")
"""
a = numpy.array(['hola', 'mundo'])
b = numpy.array(['como', 'va'])
print(a+b)
"""


print("\n-----------------------------------------------------")
print("Numpy multiplica una matriz por un escalar como se haría en matemática")
a = numpy.array([1,2,3])
print(a*3)


print("\n-----------------------------------------------------")
print("La multiplicación de matrices de numpy no es como la multiplicación real,")
print("sino elemento por elemento, 1 a 1 igual que la suma o resta")
print("Las 4 operaciones solo se pueden hacer entre matrices del mismo tamaño")

a = numpy.array([1,2,3])
b = numpy.array([2,4,10])
print(a, b)
print("\n")
print(a*b)
print("\n")

a = numpy.array([
    [2,3,4],
    [3,4,5],
    [4,5,6],
    [5,6,7]
])
b = numpy.array([
    [1,2,3],
    [2,3,4],
    [4,5,6]
])
print(a)
print(b)
print("\n")
# estas operaciones entre matrices son válidas
print(a+a)
print("\n")
print(a*a)
# estas operaciones son invalidas
"""
print(a+b)
print(a*b)
print(b*a)
"""

print("\n-----------------------------------------------------")
print("Para hacer multiplicación de verdad, función dot")
print("La cantidad de columnas de la primera tiene que ser igual a la cantidad de columnas de la segunda")

print(numpy.dot(a,b))
"""
fila por columna
4x3  *  3x3
  ^		^
^		  ^		<- resultado
resultado 4x3
"""

print("\n-----------------------------------------------------")
print("Numpy.dot también interpreta arrays unidimensionales según los requerimientos para hacer la multiplicación")
a = numpy.array([
	[2,5,1],
	[3,10,12],
	[2,0,0],
	[10,10,10]
])
b = numpy.array([1,2,3])
c = numpy.array([1,2,3,4])
print(numpy.dot(a,b))
print(numpy.dot(c,a))


print("\n-----------------------------------------------------")
print("Variable shape contiene el tamaño de una matriz")
print(a.shape)
print(b.shape)
print(c.shape)


print("\n-----------------------------------------------------")
print("Se puede transponer con la función transpose")
print(a)
print(numpy.transpose(a))


print("\n-----------------------------------------------------")
print("Concatenate concatena matrices")
print("Se puede concatenar vertical (axis 0) u horizontalmente (axis 1)")
print("Obviamente para concatenar verticalmente las columnas tienen que coincidir")
print("y para concatenar horizontalmente las filas tienen que coincidir")
a = numpy.array([
	[2,5,1],
	[3,10,12],
	[2,0,0],
	[10,10,10]
])
b = numpy.array([
	[2,5,1],
	[3,10,12],
	[2,0,0]
])
print(numpy.concatenate((a,b),axis=0))
print("\n")
print(numpy.concatenate((b,b),axis=1))


print("\n-----------------------------------------------------")
print("Se puede cortar una matriz")
print("Se puede seleccionar filas o columnas enteras con ':'")
print(a)
print("\n")
print(a[1:2])
print("\n")
print(a[1:3])
print("\n")
print(a[1:3,1:3])
print("\n")
print(a[:,1])
print("\n")
print(a[1,:])


print("\n-----------------------------------------------------")
print("Se pueden sacar los valores de una matriz que cumplen alguna condición")
print("Where devuelve una tupla de 2 arrays con los índices de los numeros que cumplen la condición")

a = numpy.array([
	[2,5,1],
	[3,10,12],
	[2,0,0],
	[10,10,10]
])
print(a)
print("\n")
print(numpy.where(a>1))

print("\n-----------------------------------------------------")
print("Se pueden pasar los números a un array indexando con la condición directamente en la matriz")

b = a[numpy.where(a>1)]
print(b)
c = a[a>1]
print(c)

print("\n-----------------------------------------------------")
print("Como 'a' no es un solo valor sino que es una matriz, no se puede indexar con operadores booleanos")
print("and y or solo funcionan con booleans de verdad")
"""
d = a[a>1 and a<9]
print(d)
"""

print("\n-----------------------------------------------------")
print("Numpy tiene funciones para usar condicionales con and y or")

print(a)
print("\n")
print(a>1)
print("\n")
print(a<9)
print("\n")
print(numpy.logical_and(a>1,a<9))
print("\n")
print(numpy.logical_or(a>1,a<9))
print("\n")
print(a[numpy.logical_and(a>1,a<9)])

print("\n-----------------------------------------------------")
print("Generar matrices regulares con 'zeros', 'ones' y 'eyes'")
print("Reciben una tupla, no los tamaños como argumentos separados")
print(numpy.zeros((2,5)))	# Matriz nula
print("\n")
print(numpy.ones((4,3)))	# Matriz de 1s que no me acuerdo como se llama
print("\n")
print(numpy.eye(5))			# Matriz identidad

print("\n-----------------------------------------------------")
print("Se puede importar un csv")
from numpy import genfromtxt
a = genfromtxt("./ejemplo-notebook2.csv", delimiter=',')

print(a)