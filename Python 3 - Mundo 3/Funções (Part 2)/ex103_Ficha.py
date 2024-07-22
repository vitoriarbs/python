#Rotinas
def ficha(jogador=0, gols=0):
    if jogador and gols:
        print(f"O jogador {jogador} fez {gols}(s) no campeonato.")
    elif jogador:
        print(f"O jogador {jogador} fez gols(s) no campeonato.")
    elif gols:
        print(f"O <jogador> fez {gols} gol(s) no campeonato.")

#Programa Principal
nome = str(input("Informe o nome do jogador: "))
gols = str(input("Informe o número de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)