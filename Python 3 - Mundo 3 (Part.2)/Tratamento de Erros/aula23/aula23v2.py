#operação
try: 
    n = int(input("Numerador: "))
    d = int(input("Denominador: "))
    r = n / d

#acontece se der erro
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')

#acontece se der não der erro
else:
    print(f"O resultado é {r:.3f}")

#acontece sempre, nas duas situações 
finally:
    print("Volte sempre! Muito obrigado!")