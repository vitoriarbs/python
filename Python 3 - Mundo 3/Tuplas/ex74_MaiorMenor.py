from random import randint

numeros = (randint(1, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Os valors sorteados foram: ", end=" ")
for num in numeros:
    print(num, end=" ")
    
#descobrindo maior e menor números    
maior = 0
menor = 10
for cont in numeros:    
    if menor > cont:
        menor = cont

    if cont > maior:
        maior = cont

print(f"\nO maior valor sorteado foi: {maior}")  
print(f"O menor valor sorteado foi: {menor}")    