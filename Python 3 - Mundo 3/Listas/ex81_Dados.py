valores = []

while True:
    #1
    valores.append(int(input(f"Informe um valor: ")))

    #2
    opcao = " "
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if opcao in "Nn":
        break

print("=" * 50)
print(f"Você digitou {len(valores)}")
print(f"Os valores digitados em ordem decrescente são {sorted(valores, reverse=True)}")
if 5 in valores:
    print("O valor 5 faz parte da lsita!")
else:
    print("O valor 5 não foi encontrado na lista!")