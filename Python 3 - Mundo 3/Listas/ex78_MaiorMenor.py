num = []

#adicionando valores em um lista
for pos in range(0,5):
    num.append(int(input(f"{pos}. Informe um valor: ")))

    #maior e menor irão receber o 0. valor
    if pos == 0:
        maior = num[pos]
        menor = num[pos]

    elif pos > 0:
        if num[pos] > maior:
            maior = num[pos]

        if menor > num[pos]:
            menor = num[pos]
print("=-" * 40)

#mostrando os resultados
print(f"Você digitou os valores: {num}")
print(f"O MAIOR valor digitado foi {maior} nas posições", end=" ")
for pos, val in enumerate(num):
    if val == maior:
        print(f"{pos}.. ", end="")

print(f"\nO MENOR valor digitado foi {menor} nas posições", end=" ")
for pos, val in enumerate(num):
    if val == menor:
        print(f"{pos}.. ", end="")
