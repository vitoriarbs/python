#Rotinas
def notas(* notas, sit=0):
    param = dict()
    cont = soma = 0

    print("-=" * 30)
    print(notas)
    
    param['total'] = len(notas)
    for val in notas:
        if cont == 0:
            param['maior_nota'] = val
            param['menor_nota'] = val
            
        else:
            if val > param['maior_nota']:
                param['maior_nota'] = val

            if param['menor_nota'] > val:
                param['menor_nota'] = val
        
        cont += 1
        soma += val

    param['média'] = soma / param['total']
    
    if sit:
        if param['média'] < 4:
            param['situação'] = 'RUIM'

        elif param['média'] < 7:
            param['situação'] = 'RAZOÁVEL'

        else:
            param['situação'] = 'BOA'

    return param

#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)