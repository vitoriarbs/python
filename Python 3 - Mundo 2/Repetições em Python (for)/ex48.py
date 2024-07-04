soma = 0
for c in range(0, 500):
    #números ímpares e múltiplos de 3
    if( c % 2 != 0) and (c % 3 == 0):
        soma += c
        print(c, end=", ")
print("Fim!!!")
print(f"A soma de todos os números ímpares que são múltiplos de três é igual a: {soma}")
