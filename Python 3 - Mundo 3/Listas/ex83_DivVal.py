tot_list = []
pares = []
impares = []

while True:
    #1
    tot_list.append((int(input(f"Informe um valor: "))))

    #2
    opcao = " "
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if opcao in "Nn":
        break

print("=" * 20)
for pos, val in enumerate(tot_list):
    if val % 2 == 0:
        pares.append(tot_list)
    else:
        impares.append(tot_list)

print(f"A lista completa é {tot_list}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")