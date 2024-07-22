#Revisarr
#Rotinas
def leiaInt(msg):
    números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while msg not in números:
        print("ERRO! Digite um número inteiro válido")
        return False

#Programa Principal
print("-=" * 40)
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")

