# 2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
# mostrar :
# a. A menor altura do grupo;
# b. A maior altura do grupo;

alturas = []

for alt in range(15):
  alt = float(input("Digite as alturas "))
  alturas.append(alt)

altX = max(alturas)
altN = min(alturas)

print(altX)
print(altN)