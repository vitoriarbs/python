ANO_ATUAL = 2024
sex = str(input("Informe seu gênero [M/F]: "))
nasc = int(input("Informe o ano de nascimento: "))
idade = ANO_ATUAL - nasc
print(f"Quem nasceu em {nasc} possui {idade} anos em {ANO_ATUAL}.")

if sex == "F":
    print("Não é necessário realizar alistamento!")

elif (idade == 18):
    print("Você deve se alistar IMEDIATAMENTE!")

elif (idade > 18):
    print(f"Você já deveria ter se alista há {(idade - 18)} anos!")

else:
    print(f"Ainda faltam {(18 - idade)} anos para o alistamento")
    print(f"Seu alistamento será em {(18 - idade) + ANO_ATUAL}")