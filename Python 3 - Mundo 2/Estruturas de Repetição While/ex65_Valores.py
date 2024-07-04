opcao = "s"
tot_num = 0
soma_num = 0

while opcao != "N" and opcao in "Ss":
    num = int(input("Digite um número: "))
    opcao = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]

    #calculando total de números digitados
    tot_num += 1

    #calculando a média
    soma_num += num
    media = soma_num / tot_num

    #recebendo maior e menor num
    if tot_num == 1:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        elif num < menor_num:
            menor_num = num 


print(f"Você digitou {tot_num} números e a média foi de {media:.2f}")
print(f"O MAIOR valor foi: {maior_num}")
print(f"O MENOR valor foi: {menor_num}")