from time import sleep

#Rotinas
def contador(início, fim, passo):
    print("-=" * 30)

    if passo == 0:
        return contador(início=início, fim=fim, passo= 1)
    
    elif fim > início:
        while True:
            #flush=True irá fazer com que o o print apareça a cada 0.5 segundos
            print(início, end=" ", flush=True)
            sleep(0.3)
            início += passo
            if início > fim:
                print("FIM!")
                break

    elif início > fim:
        if passo > 0:
            while True:
                print(início, end=" ", flush=True)
                início -= passo
                sleep(0.3)
                if início < fim:
                    print("FIM!")
                    break
        elif passo < 0:
            while True:
                print(início, end=" ", flush=True)
                início += passo
                sleep(0.3)
                if início < fim:
                    print("FIM!")
                    break
#Programa Princial
contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Inicío: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))

contador(ini, fim, pas)