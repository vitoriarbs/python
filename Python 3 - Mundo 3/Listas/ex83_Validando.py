pares = []


tot = (str(input("Informe a expressão: ")))

for simbolo in tot:
    if simbolo == '(':
        pares.append('(')

    elif simbolo == ')':
        if len(pares) > 0:
            pares.pop()
        else:    
            pares.append(')')
            break

if len(pares) == 0:
    print("Sua expressão é válida")
else:
    print("Sua expressão é inválida")