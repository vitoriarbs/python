from random import randint
num_sorte = [ ]

print("=" * 40)
print("JOGO NA MEGA SENA")
print("=" * 40)

qnt_linhas = int(input("Quantos jogos você quer que eu sorteie? "))
print("-=" * 3, f" SORTEANDO {qnt_linhas} JOGOS! ", 3 * "=-")
for jogos in range(0, qnt_linhas):
    print(f"Jogo {jogos}:", end=" ")

    tot_num = 0
    while tot_num < 6:
        num = randint(1, 60)

        #a lista receberá o primeiro valor, caso não tenha nenhum
        if len(num_sorte) == 0:
            num_sorte.append(num)
            tot_num += 1

        else: 
            #filtrando para não repetir num
            if num not in num_sorte:
                if num > num_sorte[-1]:
                    num_sorte.append(num)
                    tot_num += 1
                else:
                    pos = 0
                    while len(num_sorte) > pos:
                        if num_sorte[pos] >= num:
                            num_sorte.insert(pos, num)
                            tot_num += 1
                            break
                        pos += 1
                
    print(f"{num_sorte}")
    num_sorte.clear()
    
print("-=" * 3, ' BOA SORTE ', 3 * "=-")