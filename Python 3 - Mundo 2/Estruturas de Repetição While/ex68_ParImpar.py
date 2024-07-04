from random import randint
win = 0

print("=" * 40)
print("{:-^40}".format("VAMOS JOGAR PAR OU ÍMPAR"))

while True:
    usuario = int(input("Informe um valor: "))
    comput = randint(0, 10)
    tot = usuario + comput
    opcao = " "

    while opcao not in "PpIi":
        opcao = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    
    #resultados
    print(f"Você jogou {usuario} e o computador {comput}. Total {tot}", end=" ")
    
    #se der par
    if tot % 2 == 0:
        print(f"DEU PAR")
        if opcao in "Pp":
            print("Você VENCEU!")
            win += win    

        elif opcao in "Ii":
            print("Você PERDEU!")
            break
    
    #se der ímpar
    else: 
        print(f"DEU ÍMPAR")
        if opcao in "Ii":
            print("Você VENCEU!")
            win += 1

        elif opcao in "Pp":
            print("Você PERDEU!")
            break
    
    print("Vamos jogar novamente!")
    print("-" * 40)

#tratando plural com if
print("=" * 40)
print(f"GAME OVER! Você venceu {win} vezes." if win > 1 or win == 0 else f"GAME OVER! Você venceu {win} vez.")