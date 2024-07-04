num = int(input("Digite um número para calcular seu Fatorial: "))
print(f"Calculando {num}!", end=" ") 
c = num
tot = 1

while  c != 1:
    print(f"{c} x", end=" ")
    if c == num:
        tot = num * (c - 1) #4! 4 x 3 = 12
    elif c < num:
        tot = tot * (c - 1) #12 x 2 = 24
    c -= 1
    
print(f"{c} = {tot}")