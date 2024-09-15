# 9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
# P.G. contendo 10 valores.


a = int(input("Digite um valor inteiro inicial: "))
r = int(input("Digite um valor inteiro para a razão: "))


for n in range(10):
  pg = a * r**n
  print(pg)