dados = []
dados.append("Pedro")
dados.append(25)
print(dados[0])

pessoas = [["Ana", 33], ["João", 19], ["Joaquim", 13]]
pessoas.append(dados[:])
dados.clear()
pessoas[1] = ["Maria", 19]

#mostrando dados compostos
print(pessoas)
print(pessoas[1])
print(pessoas[2][0])
for p in pessoas:
    print(p)

#adicionando dado com repetção
#for c in range(0,2):
#    dados.append(str(input("Nome: ")))
#    dados.append(int(input("Idade: ")))
#    pessoas.append(dados[:])
#    dados.clear()

for p in pessoas:
    #p[1] é onde fica a idade
    if p[1] >= 21:
        #p[0] é onde ficam os nomes
        print(f"{p[0]} é maior de idade")
    
    else:
        #p[0] é onde ficam os nomes
        print(f"{p[0]} é menor de idade")