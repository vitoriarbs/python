#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Em que cidade você nasceu? ").strip().title())

cidade = cidade.split()

print(cidade)

print({"Santo" in cidade[0]})
#print(cidade[0] == 'Satnto')