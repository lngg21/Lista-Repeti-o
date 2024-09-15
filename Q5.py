# 5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
# números lidos. O número que encerrará a leitura será zero.
pares = []
impares = []
soma_total = 0
qtd_numeros = 0

while True:
    num = int(input("Digite um número positivo : "))

    if num == 0:
        break
    elif num < 0:
        print("Digite um número positivo.")
        continue

    qtd_numeros += 1
    soma_total += num

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Cálculo das médias
if len(pares) > 0:
    media_pares = sum(pares) / len(pares)
else:
    media_pares = 0
if qtd_numeros > 0:
    media_geral = soma_total / qtd_numeros
else:
    media_geral = 0

print(f"\nQuantidade de números pares: {len(pares)}")
print(f"Quantidade de números ímpares: {len(impares)}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números: {media_geral:.2f}")