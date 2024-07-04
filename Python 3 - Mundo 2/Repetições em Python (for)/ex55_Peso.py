for c in range(1,6):
    peso = float(input(f"{c}. Informe seu peso: "))

    if c == 1:
        maior_peso = peso
        menor_peso = peso

    else:
        if peso > maior_peso:
            maior_peso = peso
        
        if peso < menor_peso:
            menor_peso = peso

print(f"O MAIOR peso iformado foi de {maior_peso}")
print(f"O MENOR peso iformado foi de {menor_peso}")

