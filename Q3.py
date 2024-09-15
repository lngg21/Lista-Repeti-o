# 3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
# negativos e o percentual de valores negativos e positivos.

numeros = []

numNeg = []
numPos = []

while True:

  num = int(input("Digite os seus numeros: "))
  numeros.append(num)

  fim = input("Deseja continuar S/N: ")
  if fim.upper() != "S":
    break

soma = sum(numeros)
qtdGeral = len(numeros)

media = soma / qtdGeral


for n in numeros:
  if n < 0:
    numNeg.append(n)
  else:
    numPos.append(n)
##Quantidades de Positivos
  qtdPos = len(numPos)
##Quantidade de Negativos
  qtdNeg = len(numNeg)



percNeg = (qtdNeg / qtdGeral ) * 100 if qtdGeral > 0 else 0
percPos = (qtdPos / qtdGeral ) * 100 if qtdGeral > 0 else 0


print(f"\nMédia aritmética dos valores: {media:.2f}")
print(f"Quantidade de valores positivos: {qtdPos}")
print(f"Quantidade de valores negativos: {qtdNeg}")
print(f"Percentual de valores positivos: {percPos:.2f}%")
print(f"Percentual de valores negativos: {percNeg:.2f}%")