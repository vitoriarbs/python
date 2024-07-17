#Rotinas
def contador(início, fim, passo):

    if passo == 0:
        return contador(início= início, fim= fim, passo= 1)
    
    elif fim > início:
        while True:
            print(início, end=" ")
            início += passo
            if início > fim:
                print("FIM!")
                break

    elif início > fim:
        if passo > 0:
            while True:
                print(início, end=" ")
                início -= passo
                if início < fim:
                    print("FIM!")
                    break
        elif passo < 0:
            while True:
                print(início, end=" ")
                início += passo
                if início < fim:
                    print("FIM!")
                    break
    
    
#Programa Princial
ini = int(input("Inicío: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))

contador(ini, fim, pas)