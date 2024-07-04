peso = float(input("Informe seu peso: "))
alt = float(input("Informe sua altura: "))
imc = peso / (alt ** 2)

print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")

elif imc < 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL")

elif imc < 30:
    print("Você está OBESO!")

else:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")