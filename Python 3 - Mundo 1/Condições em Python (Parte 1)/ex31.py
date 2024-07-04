distancia = float(input("Informe a distância da sua viagem: R$ "))
preco = distancia * 0.50 if (distancia <= 200) else distancia * 0.45

'''if distancia <= 200:
    preco = distancia * 0.50
    print(f"O preço da passagem será de R${valor:.2f}")

else:
    preco = distancia * 0.45
    print(f"O preço da passagem será de R${valor:.2f}")'''
print(f"O preoço da sua passagem será de R${preco:.2f}")