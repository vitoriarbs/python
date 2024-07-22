from moedas import resumo

#Programa Principal
valor = float(input("Informe o valor: R$"))
aumento = int(input("Informe o aumento: "))
reduzir = int(input("Informe a redução: "))

resumo(valor, moeda='U$', aumento=aumento, redução=reduzir)
