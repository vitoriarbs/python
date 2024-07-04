# Décimo Segundo Desafio - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# ou novo_preço = val - (val * (5/100))
val = float(input('Informe o preço do produto: R$'))
print(f'Parabén! Este produto possui um deconto de 5%. Ele sairá por {val*(1 - 0.05):.2f}')
print('-'*20,'\n')

# Décimo Segundo Desafio - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Informe o salário do funcionário: R$'))
print(f'Parabéns! Você recebeu um aumente de 15%. Seu novo salário será de {sal*(1+0.15):.2f}')
print('-'*20,'\n')