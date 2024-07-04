# Nono Desafio - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuala
num = int(input('Informe o número: '))
c = 0
print('-'*12)
while c <= 10:
    print(f'{num} x {c:2} = {num*c}')
    c += 1
print('-'*12, '\n')

# ------------------------------
# Décimo Desafio - Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos ólares ela pode comprar. Considere US$= 1.00 = R$3,27
val = float(input('Informe o valor em real: R$'))
print(f'Com R${val:.2f} você poderá comprar U${val/3.27:.2f}')
print('-'*20,'\n')

# ------------------------------
# Décimo Primeiro Desafio - Faça um Programa que leia  largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2metros-quadrados.
lar = float(input('Informe a largura da parede em metros: '))
h = float(input('Informe a altura da parede em metros: '))
print(f'Sua parede tem dimensão {lar}x{h} e sua área é de {lar*h:.2f}m')
print(f'Para pintar essa parede, você precisará de {(lar*h)/2:.2f}L de tinta.')
