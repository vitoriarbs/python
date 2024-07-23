#Rotinas
def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))

        #erro de valor ou de tipo
        except (ValueError, TypeError):
            print(f"\033[31mERRO! Digete um valor inteiro válido!")
            continue #joga direto para o while novamente

        except (KeyboardInterrupt):
            print("\n\033[31mERRO: Entrada de dados interrompida pelo usuário.")
            return 0

        else:
            return valor
        
        
def leiaFloat(msg):
    while True:
        try:
            valor = int(input(msg))

        #erro de valor ou de tipo
        except (ValueError, TypeError):
            print(f"\033[31mERRO! Digete um valor real válido!\033")
            continue #joga direto para o while novamente

        except (KeyboardInterrupt):
            print("\n\033[31mERRO: Entrada de dados interrompida pelo usuário.\033")
            return 0

        else:
            return valor
        
num_int = leiaInt('Digite um valor inteiro: ')
num_float = leiaFloat('Digite um valor real: ')
print(f"O valor inteiro digitado foi {num_int} e o real foi {num_float}")