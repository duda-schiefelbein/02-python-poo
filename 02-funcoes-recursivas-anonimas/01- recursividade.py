def fatorial(n):
    if n == 0:      #ponto de parada quando o n for zero
        return 1    # se ele chegar no zero ele vai retornar 1
    else:           # enquanto ele não chegar no zero o retorno
        return n * fatorial(n-1) # return vai ser sempre ele vezes o fatorial dele - 1.
print(fatorial(5)) #aqui vamos exibir o fatorial de 5 ex de fatorial(5*4*3*2*1)