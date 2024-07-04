frase = str(input("Digite uma frase: "))

frase = frase.strip().lower()

print(f"A letra A aparece {frase.count('a')} vezes na frase.")
print(f"A primeira letra A apareceu na posição {frase.find('a')+1}")

#rfind irá preocurar da direita para a esquerda
print(f"A última letra A apareceu na posição {frase.rfind('a')+ 1}")