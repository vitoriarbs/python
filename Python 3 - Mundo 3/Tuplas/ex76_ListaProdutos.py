print("=" * 40)
print("{:^40}".format("LISTAGEM DE PREÇOS"))
print("=" * 40)

lista = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.00, "Estojo", 25.00, "Transferidor", 4.20,
         "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livros", 34.90)

#for pos in range(0, len(linguagem)) - também serve
for pos, item in enumerate(lista):
    if pos % 2 == 0:
        print(f"{item:.<30}", end=" ")
    
    if pos % 2 != 0:
        print(f"R${item:>7.2f}")
print("="*40)