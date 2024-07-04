from random import randint

print("{:=^20}" .format(" MINIJOGO "))
print("""
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
""")

usuario = int(input("Informe é a sua jogada: "))
comput = randint(1,3)

print("-=*20")

#jogadas do computador
if comput == 1: 
    print("Computador jogou PEDRA")

elif comput == 2:
    print("Computador jogou PAPEL")

elif comput == 3:
    print("Computador jogou TESOURA")

#jogadas do usuario
if usuario == 1:
    print("Jogador jogou PEDRA")

elif usuario == 2:
    print("Jogador jogou PAPEL")

elif usuario == 3:
    print("Jogador jogou TESOURA")

print("-=*20")

#resultados
if (usuario == comput):
    print("EMPATE!")

elif (usuario != comput):
    if usuario == 1:
        if comput == 2:
            print("Computador VENCE") 
        elif comput == 3:
            print("Jogador VENCE!")
    
    if usuario == 2:
        if comput == 1:
            print("Jogador VENCE!")
        elif comput == 3:
            print("Computador VENCE!")

    if usuario == 3: 
        if comput == 1:
            print("Computador VENCE!")
        if comput == 2:
            print("Jogador VENCE!")