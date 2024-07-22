import moedas

#Rotina
def menu(num):
    print(f""" 
O que gostaria de fazer com seu valor de R${num}?
    [1] AUMENTAR
    [2] DIMINUIR
    [3] DOBRAR
    [4] METADE
""")
    opc = int(input(">>> "))
    return opc

#Programa Principal
def main():
    valor = float(input("Informe o valor: R$"))
    opc = menu(valor)

    if opc == 1:
        aumento = moedas.aumentar(valor)
        print(f"AUMENTO de 10%, temos {moedas.moeda_format(aumento, True)}")

    elif opc == 2:
        dimin = moedas.diminuir(valor)
        print(f"DIMINUINDO 13%, temos {moedas.moeda_format(dimin, True)}")

    elif opc == 3:
        dobro = moedas.dobrar(valor)
        print(f"O DOBRO de {moedas.moeda_format(valor)} é {moedas.moeda_format(dobro)}")

    elif opc == 4:
        metad = moedas.metade(valor)
        print(f"A METADE de {moedas.moeda_format(valor)} é {moedas.moeda_format(metad)}")

main()