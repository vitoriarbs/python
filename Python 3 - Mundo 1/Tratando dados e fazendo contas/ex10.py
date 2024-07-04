# Décimo Quarto Desafio - Escreva um programa que converta uma temperatura digitada em graus Celsius para Farenhein
temp = float(input('Qual a temperatura atual em C: '))
print(f'A temperatura de {temp}C corresponde a {(9*temp) / 5 + 32:.2f}F')
print('-'*12,'\n')

#Décimo Quinto Desafio - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
km = float(input('Foram quantos Km rodados? '))
dia = int(input('Foram quantos dias alugados? '))
print(f'O total a pagar é de R${(dia * 60)+(km * 0.15):.2f}')