#!/usr/bin/env python3

# Dateien lesen und schreiben

f = open("datei.txt","r") # Datei zum lesen öffnen
for line in f:  # Zeilenweise ausgeben
    print(line)
f.close() # Datei schließen

f = open("datei.txt","w") # Datei zum schreiben öffnen
f.write("{} {}\n".format("Hallo", " Welt"))  # in die Datei schreiben
f.close() # Datei schließen

with open('datei.txt') as f:  # Datei zeilenweise ausgeben
     for line in f:
         print(line)
