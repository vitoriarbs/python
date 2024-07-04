n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))

#verificando quem é maior
if (n1 > n2) and (n1 > n3):
    maior  = n1
    
elif (n2 > n1) and (n2 > n3):
    maior = n2
else:
    maior = n3

#verificando quem é menor
if (n1 < n2) and (n1 < n3):
    menor  = n1
elif (n2 < n1) and (n2 < n3):
    menor = n2
else:
    menor = n3

print(f"{maior} é o MAIOR número")
print(f"{menor} é o MENOR número")