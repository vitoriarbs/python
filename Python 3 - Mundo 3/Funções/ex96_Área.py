#Rotinas
def título():
    print("Controle de Terrenos")
    print("-" * 40)

def área(larg, comp):
    area = larg * comp
    print(f"A área de um terreno {larg}x{comp} é de {area}m2")


#Programa Principal
título()

l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))

área(l, c)