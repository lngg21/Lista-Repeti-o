# 4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
# estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
# terminar quando for lido um número negativo.


vCinco = []
cQuenta = []
cTenta = []
cem = []

while True:

  num = int(input("Digite os seus numeros: "))



  if num < 0:
    break

  if num >= 0 and num <= 25:
        vCinco.append(num)
  elif num >= 26 and num <= 50:
        cQuenta.append(num)
  elif num >= 51 and num <= 75:
        cTenta.append(num)
  elif num >= 76 and num <= 100:
        cem.append(num)


qtdUm = len(vCinco)
qtdDois= len(cQuenta)
qtdTres = len(cTenta)
qtdQuatro = len(cem)

print(f"Quantidade de valores entre o intervalo 0 - 25: {qtdUm}")
print(f"Quantidade de valores entre o intervalo 26 - 50: {qtdDois}")
print(f"Quantidade de valores entre o intervalo 51 - 75: {qtdTres}")
print(f"Quantidade de valores entre o intervalo 76 - 100: {qtdQuatro}")