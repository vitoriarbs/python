def menu():
    print("-=" * 50)
    print("MENU PRINCIPAL")
    print("-=" * 50)
    print("""
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do Sistema
""")
    opcao = leiaInteiro(">>>> ")
    print(f"{opcao}ooo")
    return opcao

def leiaInteiro(msg):
    while True:
        try:
            opcao = int(input(msg))
            if opcao <= 3:
                return opcao
            else:
                print("ERRO! Digite uma opção válida!")
                return menu()
            
        except (ValueError, TypeError):
            print("ERRO: Por favor, digite um número inteiro válido.")
            continue


def main():
    opc = menu()

    if opc == 3:
        print("Saindo do Sistema... Até logo!")

main()