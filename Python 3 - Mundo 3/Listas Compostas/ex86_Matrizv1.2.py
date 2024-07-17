matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#matriz possui 3 linhas
for l in range(0, 3):
    #cada linha possui 3 colunas
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))

print("*" * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print() 