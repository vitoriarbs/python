alunos = dict()

alunos['Nome'] = str(input("Nome do Aluno: ")).strip().title()
alunos['Média'] =  float(input(f"Média de {alunos['Nome']}: "))

if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'

print("=-" * 30)
for keys, val in alunos.items():
    print(f"    - {keys} = {val}")