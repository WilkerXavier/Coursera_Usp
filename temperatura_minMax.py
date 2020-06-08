def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")


def maxima(temps):
    max = temps[0]
    i = 1
    while  i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

def minima(temps):
    min = temps[0]
    i = 1
    while  i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min


def teste_pontual(temp,valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
         print("Valor errado para array ", temp)
         print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)


def testa_maxima():
    print("Iniciando os testes ")

    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 1], 1)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    teste_pontual([30, 27, 25, 29, 24, 22, 33, 32 ], 33)
    teste_pontual([-15, -12, 0, 20, 30], 30)

    print ("Finalisando os testes")


def testa_minima():
    print("Iniciando os testes ")

    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([30, 27, 25, 29, 24, 22, 33, 32 ], 22)
    teste_pontual([-15, -12, 0, 20, 30], -15)

    print ("Finalisando os testes")