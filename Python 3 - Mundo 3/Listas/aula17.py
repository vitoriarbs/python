print("criando e mostrando listas")
valores_desord =  [8, 2, 5, 4, 9, 3, 0]
valores = list(range(5, 11))
valores_par = list(range(0, 11, 2))

print(valores_desord)

for val in valores_par:
    print(f"{val}..", end=" ")
print("\n")

for pos, val in enumerate(valores):
    print(f"{pos} posição. {val}")



print("\nmudando valores da lista")
valores_desord[1] = 124
valores_desord.append(227) #adicionando o valor 227 no final da lista
valores_par.insert(1, 105)#adicionamos o valor 105 no índece 1 da lista valores_par
print(valores_par) 
print(valores_desord)
print(f"Essa lista possui {len(valores_desord)} elementos")

print("\nordenando valores")
print(sorted(valores_desord))
valores.sort(reverse=True)
print(valores)

print("\neliminando valores")
print("1.",valores_par)
valores_par.pop(1) #removemos o valor do índece 1
print("1.",valores_par)

print("2.", valores_desord)
if 124 in valores_desord:
    valores_desord.remove(124) #removemos o valor 124 de valores_desord
    print(valores_desord)
    print(f"Essa lista possui {len(valores_desord)} elementos")
else:
    print("não achei o valor 124")
