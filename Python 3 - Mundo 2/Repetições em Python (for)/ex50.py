soma = 0
for c in range (1,7):
    num = int(input(f"{c}. Informe um número: "))
    if num % 2 == 0:
        soma += num
    
"""print("Dos números informados, os números pares são: ", end=" ")
print(num)"""
print(f"A soma dos números pares dos valores informados é igual a: {soma}")