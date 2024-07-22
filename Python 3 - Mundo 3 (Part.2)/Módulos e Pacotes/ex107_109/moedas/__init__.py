def aumentar(num, taxa):
    resposta = num + (num * (taxa/100))
    return resposta

def diminuir(num, taxa):
    resposta = num * (1 - (taxa/100))
    return resposta

def dobrar(num):
    resposta = num * 2
    return resposta

def metade(num):
    resposta = num / 2
    return resposta

def moeda_format(num, param=0):
    if param:
        return f"R$ {num:.2f}"
    else:
        return f"{num}"