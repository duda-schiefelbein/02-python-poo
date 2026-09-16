def somar(n1,n2):
    return n1+n2

def subtrair(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2
    
def dividir(n1, n2):
    if n2 == 0:
        print("Não é possivel dividir um número por zero")
    else:
        resultado = n1 / n2
        # print(f'O resultado da divisão é {resultado}')
        # print(f'{n1} / {n2}= {resultado}')
        return resultado
print (somar(90,789))
print (subtrair(90,789))
print (multiplicar(90,789))
print (dividir(90,789))
    
    

'''# print(f'O Resultado da divisão é {80/5}')
divisao = dividir(80, 8)
print("O resultado divisão é ", divisao)

print("Resultado", dividir(30, 0))

resultado = dividir(3, 1)
soma = 20 + resultado
print("A soma é", soma)

dividir(6, 3)'''