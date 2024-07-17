dados = []
maior_peso = 0
menor_peso = 0
tot_usuarios = 0

while True:
    nome = str(input("Informe o nome: ")).strip().title()
    peso = float(input("Informe o peso: "))
    dados.append([nome, peso])

    #ou if len(dados) == 0:
    if tot_usuarios == 0:
        maior_peso = peso
        menor_peso = peso
    
    elif tot_usuarios > 0:
        if peso > maior_peso:
            maior_peso = peso
        elif menor_peso > peso:
            menor_peso = peso

    tot_usuarios += 1

    opcao = " "
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar? [S/N]? ")).strip().upper()[0]
    if opcao in "Nn":
        break


print("\n", "*" * 50)
print(f"Foram cadastradas {tot_usuarios} pessoas: {dados}")
print(f"O MAIOR peso foi de {maior_peso}Kg. Peso de:", end=" ")
for p in dados:
    #os pesos ficam no índice um dentro da lista [0.nome, 1.peso]
    if p[1] == maior_peso:
        print(p[0], end=" ")

print(f"\nO MENOR peso foi de {menor_peso}Kg. Peso de:", end=" ")
for nome, peso in dados:
    if peso == menor_peso:
        print(f"[{nome}]", end=' ')