# Quinto Desafio - Faça um programa que leia um número inteiro e mostre na tela seu SUCESSOR e seu ANTECESSOR.
num = int(input('Digite um número: '))
print(f'O sucessor de {num} é {num + 1}. \nO antecessor de {num} é {num - 1}.')
print('-'*20,'\n')

# ------------------------------
# Sexto Desafio - Crie um algoritmo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada.
num = int(input('Digite um número: '))
print(f'O dobro de {num} é {num*2}\nO triplo de {num} é {num *3}\nA raiz quadrada de {num} é {num**(1/2):.2f}') #:.2f = duas casas decimais flutuantes
print('-'*20,'\n')

# ------------------------------
# Sétimo Desafio - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = int(input('Informe a nota do primeiro semestre: '))
n2 = int(input('Informe a nota do segundo semetre: '))
print(f'A média entre {n1} e {n2} é {(n1+n2)/2:.2f}')
print('-'*20,'\n')

# ------------------------------
# Oitavo Desafio - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
val = float(input('Informe a distância em metros'))
print(f'{val}m = {val*100:.0f}cm\n{val}m = {val*1000:.0f}mm')
print('-'*20,'\n')