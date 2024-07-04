a = (2, 4, 6)
b = (9, 12, 15)
c = a + b
d = b + a
e = c + d
print(c)
print(d)
print(e)
print(f"O número 2 aparece {e.count(2)} vezes em {e}")

#mostra apenas a posição do primeiro 2 que aparecer
print(f"A posição do número 2 em {e} é: {e.index(2)}")
#procura o número 2 a partir da posição 2
print(f"A posição do número 2 em {e} é: {e.index(2, 2)}")

#TUPLAS aceitam dados de VÁRIOS tipos
pessoa = ("Gustavo", 39, "M", 99.8)
print(pessoa)

#deleta a variável inteira
del(pessoa)
#print(pessoa) - vai dar erro porq pessoa foi deletada