from random import randint

#Rotinas
def sorteia():
    nums_sort = list()
    print("Sorteado 5 valores da lsita: ", end="")

    for c in range(0,5):
        num_sort = randint(1, 100)
        nums_sort.append(num_sort)
        print(num_sort, end=" ")
    print("PRONTO!")

    return nums_sort

def somaPar(resultado):
    #variável local
    soma = 0

    for val in resultado:
        if val % 2 == 0:
            soma += val
    print(f"Somando os valores pares de {resultado}, temos: {soma}")
    
#Variáveis Globais
resultado = sorteia()

#Programa Principal
somaPar(resultado)