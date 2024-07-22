# Rotinas
def maior(* num):
    cont = maior = 0

    print("-=" * 30)
    print("Analisando os valores passados...")
    for val in num:
        print(f"{val}", end=" ")
        if cont == 0:
            maior = val
        else:
            if val > maior:
                maior = val
        cont += 1

    print(f"Foram informados {len(num)} ao todo. O maior valor informado foi {maior}")


#Variáveis globais
nums = list()

#Programa Principal
maior(1, 3, 4, 5)
maior(1, 5)