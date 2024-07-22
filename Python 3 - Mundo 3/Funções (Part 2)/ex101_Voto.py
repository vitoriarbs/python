from datetime import date
ano = date.today().year()

#Rotinas
def voto():
    print("-=" * 40)
    ano_nasc = int(input("Informe o ano de nascimento: "))
    idade = ano - ano_nasc

    print(f"Com {idade}:", end="")
    if idade < 16:
        return  "VOTO NEGADO"

    elif idade < 21 or idade > 65:
        return "VOTO OPCIONAL"

    else:
        return "VOTO OBRIGATÓRIO"
    
#Variáveis Globais
resultado = voto()

#Programa Principal
print(resultado)