locadora = [ ]
filme_1 = {'título': 'Avengers', 'ano': 2012, 'gênero': 'Ação'}
filme_2 = {'título': 'Piratas do Caribe: Por Estranhas Marés', 'ano': 2011, 'gênero': ['Fantasia', 'Ação']}

locadora.append(filme_1)
locadora.append(filme_2)

print(locadora)
print(locadora[0])
print(locadora[1]['título'])
