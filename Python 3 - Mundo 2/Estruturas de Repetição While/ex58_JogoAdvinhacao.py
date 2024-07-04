from random import randint
num_computador = randint(0,10)
print(num_computador)
print("\n")
print("=" * 20 )
print("Sou seu computador...\nAcabei de pensar em um número entre 0 a 10.\nSerá que você consegue advinhar qual foi?")
num_usuario = int(input("Qual o seu palpite? "))
tentativas = 1
#acertou = False

#while not acertou
while num_computador != num_usuario:
    tentativas += 1
    if num_usuario > num_computador:
        num_usuario = int(input("Menos.. Tente mais uma vez.\nQual seu palpite? "))
    else:
        num_usuario = int(input("Mais.. Tente mais uma vez.\nQual seu palpite? "))
     

if (num_computador == num_usuario):
    print("Parebéns!", end=" ")
    if tentativas == 1:
        print("Você conseguiu de primeira!")    
    else:
        print(f"Você acertou com {tentativas} tentativas!")