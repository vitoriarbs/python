#Rotina
def escreva(texto):
    print("*" * len(texto))
    print(texto)
    print("*" * len(texto))

#Programa Principal
txt = str(input("Informe o texto que deseja: "))
escreva(txt)