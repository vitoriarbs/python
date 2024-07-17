jogador = dict()
gols = list()
tot_gols = 0

jogador['nome'] = str(input("Nome do Jogador: ")).strip().title()
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?"))

for c in range(0, partidas):
   gol = int(input(f"Quantos gols na partida {c}?"))
   gols.append(gol)
   tot_gols += gol
jogador['gols'] = gols
jogador['total'] = tot_gols

print("-=" * 40)
print(jogador)
print("-=" * 40)

for key, val in jogador.items():
   print(f"O campo {key} tem o valor {val}.")
print("-=" * 40)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")

for ind, val in enumerate(jogador['gols']):
   print(f"   => Na partida {ind}, fez {val} gols.")
print(f"Foi um total de {tot_gols} gols.")