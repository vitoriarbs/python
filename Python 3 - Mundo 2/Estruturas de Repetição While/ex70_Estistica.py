print("=" * 40)
print("{:^40}".format("LOJA SUPER BERNAR"))
print("=" * 40)
valor = 0
tot = 1
tot_compra = 0
mais1000 = 0


while True:
    nome_produto = str(input("Nome do Produto: ")).strip().title()
    valor = float(input("Valor: R$"))
    tot_compra += valor
    
    #recebendo primeiro produto como mais barato
    if tot == 1:
        valor_barato = valor
        nome_barato = str(nome_produto)

    #recebendo produto mais barato que o primeiro
    elif tot > 1:
        if valor_barato > valor:
            valor_barato = valor
            nome_barato = str(nome_produto)

    #valores maior que R$1000.00
    if valor > 1000:
        mais1000 += 1

    opcao = " "
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if opcao in "Nn":
        break

    tot += 1

print("=" * 40)
print("FIM DO PROGRAMA")
print(f"O total da compra foi de R${tot_compra:.2f}")
print(f"Temos {mais1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_barato} que custa R${valor_barato:.2f}")