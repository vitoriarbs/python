#REVISAR
print("=" * 20, "\nBANCO CEV")
valor = int(input("Que valor você quer sacar? R$"))

totced_50 = 0
totced_20 = 0
totced_10 = 0
totced_1  = 0

while True:

    while valor >= 50:
        totced_50  += 1
        valor = valor - 50
        if valor < 50:
            break

    while 50 > valor >= 20:
        totced_20  += 1
        valor = valor - 20
        if valor < 20:
            break

    while 20 > valor >= 10:
        totced_10  += 1
        valor = valor - 10
        if valor < 10:
            break

    while 10 > valor >= 1:
        totced_1  += 1
        valor = valor - 1
        if valor < 0:
            break

    break

print("=" * 10)
if totced_50 > 0:
    print(f"Total de {totced_50} cédulas de R$50")

if totced_20 > 0:
    print(f"Total de {totced_20} cédulas de R$20")

if totced_10 > 0:
    print(f"Total de {totced_10} cédulas de R$20")
    
if totced_1 > 0:
    print(f"Total de {totced_1} cédulas de R$20")

print("=" * 10)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")