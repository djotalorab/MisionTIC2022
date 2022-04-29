# Buclues:

from math import factorial


for i in [1, 2, 3, 4, 5, 6]:
    print("\nBuenas noches")
    print(i)

for i in [1, 5, 7, 9, 11, 3]:
    print("\nBuenas noches")
    print(i)

for i in "Buenas noches":
    print("\nBuenas noches")
    print(i)

for i in "Buenas noches":
    print(i, end=" ")
print("")

for i in "Buenas noches":
    if i in ("a", "e", "i", "o", "u"):
        print(i, end="")
print("")

for i in range (10):
    print(i, end=" ")
print(" ")

for i in range (100):
    print(i, end=" ")
print("")

for i in range (1, 5):
    print(i, end=" ")
print("")

contador = 0
for i in range (1, 10):
    contador += i
    print(i, end="")
print("\n",contador)

factor = 1
for i in range (1, 10):
    factor *= i
    print(i, end="")
print("\n", factor)