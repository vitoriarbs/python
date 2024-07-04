valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salario do comprador"))
anos = int(input("Informe quantos em anos será pago: "))

parcela = valor_casa / (anos *  12)
minimo = salario * 30 / 100

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${parcela:.2f}")

#se a parcela for maior que 30% do salario do comprador
if parcela > (salario - ((salario * 30)/100)):
    print("Empréstimo NEGADO! Salário insuficiente para realizar esse financiamento!")

else:
    print("Parabéns! Financiamento foi realizado com sucesso!")