#operação
try: 
    n = int(input("Numerador: "))
    d = int(input("Denominador: "))
    r = n / d

#acontece se der erro
except:
    print('Infelizmente tivemos um problema: :(')

#acontece se der não der erro
else:
    print(f"O resultado é {r:.3f}")

#acontece sempre, nas duas situações 
finally:
    print("Volte sempre.")