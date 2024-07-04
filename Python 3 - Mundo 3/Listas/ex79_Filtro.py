valores = []
val_filtro = []


while True:
    #1
    valores.append(int(input(f"Informe um valor: ")))

    if valores[-1] in val_filtro:
        print(f"Valor duplicado! Não vou adicionar!")
    else:
        print("Valor adicionado com sucesso!")
        val_filtro.append(valores[-1])

    #2
    opcao = " "
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if opcao in "Nn":
        break

print(valores)
print(f"Você digitou os valores {val_filtro}")