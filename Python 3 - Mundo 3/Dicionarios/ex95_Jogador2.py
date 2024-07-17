jogador = dict()
gols = list()
time = list()


while True:
    
    jogador['nome'] = str(input("Qual o nome do jogador? ").strip().title())
    jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for c in range(1, jogador["partidas"] + 1):
        gols.append(int(input(f"Quantos gols na partida {c}: ")))

    tot_gols = 0    
    for g in gols:
        tot_gols += g

    jogador['gol'] = gols[:]
    jogador['total'] = tot_gols

    gols.clear()
    time.append(jogador.copy())

    #validação
    while True:
        opcao = str(input("Deseja continuar [S/N]? "))
        if opcao not in "NnSs":
            print("ERRO: Informe apenas S ou N")
        else:
            break
    if opcao in "Nn":
        break

print("=-" * 40)
print("cod nome gols tot")
print("--" * 40)

for ind, val in enumerate(time):
    print(f"{ind} {val['nome']} {val['gol']} {val['total']}")

while True:
    cod = int(input("Buscar dados de qual jogador? (999 para parar)"))
    if cod == 999:
        break
    elif cod == len(time):
        print(f"ERRO: Não existe jogador com cod {cod}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[cod]["nome"]}")
        for ind, val in enumerate(time[cod]['gol']):
            print(f" No partida {ind + 1} fez {val} gols")
        print()