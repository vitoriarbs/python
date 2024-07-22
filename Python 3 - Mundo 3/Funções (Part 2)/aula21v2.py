#parâmetros OPCIOANAIS, mesmo se não forem passados o código não dará erro 
def contador(i=0, f=0, p=0):
    #DOCSTRING - clicar em ctrl + (" x3)
    """Faz uma contagem e mostra na tela

    Args:
        i (_type_): _início da contagem_
        f (_type_): _fim da contagem_
        p (_type_): _passo da contagem_
    """
    c=i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM!")

contador(2, 10)

#help(contador)