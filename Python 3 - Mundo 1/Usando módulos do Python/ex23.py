numero = float(input("Informe um numero: "))

print(f"Analisando o número {len(numero)}")

print(f"Unidade: {numero   // 1 }")
print(f"Dezena: {numero   // 10 % 10}")
print(f"Centena: {numero // 100 % 10}")
print(f"Milhar: {numero // 1000 % 10}")