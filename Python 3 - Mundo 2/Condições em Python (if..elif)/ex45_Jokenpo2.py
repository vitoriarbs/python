from time import sleep
from random import randint
computador = randint(1,3)
itens = (0, "Pedra", "Papel", "Tesoura")

print("{:=^20}" .format(" MINIJOGO "))
print("""
Informe sua jogada!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
""")
jogador = int(input(">> "))

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!\n")

print("-=" * 20)
print(f"O computador escolheu {itens[computador]}")
print(f"O jogador escolheu {itens[jogador]}")
print("-=" * 20)

#resultados
if (jogador == computador):
    print("EMPATE!")

elif (jogador != computador):
    if ((jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2)):
        print("Jogador VENCE!")
    
    else:
        print("Computador VENCE!")