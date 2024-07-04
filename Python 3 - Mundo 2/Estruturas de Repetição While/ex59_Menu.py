n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
opcao = 0

while opcao != 5:
    print("=-=" * 10)
    print('''[ 1 ]SOMAR
    [ 2 ]MULTIPLICAR
    [ 3 ]MAIOR
    [ 4 ]NOVOS NÚMEROS
    [ 5 ]SAIR''')
    opcao = int(input(">>>>> Qual sua opção? "))

    if opcao == 1:
        print(f"A SOMA entre {n1} + {n2}: {n1 + n2}")

    elif opcao == 2:
        print(f"O resultado de {n1} X {n2} é: {n1 * n2}")

    elif opcao == 3:
        print(f"Entre {n1} e {n2} o MAIOR valor é: {n1 if (n1 > n2) else n2}")

    elif opcao == 4:
        n1 = int(input("Informe novamente o primeiro valor: "))
        n2 = int(input("Informe novamente o segundo valor: "))
    
    elif opcao == 5:
        print("Finalizando...")

    elif opcao > 5:
        print("Opção inválida! Tente novamente!")