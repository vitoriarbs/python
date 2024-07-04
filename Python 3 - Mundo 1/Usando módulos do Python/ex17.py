'''
19 - Um professor quer sortear um ds seus quatro alunos para apagar o quadro. Faça um programa que ajude ele. lendo o nome deles e escrevendo o nome do escolhido 
'''
from random import choice
n1 = input('Primeiro aluuno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)