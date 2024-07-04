while True:
    c = 1
    tab = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 20)

    if tab >= 0:
        #podemos fazer com qualquer laço de repetição
        while True:
            print(f"{tab} x {c:2} = {tab * c}")
            c += 1
            if c > 10:
                break
    else:
        print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")
        break
    
    print("=" * 40)