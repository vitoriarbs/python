#{:^40} centraliza em 40 espaços
#{:=^40} centraliza em 40 espaços com '='
print("{:=^40}" .format(" LOJAS BERNAR "))
valor = float(input("Informe o preço da compra: R$"))

print("""
Informe a forma de pagamento
[1]DINHEIRO / PIX
[2]DÉBITO
[3]CRÉDIO
[4]CRÉDITO PARCELADO""")
menu = int(input("=>>"))

if menu == 1:
    #terá desconto de 10%
    valor_final = valor * (1 - (10 / 100))


elif menu == 2:
    #terá desconto de 5%
    valor_final = valor * (1 - (5 / 100))

elif menu == 3:
    valor_final = valor

elif menu == 4:
    qnt_parcelas = int(input("Informe a quantidade de parcelas: "))
    
    if qnt_parcelas < 3:
        valor_final = valor
        print(f"Sua compra será parcelada em {qnt_parcelas}x de R${(valor_final / qnt_parcelas):.2f} SEM JUROS")

    elif qnt_parcelas >= 3:
        valor_final = valor * (1 + (20 / 100))
        print(f"Sua compra será parcelada em {qnt_parcelas}x de R${(valor_final / qnt_parcelas):.2f} COM JUROS")

else:
    valor_final = 0
    print("ERRO: FORMA DE PAGAMENTO INVÁLIDA!")
print(f"Sua compra de R${valor:.2f} vai custar R${valor_final:.2f} no final.")