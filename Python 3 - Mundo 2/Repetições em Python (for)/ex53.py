frase = str(input("Informe uma frase: ")).strip().upper().split()
palavra = "".join(frase)
inverso = ''

for letra in range(len(palavra) -1, -1, -1):
    #print(palavra[letra])
    inverso += palavra[letra]
print(palavra, inverso)
if inverso == palavra:
    print("Temos é um palíndromo")   
else:
    print("NÃO temos um palíndromo")

"""if frase == frase[::-1]:
    print(f"{frase} é um palíndromo")
else:
    print(f"{frase} NÃO é um palíndromo")"""