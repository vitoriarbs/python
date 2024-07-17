matriz = [[], [], []]

for m0 in range (0,3):
    matriz[0].append((input(f"Digite um valor para [0, {m0}]: ")))

for m1 in range (0,3):
    matriz[1].append((input(f"Digite um valor para [0, {m1}]: ")))

for m2 in range (0,3):
    matriz[2].append((input(f"Digite um valor para [0, {m2}]: ")))

print("-=" * 40)
for val in matriz[0]:
    print(f"[{val}]", end=" ")
print("")

for val in matriz[1]:
    print(f"[{val}]", end=" ")
print("")

for val in matriz[2]:
    print(f"[{val}]", end=" ")