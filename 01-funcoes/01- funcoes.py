def dividir(n1, n2):
    if n2 == 0:
        print("Não é possivel dividir um número por zero")
    else:
        resultado = n1 / n2
        # print(f'O resultado da divisão é {resultado}')
        # print(f'{n1} / {n2}= {resultado}')
        return resultado

# print(f'O Resultado da divisão é {80/5}')
divisao = dividir(80, 8)
print("O resultado divisão é ", divisao)

print("Resultado", dividir(30, 0))

resultado = dividir(3, 1)
soma = 20 + resultado
print("A soma é", soma)

dividir(6, 3)