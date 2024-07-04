#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

from random import randint
num_computador = randint(0,5)
#print(num_computador)
print("=" * 20 )
num_usuario = int(input("\n Entre 0 e 5, qual foi o número escolhido? "))
print("Parebéns! Você acertou o número escolhido!" if (num_usuario == num_computador) else "Você errou o número escolhido.\n")
print("=" * 20)
