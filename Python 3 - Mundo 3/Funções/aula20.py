#rotinas
def mensagen(msg):
    print("*" * 30)
    print(msg)
    print("*" * 30)

def soma(a, b):
    soma = a + b
    print(f"A soma de {a} + {b} = {soma}")

#Programa Principal

#comando personalizado utilizando parâmetros
mensagen("APRENDA PYTHON")
mensagen("  CURSO EM VIDEO  ")

#comando referenciando parâmetros
soma(b=4, a=18)
soma(7, 3)
