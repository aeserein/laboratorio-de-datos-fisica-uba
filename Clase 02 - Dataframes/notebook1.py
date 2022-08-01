import os
os.system("clear")

a = 8
b = 8.0     
c = 1.4e80 
d = 0b100   
e = 43.2 + 3j

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e, "(La j es número imaginario)")

print("--------------------------")

print(1.8e308*10)
print(5e-324/10)

print("--------------------------")

a = "hola mundo"
b = 'mucho gusto'
print(type(a))
print(type(b))
print(a)
print(b)

print("--------------------------")

a = "Una comilla simple ' en mi string"
b = 'Una comilla doble " en mi string'
print(a)
print(b)

print("--------------------------")

print("hola\nmundo")
print("hola\tmundo")
print("hola\\mundo")

print("--------------------------")

print(r'hola\nmundo', "(la r significa 'raw')")

print("--------------------------")

frase = """hola
mundo
\que tal?"""
print(frase)

print("--------------------------")

print("True or False\t->\t", True or False)
print("True and False\t->\t", True and False)
print("3==3\t\t->\t", 3==3)
print("3>2 or 2>3\t->\t", 3>2 or 2>3)
print("2!=0 and 5<0\t->\t", 2!=0 and 5<0)

print("--------------------------")

a = [1, 1.2, [3], True, 'hola', 3+3j]
print(a)
print(len(a))
print(a[0])
print(a[len(a)-1])
print(a[2:5])

print("--------------------------")

for item in a:
    print(item)

print("--------------------------")

for n in range(4,10):
    print(n)

print("--------------------------")

a = [1,2,3]
b = ['a', 'b', 'c']
print(a+b)
a = 'supercalifragilistico'
print(a[4:10])
print(a+ ' abracadabra')

print("--------------------------")

a = [1, 1.2, [3], True, 'hola', 3+3j]
a.reverse()
print(a)

print("--------------------------")

a = {
    'llave1':'hola',
    'llave2':[True,False,3.5],
    39:'hola mundo',
    49.324:12
}
print(a['llave1'])
print(a['llave2'])
print(a[39])
print(a[49.324])

print("--------------------------")

a = {
    'llave1':'hola',
    'llave1':[True,False,3.5],
    39:'hola mundo',
    49.324:12
}
print(a['llave1'])

print("--------------------------")

llaves = a.keys()
print(llaves)
print(list(llaves))
