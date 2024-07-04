print("=" * 20)
print("10 TERMOS DE UMA PROGRASSÃO ARITMÉTICA - (PA)")
print("=" * 20)
n1 = int(input("Inform o primeiro termo: "))
razao = int(input("Razão: "))
decimo_termo = n1 + (10 - 1) * razao

for c in range(n1, decimo_termo, razao):
    print(c, end=" > ")

print("Fim!!!")