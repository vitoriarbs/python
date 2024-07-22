#Rotinas

def aumentar(valor, moeda, taxa, format):
    resposta = valor + (valor * (taxa/100))
    res_format = moeda_format(resposta, moeda, format)
    return res_format if format else resposta 

def reduzir(valor, moeda, taxa, format):
    resposta = valor * (1 - (taxa/100))
    res_format = moeda_format(resposta, moeda, format)
    return res_format if format else resposta

def dobrar(valor, moeda, format):
    resposta = valor * 2
    res_format = moeda_format(resposta, moeda, format)
    return res_format if format else resposta

def metade(valor, moeda, format):
    resposta = valor / 2
    res_format = moeda_format(resposta, moeda, format)
    return res_format if format else resposta

def moeda_format(valor, moeda, format):
    if format:
        return f"{moeda}{valor:.2f}".replace(".", ",")
    else:
        return f"{valor:.2f}".replace(".", ",")
    

#Programa Principal que será mostrado
def resumo(valor, moeda='R$', aumento=0, redução=0, format=True):
    print("-" * 40)
    print("RESUMO DO VALOR")
    print("-" * 40)
    print(f"""
Preço analisado: \t{moeda_format(valor, moeda, format)}
Metade do preço:\t{metade(valor, moeda, format)}
{aumento}% de aumento: \t{aumentar(valor, moeda, aumento, format)}
{redução}% de redução: \t{reduzir(valor, moeda, redução, format)}
Dobro do preço: \t{dobrar(valor, moeda, format)}

""")
