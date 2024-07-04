'''18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''
#ou from math import radians, sin, cos, tan
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))#passa ângulo para radiano
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {ângulo} tem o TANGENTE de {tangente:.2f}')