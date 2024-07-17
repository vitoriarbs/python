#Rotinas
#Trabalhando com listas
def dobra(num):
    c = 0
    while c < len(num):
        num[c] *= num[c] 
        c += 1
    print(num)

#Programa Principal
valores = [7, 2, 3, 4]
dobra(valores)