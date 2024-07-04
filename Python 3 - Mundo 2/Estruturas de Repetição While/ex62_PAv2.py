#ERROS DE LÓGICA

print("\nGERADOR DE PA\n", "-=" * 10)
num = int(input("Primeiro termo: "))
pulo = int(input("Razão da PA: "))
cont = 1
totcont = 0

while cont != 0:
    print(f"{num} >", end=" ")
    num +=  pulo
    totcont += 1

    if totcont >= 10:
        print("PAUSA")
        cont = int(input("Quantos termos você quer motrar a mais? "))
        totcont += cont
        parador = 1

        while cont > parador:
            print(f"{num} >", end=" ")
            num +=  pulo
            parador += 1

print(f"Progressão finalizada com {totcont} termos mostrados.")