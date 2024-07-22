# Rotinas
def maior(num):
    #variável local
    maior = list()

    for ind, val in enumerate(num):
        print(f"{val}", end=" ")

    print(f"Foram informados {len(num)} ao todo. O maior valor informado foi")

#Variáveis globais
nums = list()

#Programa Principal
while True:
    num = int(input("Informe um valor: "))
    nums.append(num)
    while True:
        opc = str(input("Deseja continuar [S/N]? "))
        if opc not in "NnSs":
            print("ERRO: Valor informado inválido. Tente novamente.")
        else:
            break
    if opc in "Nn":
        break

maior(nums)