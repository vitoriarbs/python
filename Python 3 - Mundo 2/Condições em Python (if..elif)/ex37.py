print("=" * 20)
num = int(input("Infome o número: "))
menu = int(input("""\n
Como você gostaria de converter seu número?
[1]Binário
[2]Octal
[3]Hexadecimal
=>> """))

if menu == 1:
    print(f"{num} convertido para BINÁRIO é igual a: {bin(num)[2:]}")
elif menu == 2:
    print(f"{num} convertido para OCTAL é igual a: {oct(num)[2:]}")
elif menu == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a: {hex(num)[2:]}") 
else:
    print("Opcão informada é inválida!")
