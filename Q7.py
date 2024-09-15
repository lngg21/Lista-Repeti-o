# 7) Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de
# N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.
N = int(input("Digite um numero entre 1 e 10: "))
for i in range(11):
  if 1 <= N <= 10:
    resultado = N * i
  print(f"{N} x {i} = {resultado}")
else:
  print("Digite um numero entre um e 10")