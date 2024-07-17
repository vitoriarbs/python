matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma_col3 = 0

#matriz possui 3 linhas
for l in range(0, 3):
    #cada linha possui 3 colunas
    for c in range(0, 3):
        num = int(input(f"Digite um valor para [{l},{c}]: "))
        matriz[l][c] = num
        
        if num % 2 == 0:
            pares += num

        #se c estiver na terceira coluna
        if c == 2:
            soma_col3 += num 

        #se l estiver na segunda linha
        if l == 1:
            if c == 0:
                maior_lin2 = num
            else:
                if num > maior_lin2:
                    maior_lin2 = num 

print("*" * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print() 

print('*' * 40)
print(f"A soma dos valores pares é: {pares}")
print(f"A soma dos valores da terceira coluna é: {soma_col3}")
print(f"O maior valor da segunda linha é: {maior_lin2}")