from utilidadesCeV.moedas import resumo
from utilidadesCeV.dados import validação

#Programa Principal
valor = validação("Informe o valor: R$")
aumento = int(input("Informe o aumento: "))
redução = int(input("Informe a redução: "))

resumo(valor, moeda='U$', aumento=aumento, redução=redução)
