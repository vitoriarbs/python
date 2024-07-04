#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
tot = 0
num = int(input("Informe um número: "))

for c in range(1, num + 1):
    if (num % c == 0):
        tot += 1
        print(f"\33[33m {c}", end="") #pinta de amarelo os números divisiveis
    
    else:
        print(f"\33[31m {c}", end="") #pinta de vermelho os não divisiveis

if tot == 2:
    print(f"\n\33[mEste número é divisível por {tot} números, por isso É PRIMO")
else: 
    print(f"\n\33[mEste número é divisível por {tot} números, por isso NÃO é primo")