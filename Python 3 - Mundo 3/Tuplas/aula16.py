#variável simples
lanche = "hamburguer"
lanche = "suco"
print(lanche)


#variável composta
#tuplas ficam dentro de ( parênteses )
lanche = ("hamburguer", "suco", "pizza", "pudim")

print(lanche)
print(lanche[2])

#fatiamentos / pedaços da tupla
#no fatiamento o último termo determinado é excluído
print(lanche[1:])
print(lanche[:2])
print(lanche[1:3])
print(lanche[-2:])

#len() pode informar a quantidade elementos dentro de uma variável composta
print(f"A variável LANCHE possui {len(lanche)} elementos")

#estruturas de repetição
for cont in range(0, len(lanche)):
    print(f"{cont}. Eu vou comer {lanche[cont]}")
print("Comi pra caramba!\n")

#para cada comida in lanche
for c in lanche:
    print(f"Eu vou comer {c}") #mostre comida
print("Comi pra caramba!\n")

#o enumerate nos da tanto o dado quanto a posição dele
for pos, comida in enumerate(lanche):
    print(f"{pos}. Eu vou comer {comida}")

#sorted transforma tuplas em listas para organizar = vira algo mutável
#em ordem alfabética
print(sorted(lanche))

#mas a tupla lanche continua com as mesmas posições
print(lanche)