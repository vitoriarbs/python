#from datetime import date
ano = int(input("Qual ano você gostaria de analisar? Caso queira analisar o ano atual digite 0"))

'''if ano == 0:
    ano = date.today().year'''

print(f"O ano {ano} é BISSEXTO!" if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0) else f"O ano {ano} NÃO é bissexto!")