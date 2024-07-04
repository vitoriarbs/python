velocidade = float(input("Informe a velocidade: "))

print("MULTA! Limite de velocidade ultrapassado" if (velocidade > 80) else "OK")

if (velocidade > 80):
    velocidade -= 80
    multa = velocidade * 7
    print(f"Sua multa será de R${multa:.2f}.")

