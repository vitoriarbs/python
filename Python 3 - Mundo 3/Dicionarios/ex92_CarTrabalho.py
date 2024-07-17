from datetime import date
ano = date.today().year
usuario = dict()

usuario['nome'] = str(input("Nome: ")).strip().title()
ano_nas = int(input("Ano de Nascimento: "))
usuario['idade'] =   ano - ano_nas
usuario['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))

if usuario["ctps"] != 0:
    usuario['contratação'] = int(input("Ano de Contratação: "))
    usuario['salário'] = float(input("Salário: R$"))
    #valor = com quantos anos o usuário poderá se aposentar, considerando que precisá de 35 anos de contribuição.
    usuario['aposentadoria'] = usuario['idade'] + (usuario['contratação'] + 35) - ano

print("-=" * 50)
for key, val in usuario.items():
    print(f"   - {key} tem o valor {val}")