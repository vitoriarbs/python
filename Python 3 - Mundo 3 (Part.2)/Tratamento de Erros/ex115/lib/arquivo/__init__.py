from lib.interface import head

'''abrindo e escrevendo no arquivo para testar
arquivo = open(nome, 'w')
arquivo.write("Arquivo aberto")
arquivo.close()
'''
def existir_arquivo(nome):
    try:
        arquivo = open(nome, 'rt') #'rt' = arquivo será aberto em modo text
        arquivo.close()

    except FileNotFoundError: #se o arquivo não for encontrado
        return False
    
    else: #se conseguirmos abrir e fechar o arquivo
        return True

def criar_arquivo(title):
    try:
        arquivo = open(title, 'wt+')
        arquivo.close()

    except:
        print('\033[31mERRO: A criação do arquivo falhou!\033[m')
    
    else: 
        print(f"Arquivo {title} criado com sucesso!")

def ler_arquivo(title):
    try:
        arquivo = open(title, 'rt')

    except:
        print('\033[31mERRO: não foi possível ler o arquivo\033[m')

    else:
        head("PESSOAS CADASTRADAS")
        for val in arquivo:
            dados = val.split(';')
            print(f"{dados[0]:<30} {dados[1]:>3}")

    finally: #irá acontecer se der certo ou se der errado
        arquivo.close()

def cadastrar(title, nome='Desconhecido', idade=0):
    try:
        arquivo = open(title, 'a') #'a' = append, adicionar coisas
    
    except:
        print("\033[31mERRO: Não foi possível abrir o arquivo\033[m")

    else:
        try:
            arquivo.write(f'{nome}; {idade}')
            arquivo.write("\n")
        except:
            print("\033[31mERRO: Dados inválidos\033[m")

        else:    
            print(f"Novo registro de {nome} adicionado com sucesso!")
            arquivo.close()
        