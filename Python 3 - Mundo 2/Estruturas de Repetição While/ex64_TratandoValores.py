num = 0
tot_num = -1
soma_num = 0

while num != 999:
    soma_num += num
    num = int(input("Digite um número [999 para parar]: "))
    tot_num += 1

print(f"Você digitou {tot_num} números e a soma entre ele foi {soma_num}")