valor_par = 0
num = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))

print(f"Você digitou os valore {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes.")

if 3 in num: 
    print(f"O valor 3 apareceu na {num.index(3) + 1} posição.")

else:
    print("O valor 3 não foi digitado em nenhuma posição")    

#print(f"O valor {num[0]} apareceu {num.count(num[0])} vezes.")
#print(f"O valor {num[1]} apareceu na {num.index(num[1]) + 1} posição.")

print(f"Os valores pares digitados foram: ")
#descobrindo números pares
for c in num:
    if c % 2 == 0:
        print(c, end=" ")
