#REVISAR VÍDEO
valores = []

for pos in range(0, 5):
    num = int(input(f"{pos}. Informe o valor: "))

    if pos == 0:
        valores.append(num)
        print("Adicionado ao final da lista..")

    elif num > valores[-1]:
        valores.append(num)
        print(f"Adicionado ao final da lista..")
        
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos += 1

#insert(1, 105)
print("=" * 40)
print(f"Os valores digitados em ordem foram: {valores}")
