def validação(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).strip().replace(",", ".") #vai continuar pedindo para informar o preço
        if entrada.isalpha() or entrada == "": #se tiver letras ou for um espaço vazio
            print(f'ERRO: \"{entrada}\" é um preço inválido!')
        else:
            válido = True
            return float(entrada)