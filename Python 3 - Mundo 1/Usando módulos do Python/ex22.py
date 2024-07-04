#strip() irá retirar os espaços desnecessários do começo e do final da string
nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome..")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")

#len() irá contar a quantidade caracteres
# - nome(" ") irá subtrair os espaços em branco que ficaram no meio(entre uma palavra e outra) da string
print(f"Seu nome ao todo possui {len(nome) - nome.count(" ")} letras")

#split() divide uma string em listas 
#nome = (["vitoria"], ["rocha"], ["bernar"], ["silva"])
print(f"Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} caracteres")

"""
separador = nome.split()
print(f"Seu primeiro nome é {separador[0]} e ele tem {len(separador[0])} caracteres")
"""