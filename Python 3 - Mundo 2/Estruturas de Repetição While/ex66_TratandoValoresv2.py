tot_num = 0
soma_num = 0

while True:
    num = int(input("Digite um número [999 para parar]: "))
    
    if num == 999:
        break
    else:
        tot_num += 1
        soma_num += num
    

print(f"Você digitou {tot_num} números e a soma entre ele foi {soma_num}")