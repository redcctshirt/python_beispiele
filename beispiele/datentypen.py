#!/usr/bin/env python

# Datentypen

# Ganze Zahl
a = 1
print(a)

# Gleitkommazahl
b = 2.3  
print(b)

# Zeichenkette
c = "Hallo Welt" 
d = 'Hi ' + 'Welt'
print(c)
print(d)

# Liste
e = [1,2,3,4]
f = ["Hi",5] + ["Welt",6]
print(e)
print(e[0])
print(f)
print(f[2])

# Dictionary
g = {"key1": "Hi", "key2": "Python"}
print(g["key1"], g["key2"])

# Boolean True, False
h = True
print(h)

# None
i = None
print(i)

# Typ ausgeben
type("Hallo Welt")
type(a)

# ID ausgeben
id(a)

del a # a löschen

# Konvertierung
int(23.4)
float(23)
bool(23)
complex(True)

print(1_0_0)  # Ausgabe 100
print(0o19)   # Oktal
print(0xFF)   # Hex
print(0b11)   # Binär
(23).bit_length()  # Anzahl der Bitstellen



