#Rotinas
#trabalhando com tuplas
def contador(* num):
    tam = len(num)
    print("Rcebi os valores", end=" ")
    
    for val in num:
        print(val, end=" ")
    
    print(f"e são ao todo {tam} números")
    print(num)#criará uma tupla

#Programa Principal
#empacotando parâmetros
contador(2, 1, 55)
contador(8, 0)
contador(4, 6, 99, 1021, 1, 32)