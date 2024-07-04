nome = str(input("Digite seu nome completo: "))

#split tira espaços desnecessários
#title irá colocar a primeira letra após um espaço em maiúsculo
#split irá separar a string em lista 
nome = nome.strip().title().split()

print(nome)

print(f"Prazer te conhecer, {nome[0]}!")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[-1]}")
