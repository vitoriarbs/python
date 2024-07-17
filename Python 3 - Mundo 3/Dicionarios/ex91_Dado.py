from random import randint
from time import sleep

jogo = dict()

print("Valores sorteados:")
for c in range(1, 5):
    resultado = randint(1, 6)
    jogo[f'jogador{c}'] = resultado

#mostrando jogadores e seus resultados
for key, val in jogo.items():
    print(f"    O  {key} tirou {val}")

#colocando dic em ordem
#key=lambda item: item[1]' faz com o sort seja feito a partir dos valores que os jogadores obtiveram. Se quiser fazer com as keys ao invés dos valores, use item[0].
#reverse=True faz com que seja organizado do maior par o menor
jogo_ordenado = dict(sorted(jogo.items(), key=lambda item:item[1], reverse=True))

print("\n==   Rankeando Jogadores   ==")

c = 0
while c < len(jogo):
    for key, val in jogo_ordenado.items():
       c += 1
       print(f"    {c} lugar: {key} com {val}")
    