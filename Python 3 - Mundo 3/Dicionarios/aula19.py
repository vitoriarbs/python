locadora = {'titulo': 'Star Wars', 'ano': 1997, 'diretor': 'George Lucas'}
print(locadora)
print(locadora.items()) #irá mostar uma lista composta de três tuplas
print(locadora.keys())
print(locadora.values())
print(f"O filme {locadora["titulo"]} está disponivel") #utilizar aspas duplas para referenciar dicionários

for k, v in locadora.items():
    print(f"{k} = {v}")

locadora['genero'] = "Ficção" #adicionando um novo dicionário
for k in locadora.keys():
    print(k)

del locadora['ano'] #removendo um dicionário
for v in locadora.values():
    print(v)

