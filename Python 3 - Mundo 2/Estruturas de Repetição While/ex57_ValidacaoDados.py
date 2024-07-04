sexo = str(input("Informe seu sexo [M/F]: ")).upper().strip()[0]

while sexo not in "MmFf":
    print("Valor informado é inválido!", end=" ")
    sexo = str(input("Informe novamente seu sexo [M/F]: ")).upper()

print(f"Sexo {sexo} registrado com sucesso!")