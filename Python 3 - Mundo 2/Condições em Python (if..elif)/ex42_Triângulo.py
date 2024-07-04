print("=" * 20)
print("ANALISADOR DE TRIÂNGULOS \n")
t1 = float(input("Informe o primeiro segmento: "))
t2 = float(input("Informe o segundo segmento: "))
t3 = float(input("Informe o terceiro segmento: "))

# a soma de dois segmentos deve ser menor que o terceiro
if (t3 < t1 + t2) and (t2 < t1 + t3) and (t1 < t2 + t3):
    print("Parabéns! Os segmentos acima podem formar um triângulo", end=" ")
    
    if (t1 == t2) and (t2 == t3):
        print("EQUILÁTERO!")

    elif (t1 != t2) and (t1 != t3) and (t2 != t3):
        print("ESCALENO!")

    else:
        print("ISÓCELES!")

else:
    print("ERRO: Os segmentos acima não podem formar um triângulo!")
