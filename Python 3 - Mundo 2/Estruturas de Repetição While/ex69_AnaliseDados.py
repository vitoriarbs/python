tot_maior18 = 0
tot_masc = 0
tot_fem20 = 0

print("=" * 40)
while True:
    print("CADASTRE UMA PESSOA")
    idade = int(input("Idade: "))
    if idade > 18:
        tot_maior18 += 1
    
    sexo = " "
    while sexo not in "MmFf":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    
    if sexo in "Mm":
        tot_masc += 1

    if sexo in "Ff":
        if idade < 20:
            tot_fem20 += 1  

    opcao = " "
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    
    if opcao in "Nn":
        break
print("=" * 40)
print("{:^40}".format("FIM DO PROGRAMA"))
print(f"O total de pessoas com mais de 18 anos: {tot_maior18}")    
print(f"Ao todo temos {tot_masc} homens cadastrados.")
print(f"Ao todo temos {tot_fem20} mulheres com menos de 20 anos.")