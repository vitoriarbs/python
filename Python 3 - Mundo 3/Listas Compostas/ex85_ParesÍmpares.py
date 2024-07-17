valor = [[], [], []]
#par = []
#impar = []

for c in range(1, 8):
    num =  int(input(f"Digite o {c}o. valores: "))

    #se não tivermos nenhum valor, será adicionado o primeiro valor à lista
    if len(valor[0]) == 0:
        valor[0].append(num)

    #se já tivermos algum valor na lista    
    elif len(valor[0]) != 0:
        #vamos verificar se o numero é maior que o último valor da lista
        if num > valor[0][-1]:
            #se for, o número será adicionado no final da lista
            valor[0].append(num)
        
        #se o número for menor que o último valor da lista
        else:
            pos = 0
            #pos irá percorrer todas as posições em lista
            while pos < len(valor[0]):
                #até encontrar uma posição onde o valor seja maior ou igual a num
                if valor[0][pos] >= num:
                    #e então irá adicionar núm nessa posição e o valor maior irá pra trás de num
                    valor[0].insert(pos, num)
                    break
                pos += 1

for v in valor[0]:
    if v % 2 == 0:
        valor[2].append(v)
    else:
        valor[1].append(v)

print("\n","*" * 50)
print(f"Os valorer digitados foram: {valor[0]}")
print(f"Os valores ÍMPARES digitados foram: {valor[1]}")
print(f"Os valores PARES digitados foram: {valor[2]}")