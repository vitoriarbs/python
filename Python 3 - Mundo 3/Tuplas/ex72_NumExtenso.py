print("=" * 40)
num_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
               "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 20 >= num > -1:
        print(f"Você digitou o número {num_extenso[num]}")
        opcao = str(input("Deseja continuar [S/N]?")).strip().upper()[0]
        
        if opcao in "Nn":
            break

    else:
        print("ERRO: Número inválido! Tente novamente!")

print("=" * 40)
print("FIM DO PROGRAMA")