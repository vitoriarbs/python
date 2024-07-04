palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS",
             "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")
vogais = ("a", "e", "i", "o", "u")


for pos, p in enumerate(palavras):
    print(f"{pos}. Na palavra {p} temos:", end=" ")
    
    for vogal in p:
        if vogal.upper() in "AEIOU":
            print(vogal, end=" ")
    print("\n")
