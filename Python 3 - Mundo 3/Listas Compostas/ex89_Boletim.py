matriz = list()

while True:
    nome = str(input("Nome: "))
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2) / 2
    
    matriz.append([nome, [nota_1, nota_2], media])

    opcao = " "
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar [S/N]? "))
    if opcao in "Nn":
        break

print("*" * 50)
print(f"{"No.":<4} {"NOME":<10} {"MÉDIA":>9}")
print("-" * 50)

for p, v in enumerate(matriz):
    print(f"{p:<4} {v[0]:<10} {v[2]:>8}")
print('-'*30)

while True:
    opcao = int(input("Mostrar notas de qual aluno [999 para interromper]?"))
    if opcao == 999:
        break
    
    elif opcao > len(matriz):
        print("ERRO: Aluno não encontrado!")

    else:
        print(f"Notas de {matriz[opcao][0]} são: {matriz[opcao][1]}")

print("FINALIZADO!")