print("\nGERADOR DE PA\n", "-=" * 10)
num = int(input("Primeiro termo: "))
pulo = int(input("Razão da PA: "))
cont = 1

while cont <= 10:
    print(f"{num} >", end=" ")
    num +=  pulo
    cont += 1
print("FIM!")