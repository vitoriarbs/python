# 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('cumprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {hi}')'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacentes: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')