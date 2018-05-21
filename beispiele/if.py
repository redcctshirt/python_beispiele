#!/usr/bin/env python3

# Kontrollstrukturen

x = 5

# Wenn ... dann

if x == 2 or x == 1:
   print("x = 2 oder 1")
elif x == 3:
   print("x = 3")
else:
   print("x = " + str(x))

y = "1" if x == 1 else "nicht 1"
print(y)

# while-Schleife

while x == 1:
   print("1")
   break # break - Abbruch, continue - Weiter

# for-Schleife

for i in [1,2,3,9]:  # break - Abbruch, continue - Weiter
    print(i)

for i in range(1, 20, 3): # range(start, stop, schritt) - Bereich
    print(i)
    pass # Pass-Anweisung macht nichts
