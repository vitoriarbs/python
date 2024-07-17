usuario = dict()
usuarios = list()
mulheres = list()
tot_idade = 0


while True:
    usuario['nome'] = str(input("Nome: "))
        
    #validação
    while True:
        usuario['sexo'] = str(input("Sexo [M/F]: "))
        if usuario['sexo'] in "MmFf":
            break
        else:
            print("ERRO! Por favor, digite apenas M ou F.")

    if usuario["sexo"] in "Ff":
            mulheres.append(usuario['nome'])

    usuario['idade']  = int(input("Idade: "))
    tot_idade += usuario['idade']
    usuarios.append(usuario.copy())

    #validação
    opcao = " "
    while opcao not in "NnSs":
        opcao = str(input("Quer continuar [S/N]?" ))
        if opcao not in "SsNn":
             print('ERRO: Responda S ou N')
    if opcao in "Nn":
        print(usuarios)
        break

print("-=" * 40)
print(f"O grupo tem {len(usuarios)} pessoas")

media = tot_idade / len(usuarios)
print(f"A média de idade é de {media} anos")
print(f"As mulheres cadastradas foram: {mulheres}")
print("Lista das pessoas que estão acima da média:")

for u in usuarios:
    for key, val in u.items():
        if u['idade'] > media:
            print(f"{key} = {val};", end=" ")
    print()