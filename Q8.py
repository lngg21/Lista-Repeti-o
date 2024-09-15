# 8) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
# P.A. contendo 10 valores.

a = int(input("Digite um valor inteiro inicial: "))
r = int(input("Digite um valor inteiro para a razão: "))



for n in range(10):
  pa = a + (n * r)
  print(pa)