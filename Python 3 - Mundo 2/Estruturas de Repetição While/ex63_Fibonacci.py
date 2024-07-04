print("-" * 10)
print("Sequeência de Fibonacci")  
print("-" * 10)

qnt = int(input("Quantas termos você quer mostrar? "))
qnt -= 1
#cont = 1

#variáveis fibonacci
anterior_num = 0
sucessor_num = 1 

#while cont <= qnt
while qnt >= 0 :
    
    print(f"{anterior_num}", end=" > ")
    print(f"{sucessor_num}", end=" > ")

    anterior_num = sucessor_num + anterior_num
    sucessor_num = anterior_num + sucessor_num
    
    qnt -= 2
    #cont += 2

print("FIM")