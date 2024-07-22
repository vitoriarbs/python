# Rotinas
def fatorial(num, show=0):
    """_fatoria(n, show=False)_
        
    Args:
        num (_inteiro_): _número a ser calculado_
        c (_inteiro_): _contador, diminui até chegar a 1 e é utilizado como multiplicador para num_
        show (_boolean_): valor opcional. caso seja true irá mostrar o calculo sendo realizado

    Returns:
        _num_:  O valor final do número fatorado_
    """
    print("-=" * 40)
    c = num
    while True:
        if show == True:
            print(f"{c} x ", end="")
            c -= 1
            num *= c
            if c == 1:
                print(f"{c} = ", end="")
                return num
        else:
            c -= 1
            num *= c

            if c == 1:
                return num

#Programa Principal
help(fatorial)
print(fatorial(8, True))
