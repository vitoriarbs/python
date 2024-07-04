info = input('Digite algo: ')

#todo print irá retornar uma string
print('o tipo primitivo desse valor é: ', type(info)) 

print('Só tem espaços? {}'.format(info.isspace()) )
print('É um número? {}'.format(info.isnumeric()))
print('É alfabético? {}'.format(info.isalpha()))
print('É alfanumérico {}' .format(info.isalnum()))
print('Está em maiúsculas? {}'.format(info.isupper()))
print('Está em minúsculas? {}'.format(info.islower()))
print('Está capitalizada?', info.istitle())