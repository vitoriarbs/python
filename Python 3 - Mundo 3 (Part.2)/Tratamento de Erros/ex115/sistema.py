from lib.interface import *
from lib.arquivo import *

arquivo = 'cadastros.txt'

if not existir_arquivo(arquivo) == True:
    print("arquivo não encontrado")
    criar_arquivo(arquivo)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])


    if resposta == 1:
        ler_arquivo(arquivo)

    elif resposta == 2:
        head("Novo Cadastro")
        
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))

        cadastrar(arquivo, nome, idade)

    elif resposta == 3:
        print("Saindo do Sistema... Até logo!")
        break

    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
