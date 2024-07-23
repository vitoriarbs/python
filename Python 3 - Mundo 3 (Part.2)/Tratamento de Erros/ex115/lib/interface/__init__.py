def leiaInteiro(msg):
    while True:
        try:
            opcao = int(input(msg))
            
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
            continue

        except (KeyboardInterrupt):
            print("\033[31mERRO: Usuário preferiu não digitar esse número.\033[m")
        
        #se o try der certo
        else:
            return opcao

def head(txt):
    print("\n")
    print("-=" * 30)
    print(txt.center(30))
    print("-=" * 30)

def menu(lista):
    head("MENU PRINCIPAL")

    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1

    opcao = leiaInteiro(">>>> ")
    return opcao


