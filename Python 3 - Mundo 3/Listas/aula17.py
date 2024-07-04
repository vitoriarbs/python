valores_desord =  [8, 2, 5, 4, 9, 3, 0]
valores = list(range(4, 15))
valores_par = list(range(0, 10, 2))
print(valores)
print(valores_par)

print("mudando valores da lista")
valores_desord[1] = 0
valores_desord.append(7) #adicionando o valor 7 no final da lista
valores_par.insert(5, 2), print(valores_par) #adicionamos o 5 no índece 2 da lista valores_par
print(valores_desord)
print(f"Essa lista possui {len(valores_desord)} elementos")

print("ordenando valores")
print(sorted(valores_desord))
valores_par.sort(reverse=True)
print(valores_par)

#eliminando valores
valores_par.pop(5)
print(valores_par)