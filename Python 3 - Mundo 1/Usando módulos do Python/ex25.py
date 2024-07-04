#Procurando uma string dentro de outra

nome = str(input("Qual seu nome completo? "))

nome = nome.strip().title()

print(f"Seu nome tem Silva? {"Silva" in nome}")