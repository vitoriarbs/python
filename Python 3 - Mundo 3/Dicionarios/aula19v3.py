brasil = list()
estado = dict()


for c in range(0, 2):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())

print(estado)
print(brasil)

for estados in brasil:
    print(estados)

for estados in brasil: #passará pela lista interia
    for key, v in estados.items():
        print(f"O campo {key} tem valor: ", end="")
        print(v) #podemos utilizar somente values
    print()    