a= [12, 3, 4, 7]
b = a
print(f"1. Lista A: {a}")
print(f"1. Lista B: {b}")

#quando igualamos listas o python cria uma ligação entre elas 
b[2] = 1234
print(f"2. Lista A: {a}")
print(f"2. Lista B: {b}\n")

c =  [2, 6, 0, 13]
d = c[0:-1] #d recebe todos os valores de c[] e não criam ligação nenhuma
print(f"1. Lista C: {c}")
print(f"1. Lista D: {d}")

