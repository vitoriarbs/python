from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0

for c in range(0, 7):
    nasc = int(input(f"{c}. Informe o ano de nascimento: "))
    idade = ano_atual - nasc

    if idade < 18:
        menores = menores + 1

    #para informar quantos são maiores de idade
    else:
        maiores = maiores + 1

print(f"{maiores} pessoas são maiores de idade.")
print(f"{menores} pessoas são menores de idade.")
        