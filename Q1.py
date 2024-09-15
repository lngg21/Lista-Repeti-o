# 1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de
# três e que se encontram no conjunto dos números de 1 até 500

soma = 0

for n in range(1, 500):

  if n %2 !=0 and n%3 ==0:
    soma +=n

  print(soma)