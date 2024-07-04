salario = float(input("\nInforme o salário do funcionário: "))

#salários maiores de R$1.250,00 recebem 10% de aumento
if salario > 1250.00:
    aumento = salario * (1 + 0.1)
    print(f"Parabéns! Você ganhou um aumento de 10% e seu salário atual será de R${aumento:.2}")

#salários menores de R$1.250,00 recebem 15% de aumento
else:
    aumento = salario + ((salario * 15)/100)
    print(f"Parabéns! Você ganhou um aumento de 15% e seu salário atual será de R${aumento:.2}")
