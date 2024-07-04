#from datetime import date
#ano_atual = date.today().year
ANO_ATUAL = 2024
nasc = int(input("Informe o ano de nascimento: "))
idade = ANO_ATUAL - nasc

print(f"O atleta tem {idade} anos")

if idade <= 9:
    print("Classificação: MIRIM")

elif idade <= 14:
    print("Classificação: INFANTIL")

elif idade <= 19:
     print("Classificação: JÚNIOR")

elif idade <= 25:
     print("Classificação SÊNIOR")

else:
     print("Classificação MASTER")