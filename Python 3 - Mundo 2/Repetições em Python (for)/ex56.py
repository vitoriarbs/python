soma_idade = 0
homem_velho = 0
mulher_menor = 0

for c in range(1, 6):
    nome = str(input(f"{c}. Informe seu nome: ")).strip().title()
    sexo = str(input(f"{c}. Informe seu sexo [M/F]: ")).upper()
    idade = int(input(f"{c}. Informe sua idade: "))
    print("\n")

    #soma a idade de todos os participantes e dps divide pela qnt de participantes
    soma_idade += idade
    media_idade = soma_idade // c

    if sexo == "M" and idade > homem_velho:
        homem_velho = idade
        nome_velho = nome

    if sexo == "F" and idade < 20:
        mulher_menor += 1

print(f"A média de idade do grupo é de: {media_idade:.1f}")
print(f"O homem mais velho é tem {homem_velho} anos e se chama {nome_velho}")
print(f"Quantidade de mulheres que possuem menos de 20 anos: {mulher_menor}")