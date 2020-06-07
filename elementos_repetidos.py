def remove_repetidos(lista):
    lt = []
    for i in lista:
        if i not in lt:
            lt.append(i)
    lt.sort()
    return lt

lista = [1, 3, 5, 2, 3, 7, 5]

lista = remove_repetidos(lista)
print (lista)